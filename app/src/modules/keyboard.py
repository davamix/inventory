from modules.base_module import BaseModule

# TODO: Create a base module to manage the DB connection
class KeyboardModule(BaseModule):
    def __init__(self):
        super().__init__()
        self.__module_name = "keyboard"

        self.__create_table()
    
    def __create_table(self):
        create_table_query = "CREATE TABLE IF NOT EXISTS keyboard(reference TEXT UNIQUE, model TEXT, layout TEXT)"

        self.create_table("keyboard", create_table_query)

    def save(self, data):
        if data["module"] == self.__module_name:
            save_query = "INSERT INTO keyboard(reference, model, layout) VALUES (?, ?, ?)"
            params = [data["reference"], data["model"], data["layout"]]

            self.execute(save_query, params)