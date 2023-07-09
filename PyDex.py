class UserAccount:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.is_active = True

class AccountManager:
    def __init__(self):
        self.accounts = []

    def create_account(self, username, password, email):
        new_account = UserAccount(username, password, email)
        self.accounts.append(new_account)
        print("Account created successfully!")

    def deactivate_account(self, username):
        for account in self.accounts:
            if account.username == username:
                account.is_active = False
                print(f"Account '{username}' deactivated successfully!")
                return
        print(f"Account '{username}' not found.")

    def display_active_accounts(self):
        active_accounts = [account for account in self.accounts if account.is_active]
        if active_accounts:
            print("Active Accounts:")
            for account in active_accounts:
                print(f"Username: {account.username}\tEmail: {account.email}")
        else:
            print("No active accounts found.")

    def display_all_accounts(self):
        if self.accounts:
            print("All Accounts:")
            for account in self.accounts:
                print(f"Username: {account.username}\tEmail: {account.email}\tActive: {account.is_active}")
        else:
            print("No accounts found.")

# Usage example
account_manager = AccountManager()

account_manager.create_account("johnDoe", "p@ssw0rd", "johndoe@example.com")
account_manager.create_account("janeSmith", "abcd1234", "janesmith@example.com")
account_manager.create_account("bobSmith", "qwerty", "bobsmith@example.com")
account_manager.display_all_accounts()

account_manager.deactivate_account("janeSmith")
account_manager.display_active_accounts()
