import sqlite3
from pathlib import Path

class BaseModule():
    def __init__(self):
        self.__database = Path(Path.cwd(), "data", "inventory.db")

    def create_table(self, table, query):
        print(f"Creating table: {table}")

        conn = sqlite3.connect(self.__database)

        try:
            with conn:
                cursor = conn.cursor()

                cursor.execute(query)
            
            print(f"Table {table} created.")
        except sqlite3.IntegrityError as ex:
            print(f"ERROR: {ex}")

    def execute(self, query, params=None):
        conn = sqlite3.connect(self.__database)

        try:
            with conn:
                cursor = conn.cursor()

                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)

                return cursor.fetchall()
        except sqlite3.IntegrityError as ex:
            print(f"ERROR: {ex}")