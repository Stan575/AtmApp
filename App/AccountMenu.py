from DB.sql_base import *
from App.Menu import Menu
import App.MainMenu


class AccountMenu(Menu):
    def __init__(self, username):
        super(AccountMenu, self).__init__()
        self.username = username
        self.account_active = True


    def print_account_menu(self):
        print('=== Account Menu ===\n'
              '1 Current Balance\n'
              '2 Deposit Money\n'
              '3 Withdraw Money\n'
              '4 Send Money\n'
              '5 Logout\n'
              '6 Close Account\n' + '=' * 25)
        return self

    def action_selection(self):
        action_number = input('Please select action: ')
        if action_number in ('1', '2', '3', '4', '5', '6'):
            return action_number
        else:
            print('Please select action number: 1 or 2 or 3 or 4 or 5 or 6')
