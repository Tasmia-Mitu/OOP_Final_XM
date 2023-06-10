
class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.balance = 0
        self.loan = 0
        self.transactions = []

    def login(self, email, password):
        if self.email == email and self.password == password:
            print("User login successful!")
            print('-------------------------')
            return True
            
        else:
            print("Invalid user credentials.")
            return False
            

    def logout(self):
        print("User logout successful.")
        print('-------------------------')

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited: {amount}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f"Withdrawn: {amount}")
            print(f"{self.balance} Withdrawal successful.")
            print("after withdraw balance:", self.balance)
        else:
            print("The bank is bankrupt")

    def transfer(self, amount, recipient):
        if self.balance >= amount:
            self.balance -= amount
            recipient.balance += amount
            self.transactions.append(f"Transferred: -{amount} to {recipient.email}")
            recipient.transactions.append(f"Received: +{amount} from {self.email}")
        else:
            print("The bank is bankrupt")

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.transactions

    def take_loan(self):
        print('---Loan History----')
        loan_amount = self.balance * 2
        self.balance += loan_amount
        self.loan += loan_amount
        self.transactions.append(f"Loan taken: {loan_amount}")
        print("Loan taken successfully.")
