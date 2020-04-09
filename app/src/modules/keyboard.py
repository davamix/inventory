from modules.base_module import BaseModule

class KeyboardModule(BaseModule):
    def __init__(self, socket):
        super().__init__(socket)
        self.__module_name = "keyboard"

        self.__create_table()
    
    def __create_table(self):
        create_table_query = "CREATE TABLE IF NOT EXISTS keyboard(reference TEXT UNIQUE, model TEXT, layout TEXT)"

        self.create_table("keyboard", create_table_query)

    def save_data(self, data):
        if data["module"] == self.__module_name:
            save_query = "INSERT INTO keyboard(reference, model, layout) VALUES (?, ?, ?)"
            params = [data["reference"], data["model"], data["layout"]]

            self.save(save_query, params)

