#!usr/bin/env python3

import sqlite3

class DatabaseConnection:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = None
        
    def __enter__(self):
        self.conn = sqlite3.connect(self.db_path)
        return self.conn
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.conn:
            if exc_type is not None:
                self.conn.rollback()
                print("Transaction rolled back due to an error")
            else:
                self.conn.commit()
            self.conn.close()
            print("Database connection closed.")
    
def main():
        try:
            
            with sqlite3.connect("test.db") as conn:
                cursor = conn.cursor()
                cursor.execute("DROP TABLE IF EXISTS users")
                cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
                cursor.execute("INSERT INTO users (name) VALUES ('Alice')")
                cursor.execute("INSERT INTO users (name) VALUES ('Bob')")
            
            with DatabaseConnection("test.db") as db_conn:
                cursor = db_conn.cursor()
                cursor.execute("SELECT * FROM users")
                results = cursor.fetchall()
                print("\nQuery results:")
                for row in results:
                    print(row)
        except Exception as e:
            print(f"An error occurred: {e}")
if __name__ == "__main__":
        main()