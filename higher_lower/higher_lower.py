import os
import game_data, art
import random

list_of_accounts = game_data.data

def get_random_accounts(account1):
    #generate
    while True:
        account2 = random.choice(list_of_accounts)
        if account1 != account2:
            return account2
        
def format_data(account):
    """Format the account data into printable format"""
    account_name = account['name']
    account_descr = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_descr}, from {account_country}"

correct_answer = True
player_score = 0
account1 = random.choice(list_of_accounts)
account2 = get_random_accounts(account1)

print(art.logo)
while correct_answer:
    print(f'Compare A: {format_data(account1)}')
    print(art.vs)
    print(f'Against B: {format_data(account2)}')

    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    if user_choice == 'a':
        if account1['follower_count'] > account2['follower_count']:
            player_score += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(art.logo)
            print(f"You're right! Current score: {player_score}")
            account2 = get_random_accounts(account1) 
        else:
            correct_answer = False
    elif user_choice == 'b':
        if account1['follower_count'] < account2['follower_count']:
            player_score += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(art.logo)
            print(f"You're right! Current score: {player_score}")
            account1 = account2
            account2 = get_random_accounts(account1)
        else:
            correct_answer = False
else:
    print(f"Sorry, that's wrong. Final score: {player_score}")



