import sys
from App.MainMenu import MainMenu
from App.Session import Session
from App.CreateAccount import CreateAccount


class AtmApp:
    def __init__(self):
        self.main_menu = MainMenu()

    def run_atm(self):
        while(True):
            self.main_menu.print_welcome_page()
            main_menu_selection = self.main_menu.select_action()
            if main_menu_selection == '3':
                print('\n=== See you soon! ===')
                sys.exit(0)
            else:
                session = Session()
                if main_menu_selection == '1':
                    while session.logged_in is not True:
                        if session.user_login() is not False:
                            session.start_session()
                        else:
                            session.connection.close()
                            sys.exit(0)
                elif main_menu_selection == '2':
                    creds = CreateAccount().new()
                    session.new_user_login(creds).start_session()
                session.connection.close()
                del session

if __name__ == "__main__":
    AtmApp().run_atm()
