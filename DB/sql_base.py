import sqlite3


class DB:
    def __init__(self):
        self.db_session_id = str()
        self.connection = sqlite3.connect('../DB/atm_app_db.sqlite3')
        self.connection.execute("""
            CREATE TABLE IF NOT EXISTS accounts
            (username text,password text,balance real)
        """)
        self.c = self.connection.cursor()

    def get_all_data(self):
        """
        Silly method :)
        :return: all db records as list of tuples
        """
        all_db_data = self.c.execute('SELECT * FROM accounts').fetchall()
        return all_db_data

    def is_username_already_exists(self, username):
        """
        :param username: username as a string
        :return: True if username found in db records or False
        """
        try:
            self.c.execute('SELECT username FROM accounts WHERE username = (?)', (username,)).fetchone()[0]
            return True
        except TypeError:
            return False

    def insert_data_for_new_account(self, username, password, balance):
        self.c.execute('INSERT INTO accounts VALUES(?,?,?)', (username, password, balance))
        self.connection.commit()
        return True

    def is_valid_user(self, username, password):
        """
        :param username: username as a string
        :param password: password as a string
        :return: True if provided credentials match record in db or False
        """
        if self.is_username_already_exists(username):
            if self.get_password_by_username(username) == password:
                return True
        return False

    def get_password_by_username(self, username):
        """
        :param username: username as a string
        :return: password as a string
        """
        password = self.c.execute('SELECT password FROM accounts WHERE username = (?)', (username,)).fetchone()[0]
        return password

    def delete_account(self, username):
        """
        :param username: username
        :return: True id successful
        """
        self.c.execute('DELETE FROM accounts WHERE username = (?)', (username,))
        self.connection.commit()
        return True

    def get_balance(self, username):
        """
        :param username: username as a string1
        :return: balance as a float
        """
        balance = self.c.execute('SELECT balance FROM accounts WHERE username = (?)', (username,)).fetchone()[0]
        return balance

    def update_balance(self, username, balance):
        self.c.execute('UPDATE accounts SET balance = (?) WHERE username = (?)', (balance,username,))
        self.connection.commit()
        return True
