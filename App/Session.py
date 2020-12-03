import sys
from App.AccountMenu import AccountMenu
from App.AccountActions import AccountActions


class Session(AccountActions):
    def __init__(self):
        super(Session, self).__init__()
        self.logged_in = False
        self.username = str()
        self.password = str()
        self.acc_menu = AccountMenu(self.username)
        self.attempt_count = 0

    def user_login(self):
        while self.attempt_count < 4:
            print('=' * 25 + '\n=== Please login ===')
            self.username = input('Enter username: ')
            self.password = input('Enter password: ')
            if self.is_valid_user(self.username, self.password):
                self.logged_in = True
                print(f'\n=== Hello {self.username} ===')
                return self
            else:
                self.attempt_count += 1
                if self.attempt_count < 3:
                    print('=== Invalid login or password, try again ===')
                else:
                    print('=== Invalid login or password entered 3 times ===')
                    print('=== Please come back later ===')
                    return False

    def new_user_login(self, credentials):
        self.username = credentials[0]
        self.password = credentials[1]
        if self.is_valid_user(self.username, self.password):
            self.logged_in = True
            print(f'\n=== Hello {self.username} ===')
            return self
        else:
            return False

    def start_session(self):
        while True:
            self.acc_menu.print_account_menu()
            action_menu_selection = self.acc_menu.action_selection()
            # Action 1: Current balance
            if action_menu_selection == '1':
                self.balance(self.username)
            # Action 2: Deposit Money
            elif action_menu_selection == '2':
                self.deposit(self.username)
            # TODO: Action 3: Withdraw Money
            elif action_menu_selection == '3':
                self.withdraw(self.username)
            # Action 4: Send Money
            elif action_menu_selection == '4':
                self.send(self.username)
            # Action 5: Logout
            elif action_menu_selection == '5':
                self.logout()
                break
            # Action 6: Close Account
            elif action_menu_selection == '6':
                if self.delete(self.username): break  # if account deleted jump into main menu

    def logout(self):  # logout and exit
        uname = self.username
        self.logged_in = False
        self.username = None
        self.password = None
        print(f'=== {uname} logged out ===\n=== See you soon! ===')
        self.connection.close()
        sys.exit(0)
