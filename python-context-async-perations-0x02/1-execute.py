#!/usr/bin/env python3
"""
A class-based context manager to execute a database query.
"""

import sqlite3

class ExecuteQuery:
    """
    A context manager to handle database connection and query execution.
    """
    def __init__(self, db_path, query, params=None):
        """
        Initializes the context manager with the database path, query, and parameters.
        """
        self.db_path = db_path
        self.query = query
        self.params = params if params is not None else ()
        self.conn = None
        self.cursor = None

    def __enter__(self):
        """
        Opens the database connection, creates a cursor, and executes the query.
        Returns the cursor object to be used in the 'with' statement.
        """
        try:
            self.conn = sqlite3.connect(self.db_path)
            self.cursor = self.conn.cursor()
            self.cursor.execute(self.query, self.params)
            return self.cursor
        except sqlite3.Error as e:
            print(f"Database error during entry: {e}")
            if self.conn:
                self.conn.close()
            # Re-raise the exception to propagate it
            raise

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Closes the connection and handles potential exceptions.
        Commits changes if no exception occurred.
        """
        if self.conn:
            if exc_type:
                # Rollback changes if an exception occurred in the 'with' block
                self.conn.rollback()
                print("Transaction rolled back due to an error.")
            else:
                # Commit changes if the 'with' block completed successfully
                self.conn.commit()
            self.conn.close()
            print("Database connection closed.")

def main():
    """
    Main function to set up the database and use the context manager.
    """
    db_name = "test.db"

    # Set up a dummy database and table with some data
    try:
        with sqlite3.connect(db_name) as setup_conn:
            setup_cursor = setup_conn.cursor()
            setup_cursor.execute("DROP TABLE IF EXISTS users")
            setup_cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
            setup_cursor.executemany("INSERT INTO users (name, age) VALUES (?, ?)", [
                ('Alice', 22),
                ('Bob', 30),
                ('Charlie', 28),
                ('Diana', 24)
            ])
            setup_conn.commit()
        print("Database set up with dummy data.")
    except sqlite3.Error as e:
        print(f"Error setting up database: {e}")
        return

    # Use the context manager to execute the required query
    query = "SELECT * FROM users WHERE age > ?"
    age_param = 25

    try:
        with ExecuteQuery(db_name, query, (age_param,)) as cursor:
            # The 'with' statement now gives us the cursor directly
            results = cursor.fetchall()
            print(f"\nResults for '{query}' with parameter '{age_param}':")
            for row in results:
                print(row)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
