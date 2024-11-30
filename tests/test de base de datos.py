import sqlite3

class PassKeeper:
    def _init_(self, db_name="passwords.db"):
        self.db_name = db_name
        self.create_table()

    def create_table(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS passwords (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    service TEXT NOT NULL,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL
                )
            """)
            conn.commit()

    def add_password(self, service, username, password):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO passwords (service, username, password)
                VALUES (?, ?, ?)
            """, (service, username, password))
            conn.commit()

    def delete_password(self, service):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM passwords WHERE service = ?", (service,))
            conn.commit()

    def view_passwords(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT service, username, password FROM passwords")
            return cursor.fetchall()