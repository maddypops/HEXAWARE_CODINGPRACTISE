class BankAccount:

    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder  # Public attribute
        self.__balance = balance  # Private attribute

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited. New balance: {self.__balance}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        raise NotImplementedError("Withdraw method must be implemented by subclasses.")

    def get_account_info(self):
        raise NotImplementedError("get_account_info method must be implemented by subclasses.")


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.03):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        if self.get_balance() - amount >= 500:
            self.deposit(-amount)
            print(f"{amount} withdrawn from Savings Account.")
        else:
            print("Insufficient balance! Minimum balance of 500 must be maintained.")

    def calculate_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f"Interest of {interest} added.")

    def get_account_info(self):
        return f"SavingsAccount: Holder: {self.account_holder}, Balance: {self.get_balance()}"


class CurrentAccount(BankAccount):
    def __init__(self, account_holder, balance=0, overdraft_limit=1000):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if self.get_balance() - amount >= -self.overdraft_limit:
            self.deposit(-amount)  # Using negative deposit to reduce balance
            print(f"{amount} withdrawn from Current Account.")
        else:
            print("Exceeded overdraft limit!")

    def get_account_info(self):
        return f"CurrentAccount: Holder: {self.account_holder}, Balance: {self.get_balance()}"

def main():
    savings = SavingsAccount("Vishnu", balance=2000, interest_rate=0.04)
    current = CurrentAccount("Vishwa", balance=500, overdraft_limit=1000)


    accounts = [savings, current]

    for account in accounts:
        print("\n" + account.get_account_info())
        account.deposit(500)
        account.withdraw(1000)

        if isinstance(account, SavingsAccount):
            account.calculate_interest()

    print("\nFinal Account Information:")
    for account in accounts:
        print(account.get_account_info())

if __name__ == "__main__":
    main()


