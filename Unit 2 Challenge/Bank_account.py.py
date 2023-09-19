class BankAccount:
    def __init__(self, acc_number, acc_holder_name, initial_balance):
        self.__account_number = acc_number
        self.__account_holder_name = acc_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        self.__account_balance += amount

    def withdraw(self, amount):
        if self.__account_balance >= amount:
            self.__account_balance -= amount
        else:
            print("Insufficient funds")

    def display_balance(self):
        return self.__account_balance

# Create an instance of BankAccount
account1 = BankAccount("1234567890", "John Doe", 1000)

# Test deposit and withdrawal functionality
account1.deposit(500)
account1.withdraw(200)

# Display the account balance
print(f"Account balance for {account1._BankAccount__account_holder_name}: {account1.display_balance()}")
