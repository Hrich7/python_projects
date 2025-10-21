import jaydebeapi
import yaml
import os
import time
import datetime
import json

# Optional: same driver/jar as your main script
JDBC_DRIVER = "oracle.jdbc.OracleDriver"
JAR_PATH = "app/lib/ojdbc8.jar"
TIMEOUT_MS = 5000

# Log file for failed connections
FAILED_LOG_FILE = "app/connection_failures.log"

def validate_timezone():
    """Ensure TZ is valid to avoid ORA-01882."""
    tz = os.getenv("TZ")
    if not tz:
        print("⚠️  No TZ environment variable set. Defaulting to UTC.")
        os.environ["TZ"] = "UTC"
        time.tzset()
    else:
        try:
            time.tzset()
            print(f"🕒 Timezone validated: {tz}")
        except Exception as e:
            print(f"⚠️  Invalid timezone '{tz}', falling back to UTC. ({e})")
            os.environ["TZ"] = "UTC"
            time.tzset()

def connect_to_oracle(hostname, conf):
    """Test connection to Oracle DB — try RAC first, then SID."""
    username = conf.get("username")
    password = conf.get("password")
    port = conf.get("port")
    service_name = conf.get("service", conf.get("sid"))
    sid = conf.get("sid")

    # If CDB, prefix username with C## if missing
    notes = conf.get("notes", "")
    if "cdb" in notes.lower() and not username.upper().startswith("C##"):
        username = f"C##{username}"

    props = {
        "user": username,
        "password": password,
        "oracle.net.CONNECT_TIMEOUT": str(TIMEOUT_MS),
        "oracle.net.READ_TIMEOUT": str(TIMEOUT_MS)
    }

    urls_to_try = [
        f"jdbc:oracle:thin:@//{hostname}:{port}/{service_name}",  # RAC style
        f"jdbc:oracle:thin:@{hostname}:{port}:{sid}"              # non-RAC
    ]

    for jdbc_url in urls_to_try:
        try:
            print(f"[{hostname}] Connecting as {username} to {jdbc_url}")
            conn = jaydebeapi.connect(JDBC_DRIVER, jdbc_url, props, JAR_PATH)
            curs = conn.cursor()
            curs.execute("SELECT 1 FROM dual")
            curs.close()
            conn.close()
            print(f"[{hostname}] ✅ Connection successful.")
            return True
        except Exception as e:
            err = str(e)
            print(f"[{hostname}] ❌ Connection failed for {jdbc_url}: {err}")
            if "ORA-12514" in err or "service" in err.lower():
                print(f"[{hostname}] 🔄 Retrying with alternate format...")
                continue
            else:
                return err

    return "All connection attempts failed."

def log_failure(dbname, hostname, error):
    """Append failure to log file with timestamp."""
    with open(FAILED_LOG_FILE, "a") as f:
        ts = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = {
            "timestamp": ts,
            "database": dbname,
            "hostname": hostname,
            "error": error
        }
        f.write(json.dumps(log_entry) + "\n")

def main():
    validate_timezone()

    with open("app/databases.yml", "r") as f:
        config = yaml.safe_load(f)

    total = 0
    failed = 0

    for db in config.get("databases", []):
        hostname = db["hostname"]
        sid = db.get("sid")
        dbname = f"{sid}_{hostname}"
        result = connect_to_oracle(hostname, db)

        total += 1
        if result is not True:
            failed += 1
            log_failure(dbname, hostname, result)

    print(f"\n=== Connection Summary ===")
    print(f"Total databases tested: {total}")
    print(f"Successful connections: {total - failed}")
    print(f"Failed connections: {failed}")

    if failed > 0:
        print(f"See {FAILED_LOG_FILE} for details.")

if __name__ == "__main__":
    main()
