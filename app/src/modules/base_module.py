import sqlite3
from pathlib import Path
from flask_socketio import emit

class BaseModule():
    def __init__(self, socket):
        self.__socket = socket
        self.__database = Path(Path.cwd(), "data", "inventory.db")

    def create_table(self, table, query):
        print(f"Creating table: {table}")

        try:
            self.__execute(query)
            print(f"Table {table} created.")
        except sqlite3.Error as ex:
            print(f"ERROR: {ex}")

    # TODO: Move emit's to inherited modules
    def save(self, query, params=None):
        try:
            self.__execute(query, params)
            self.__socket.emit("saved", True)
        except sqlite3.Error as ex:
            self.__socket.emit("saved", {"error": str(ex)})
            print(f"ERROR: {ex}")

    def __execute(self, query, params=None):
        conn = sqlite3.connect(self.__database)

        try:
            with conn:
                cursor = conn.cursor()

                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)

                return cursor.fetchall()
        except:
            raise