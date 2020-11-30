from DB.sql_base import DB


class AccountActions(DB):
    def __init__(self):
        super(AccountActions, self).__init__()

    def __format_amount(self, amount):
        return "{0:.2f}".format(amount)

    def balance(self, username):
        balance_flt = self.get_balance(username)
        print(f'{username}\'s account balance: ${self.__format_amount(balance_flt)}')

    def deposit(self, username):
        amount_str = input('Deposit amount: $')
        amount_flt = float(amount_str)
        if amount_flt > 0.01:
            current_balance_flt = self.get_balance(username)
            new_balance_flt = current_balance_flt + amount_flt
            self.update_balance(username, new_balance_flt)
            print(f'${self.__format_amount(amount_flt)} deposited to your account\nCurrent balance: '
                  f'${self.__format_amount(self.get_balance(username))}')
            return True
        else:
            print('!!! Deposit amount must be more than $0.01 !!!')
            return False

    def withdraw(self, username):
        current_balance_flt = self.get_balance(username)
        if current_balance_flt == 0:
            print('!!! Current balance is $0.00 !!!')
            return False
        amount_str = input('Amount to withdraw: $')
        amount_flt = float(amount_str)
        if amount_flt <= 0:
            print('!!! Withdraw amount must be more than $0.00 !!!')
            return False
        if amount_flt > current_balance_flt:
            print('!!! You can withdraw up to {} !!!'.format(self.__format_amount(current_balance_flt)))
            return False
        current_balance_flt = self.get_balance(username)
        new_balance_flt = current_balance_flt - amount_flt
        self.update_balance(username, new_balance_flt)
        print(f'${self.__format_amount(amount_flt)} Withdrawn from your account\nCurrent balance: '
              f'${self.__format_amount(self.get_balance(username))}')
        return True

    def send(self, username):
        current_balance_flt = self.get_balance(username)
        if current_balance_flt == 0:
            print('!!! Current balance is $0.00 !!!')
            return False
        receiver = input('Who send money: ')
        if receiver == username:
            print('!!! You trying to send money yourself !!!'.format(receiver))
            return False
        if not self.is_username_already_exists(receiver):
            print('!!! {} not found !!!'.format(receiver))
            return False
        amount_str = input('Amount to send: $')
        amount_flt = float(amount_str)
        if amount_flt <= 0.01:
            print('!!! You can send only more than $0.00 !!!')
            return False
        if amount_flt > current_balance_flt:
            print('!!! You can send up to {} !!!'.format(self.__format_amount(current_balance_flt)))
            return False
        new_balance_flt = current_balance_flt - amount_flt
        self.update_balance(username, new_balance_flt)
        receiver_balance_flt = self.get_balance(receiver)
        self.update_balance(receiver, receiver_balance_flt + amount_flt)
        print(f'You sent ${self.__format_amount(amount_flt)} to {receiver}\nCurrent balance: '
              f'${self.__format_amount(self.get_balance(username))}')
        return True

    def delete(self, username):
        zero_balance = self.get_balance(username) == 0
        confirm_password = input('Enter password: ')
        password_confirmed = self.get_password_by_username(username) == confirm_password
        if zero_balance and password_confirmed:
            uname = username
            self.delete_account(username)
            print(f'=== {uname} account has been deleted ===')
            return True
        else:
            if not zero_balance:
                print('!!! Account balance must be $0.00 !!!')
            else:
                print('!!! Password is incorrect !!!')
            return False
