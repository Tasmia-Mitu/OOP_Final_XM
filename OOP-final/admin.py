
class Admin:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def login(self, email, password):
        if self.email == email and self.password == password:
            print("Admin login successful!")
            return True
        else:
            print("Invalid admin credentials.")
            return False

    def logout(self):
        print("Admin logout successful.")

    def check_total_balance(self, accounts):
        total_balance = sum(account.balance for account in accounts)
        print("Total available balance: ", total_balance)

    def check_total_loan(self, accounts):
        total_loan = sum(account.loan for account in accounts)
        print("Total loan amount: ", total_loan)

    def loan_feature(self, enable):
        if enable:
            print("Loan feature enabled.")
        else:
            print("Loan feature disabled.")
