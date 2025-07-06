#!/usr/bin/env python3
"""
Generator functions for batch processing of user data
"""

import seed


def stream_users_in_batches(batch_size):
    """
    Generator that fetches rows in batches from user_data table.
    
    Args:
        batch_size (int): Number of rows to fetch in each batch
        
    Yields:
        list: A batch of user records as dictionaries
    """
    connection = seed.connect_to_prodev()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM user_data")
            
            while True:
                batch = cursor.fetchmany(batch_size)
                if not batch:
                    break
                yield batch
                
        finally:
            cursor.close()
            connection.close()


def batch_processing(batch_size):
    """
    Processes each batch to filter users over the age of 25.
    
    Args:
        batch_size (int): Size of each batch to process
    """
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user['age'] > 25:
                print(user)
