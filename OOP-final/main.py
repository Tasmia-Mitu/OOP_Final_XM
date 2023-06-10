
from admin import Admin
from user import User

def main():
    # Create admin instance
    admin = Admin("admin@example.com", "admin123")
    # Create user instance
    user = User("user@example.com", "user123")

    # Admin login
    admin.login("admin@example.com", "admin123")
    # Admin checks total available balance
    accounts = [user]
    admin.check_total_balance(accounts)

    # Admin checks total loan amount
    admin.check_total_loan(accounts)

    # Admin enables the loan feature
    admin.loan_feature(True)

    # User login
    user.login("user@example.com", "user123")

    # User deposits money
    user.deposit(1000)

    # User checks available balance
    balance = user.get_balance()
    print("Available balance: ", balance)

    # User withdraws money
    user.withdraw(500)

    # User transfers money to another user
    recipient = User("recipient@example.com", "recipient123")
    user.transfer(200, recipient)

    # User checks transaction history
    transaction_history = user.get_transaction_history()
    print("-----Transaction history:-----")
    for transaction in transaction_history:
        print(transaction)

    # User takes a loan
    user.take_loan()

    # Admin checks total loan amount after loan taken
    admin.check_total_loan(accounts)

    
    admin.logout()

if __name__ == '__main__':
    main()
