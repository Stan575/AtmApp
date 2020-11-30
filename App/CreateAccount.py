from DB.sql_base import DB


class CreateAccount(DB):
    def __init__(self):
        super(CreateAccount, self).__init__()
        self.__username = str()
        self.__password = str()
        self.__unique_username = False

        self.db = DB()

    def new(self):
        print('*' * 25 + '\nCreating account:')
        # username must be unique
        while self.__unique_username is False:
            self.__username = input('Enter username: ').strip()
            if self.db.is_username_already_exists(self.__username) is False:
                self.__unique_username = True
            else:
                print(f'{self.__username} is taken, create another one')
        self.__password = input('Enter password: ').strip()
        if self.db.insert_data_for_new_account(self.__username, self.__password, 0):
            new_acc_credentials = [self.__username, self.__password]
            print('=== New account has been created ===')
            return new_acc_credentials
        else:
            print('=== New account could not be created ===') # could not be
            return [None, None]
