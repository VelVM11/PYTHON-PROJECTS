class Account:
    def __init__(self, user_id, pin, balance=0):
        self.user_id = user_id
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Insufficient funds."

    def transfer(self, target_account, amount):
        if amount <= self.balance:
            self.balance -= amount
            target_account.balance += amount
            return f"Transferred ${amount} to {target_account.user_id}. Your new balance: ${self.balance}"
        else:
            return "Insufficient funds."

    def get_balance(self):
        return f"Your balance: ${self.balance}"

class ATM:
    def __init__(self):
        self.accounts = {}
        self.current_user = None

    def create_account(self, user_id, pin):
        if user_id in self.accounts:
            return "User ID already exists. Please choose a different one."
        else:
            account = Account(user_id, pin)
            self.accounts[user_id] = account
            return "Account created successfully."

    def login(self, user_id, pin):
        if user_id in self.accounts and self.accounts[user_id].pin == pin:
            self.current_user = user_id
            return "Login successful."
        else:
            return "Invalid user ID or PIN. Please try again."

    def logout(self):
        self.current_user = None

    def menu(self):
        while True:
            print("\nATM MENU")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Transfer")
            print("4. Check Balance")
            print("5. Logout")
            print("6. Quit")
            choice = input("Enter your choice: ")

    class Account:
     def __init__(self, user_id, pin, balance=0):
        self.user_id = user_id
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Insufficient funds."

    def transfer(self, target_account, amount):
        if amount <= self.balance:
            self.balance -= amount
            target_account.balance += amount
            return f"Transferred ${amount} to {target_account.user_id}. Your new balance: ${self.balance}"
        else:
            return "Insufficient funds."

    def get_balance(self):
        return f"Your balance: ${self.balance}"

class ATM:
    def __init__(self):
        self.accounts = {}
        self.current_user = None

    def create_account(self, user_id, pin):
        if user_id in self.accounts:
            return "User ID already exists. Please choose a different one."
        else:
            account = Account(user_id, pin)
            self.accounts[user_id] = account
            return "Account created successfully."

    def login(self, user_id, pin):
        if user_id in self.accounts and self.accounts[user_id].pin == pin:
            self.current_user = user_id
            return "Login successful."
        else:
            return "Invalid user ID or PIN. Please try again."

    def logout(self):
        self.current_user = None

    def menu(self):
        while True:
            print("\nATM MENU")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Transfer")
            print("4. Check Balance")
            print("5. Logout")
            print("6. Quit")
            choice = input("Enter your choice: ")

            if choice == '1':
                amount = float(input("Enter the amount to deposit: "))
                print(self.accounts[self.current_user].deposit(amount))
            elif choice == '2':
                amount = float(input("Enter the amount to withdraw: "))
                print(self.accounts[self.current_user].withdraw(amount))
            elif choice == '3':
                target_user = input("Enter the target user ID: ")
                if target_user in self.accounts:
                    amount = float(input("Enter the amount to transfer: "))
                    print(self.accounts[self.current_user].transfer(self.accounts[target_user], amount))
                else:
                    print("Target user not found.")
            elif choice == '4':
                print(self.accounts[self.current_user].get_balance())
            elif choice == '5':
                self.logout()
                print("Logged out.")
            elif choice == '6':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    atm = ATM()
    while True:
        print("\nATM SYSTEM")
        print("1. Create Account")
        print("2. Login")
        print("3. Quit")
        option = input("Enter your choice: ")

        if option == '1':
            user_id = input("Enter your desired user ID: ")
            pin = input("Enter your desired PIN: ")
            print(atm.create_account(user_id, pin))
        elif option == '2':
            user_id = input("Enter your user ID: ")
            pin = input("Enter your PIN: ")
            login_result = atm.login(user_id, pin)
            if login_result == "Login successful.":
                atm.menu()
            else:
                print(login_result)
        elif option == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    atm = ATM()
    while True:
        print("\nATM SYSTEM")
        print("1. Create Account")
        print("2. Login")
        print("3. Quit")
        option = input("Enter your choice: ")

        if option == '1':
            user_id = input("Enter your desired user ID: ")
            pin = input("Enter your desired PIN: ")
            print(atm.create_account(user_id, pin))
        elif option == '2':
            user_id = input("Enter your user ID: ")
            pin = input("Enter your PIN: ")
            login_result = atm.login(user_id, pin)
            if login_result == "Login successful.":
                atm.menu()
            else:
                print(login_result)
        elif option == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
