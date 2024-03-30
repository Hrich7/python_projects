import os


class Person:

    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name

class Customer(Person):

    def __init__(self, first_name, last_name, account_number, balance=0) -> None:
        super().__init__(first_name, last_name)
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
         self.balance += amount
         print("Deposit Accepted")
    
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            print("Withdraw done")
        else:
            print("Insufficent Funds")


    def __str__(self) -> str:
        return f"Client: {self.first_name} {self.last_name}\nAccount Number : {self.account_number}\
    \nAccount Balance: {self.balance}"
    


def create_customer():
    first_name = input("Please Enter your first name: ")
    last_name = input("Please enter your last name: ")
    account_number = input("Enter your account balance: ")
    customer = Customer(first_name, last_name, account_number)
    return customer

def main():
    os.system('clear')
    my_customer = create_customer()
    print(my_customer)

    option = 0
    while option != 'E':
        print("Choose:\n- Deposit(D)\n- Withdraw(W)\n- Exit(E)")
        option = input('> ')

        if option == 'D':
            deposit_amount = int(input("Deposit Amount: "))
            my_customer.deposit(deposit_amount)
        elif option == 'W':
            withdraw_amount = int(input("Withdraw Amount: "))
            my_customer.withdraw(withdraw_amount)
        
        print(my_customer)
    print("Thank you! Come again")
if __name__ == '__main__':
    main()