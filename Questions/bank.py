class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    # Deposit amount into the account
    def deposit(self, amount):
        if amount <= 0:
            return "Deposit amount must be positive."
        self.balance += amount
        return f"Deposited {amount}. Current balance is {self.balance}"

    # Withdraw amount from the account
    def withdraw(self, amount):
        if amount <= 0:
            return "Withdrawal amount must be positive."
        if amount > self.balance:
            return "Insufficient funds."
        self.balance -= amount
        return f"Withdrew {amount}. Current balance is {self.balance}"

    # Check current balance
    def check_balance(self):
        return f"Current balance is {self.balance}"

    # Transfer amount to another account
    def transfer(self, amount, recipient_account):
        if amount <= 0:
            return "Transfer amount must be positive."
        if amount > self.balance:
            return "Insufficient funds for transfer."
        self.balance -= amount
        recipient_account.balance += amount
        return f"Transferred {amount} to {recipient_account.account_holder}. Current balance is {self.balance}"


if __name__ == "__main__":
    account1 = BankAccount("123456", "John Doe", 1000)
    account2 = BankAccount("654321", "Jane Smith", 500)

    print(account1.deposit(500))  # Deposit operation
    print(account1.withdraw(200))  # Withdrawal operation
    print(account1.check_balance())  # Check balance
    print(account1.transfer(300, account2))  # Transfer operation
    print(account2.check_balance())  # Check recipient balance
