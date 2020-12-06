from DB.sql_base import DB


class TempDB(DB):
    def __init__(self):
        super(TempDB, self).__init__()
        self.db = DB()


    print(DB().get_all_data())

    # print(DB().is_username_already_exists('Johny'))
    # DB().delete_account()