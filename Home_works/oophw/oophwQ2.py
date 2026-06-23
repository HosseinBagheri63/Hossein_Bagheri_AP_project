class BankAccount():
    #account_holder: str
    #_transaction_history: list[str]
    #__balance: int
    def __init__(self, account_holder: str):
        self.account_holder= account_holder
        self._transaction_history= []
        self.__balance= 0
    
    def deposit(self, amount:int):
        self.__balance+= amount
        self._transaction_history.append(f"Deposited ${amount}")

    def withdraw(self, amount:int):
        if amount > self.__balance:
            print("Insufficient funds!")
            return
        self.__balance-= amount
        self._transaction_history.append(f"Withdrew ${amount}")
    
    @property
    def balance(self):
        print(f"Balance: ${self.__balance}")
        return self.__balance
#مطئن نبودم که منظور صورت سوال برگرداندن مقدار موجودی است یا چاپ کردن آن
    @property
    def transaction_history(self):
        print(self._transaction_history)
        return self._transaction_history

# Create account
account = BankAccount("John")
# Test all methods
account.balance # Balance: $0
account.deposit(100) # Deposited $100
account.withdraw(30) # Withdrew $30
account.withdraw(100) # Insufficient funds!  
account.balance # Balance: $70
account.transaction_history # Show all transactions

account.account_holder = "Reza"
print(account.account_holder)
#it is possible to change the account holder name, and it is should not be

class SavingsAccount(BankAccount):
    pass

SAccount= SavingsAccount("ali")
SAccount._transaction_history    #this class can access _transaction_history
#SAccount.__balance                
SAccount.deposit(123123)
SAccount.balance
#SavingAccount class can inherit balance attribute but cannot access it directly