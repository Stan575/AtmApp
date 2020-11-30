from App.Menu import Menu


class MainMenu(Menu):
    def __init__(self):
        super(MainMenu, self).__init__()

    @staticmethod
    def print_welcome_page():
        print('=' * 25 +
              '\nWelcome to AtmApp\n'
              'Main Menu:\n'
              '1 Login\n'
              '2 Create an account\n'
              '3 Exit\n' +
              '=' * 25)

    def select_action(self):
        action_number = input('Please select action: ')
        if action_number in ('1', '2', '3'):
            return action_number
        else:
            print('Please select action number: 1 or 2 or 3')
