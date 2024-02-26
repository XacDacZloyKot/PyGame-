# import os
# import sqlite3
# import settings

# class Database(object):
#     __DB_LOCATION = os.path.join(settings.BASE_DIR, "db.sqlite3")

#     def __init__(self):
#         try:
#             self.db_exists = os.path.exists(Database.__DB_LOCATION)

#             self.connection = sqlite3.connect(Database.__DB_LOCATION)
#             self.cur = self.connection.cursor()

#             if not self.db_exists:
#                 self.create_table()

#         except Exception as e:
#             print(f"Error during database initialization: {e}")

#     def __enter__(self):
#         return self

#     def __exit__(self, ext_type, exc_value, traceback):
#         try:
#             self.cur.close()
#             if isinstance(exc_value, Exception):
#                 self.connection.rollback()
#             else:
#                 self.connection.commit()
#             self.connection.close()
#         except Exception as e:
#             print(f"Error during database cleanup: {e}")

#     def close(self):
#         try:
#             self.connection.close()
#         except Exception as e:
#             print(f"Error closing database connection: {e}")

#     def execute(self, sql, params=None):
#         try:
#             if params is None:
#                 self.cur.execute(sql)
#             else:
#                 self.cur.execute(sql, params)
#         except Exception as e:
#             print(f"Error executing SQL query: {e}")

#     def create_table(self):
#         try:
#             self.cur.execute('''CREATE TABLE IF NOT EXISTS player (
#                                 name TEXT,
#                                 kill INTEGER,
#                                 score INTEGER)''')
#         except Exception as e:
#             print(f"Error creating table: {e}")

#     def commit(self):
#         try:
#             self.connection.commit()
#         except Exception as e:
#             print(f"Error committing transaction: {e}")
            
#     def fetch_all(self):
#         return self.cur.fetchall()

import os
import sqlite3
import settings
import logging
from datetime import datetime

class Database(object):
    __DB_LOCATION = os.path.join(settings.BASE_DIR, "db.sqlite3")
    __LOG_FILE_PATH = os.path.join(settings.BASE_DIR, "db_actions_log.txt")

    def __init__(self):
        try:
            self.db_exists = os.path.exists(Database.__DB_LOCATION)
            self.connection = sqlite3.connect(Database.__DB_LOCATION)
            self.cur = self.connection.cursor()

            if not self.db_exists:
                self.create_table()

        except Exception as e:
            self.log_error(f"Error during database initialization: {e}")

    def __enter__(self):
        return self

    def __exit__(self, ext_type, exc_value, traceback):
        try:
            self.cur.close()
            if isinstance(exc_value, Exception):
                self.connection.rollback()
            else:
                self.connection.commit()
            self.connection.close()
        except Exception as e:
            self.log_error(f"Error during database cleanup: {e}")

    def close(self):
        try:
            self.connection.close()
        except Exception as e:
            self.log_error(f"Error closing database connection: {e}")

    def execute(self, sql, params=None):
        try:
            if params is None:
                self.cur.execute(sql)
            else:
                self.cur.execute(sql, params)
            self.log_action(f"Executed SQL: {sql} with params: {params}")
        except Exception as e:
            self.log_error(f"Error executing SQL query: {e}")

    def create_table(self):
        try:
            self.cur.execute('''CREATE TABLE IF NOT EXISTS player (
                                name TEXT,
                                kill INTEGER,
                                score INTEGER)''')
            self.log_action("Created 'player' table")
        except Exception as e:
            self.log_error(f"Error creating table: {e}")

    def commit(self):
        try:
            self.connection.commit()
            self.log_action("Committed transaction")
        except Exception as e:
            self.log_error(f"Error committing transaction: {e}")

    def fetch_all(self):
        return self.cur.fetchall()

    def log_error(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"{timestamp} - ERROR - {message}"

        logging.basicConfig(filename=Database.__LOG_FILE_PATH, level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.error(log_message)

    def log_action(self, action):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"{timestamp} - {action}"

        logging.basicConfig(filename=Database.__LOG_FILE_PATH, level=logging.INFO, format='%(asctime)s - %(message)s')
        logging.info(log_message)
