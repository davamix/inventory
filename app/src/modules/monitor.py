from modules.base_module import BaseModule

class MonitorModule(BaseModule):
    def __init__(self, socket):
        super().__init__(socket)
        self.__module_name = "tv" # Monitor is detected as TV

        self.__create_table()
    
    def __create_table(self):
        create_table_query = "CREATE TABLE IF NOT EXISTS monitor(reference TEXT UNIQUE, model TEXT, inches TEXT, resolution TEXT)"

        self.create_table("monitor", create_table_query)

    def save_data(self, data):
        if data["module"] == self.__module_name:
            save_query = "INSERT INTO monitor(reference, model, inches, resolution) VALUES (?, ?, ?, ?)"
            params = [data["reference"], data["model"], data["inches"], data["resolution"]]

            self.save(save_query, params)