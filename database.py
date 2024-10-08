import sqlite3

class Database:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name):
        self.cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table_name}
                             (id INTEGER PRIMARY KEY, user_text TEXT, response TEXT)''')
        self.conn.commit()

    def insert_conversation(self, user_text, response):
        self.cursor.execute(f"INSERT INTO {DB_TABLE} (user_text, response) VALUES (?, ?)",
                             (user_text, response))
        self.conn.commit()

    def get_conversation_history(self):
        self.cursor.execute(f"SELECT * FROM {DB_TABLE}")
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()
