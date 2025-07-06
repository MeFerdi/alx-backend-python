#!/usr/bin/env python3
"""
Generator function to stream rows from the user_data table one by one
"""

import seed


def stream_users():
    """
    Generator that streams rows from user_data table one by one.
    Uses yield to return one user at a time as a dictionary.
    """
    connection = seed.connect_to_prodev()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM user_data")
            
            for row in cursor:
                yield row
                
        finally:
            cursor.close()
            connection.close()
