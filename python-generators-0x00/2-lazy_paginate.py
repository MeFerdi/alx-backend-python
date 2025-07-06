#!/usr/bin/env python3
"""
Lazy pagination implementation using generators
"""

import seed


def paginate_users(page_size, offset):
    """
    Fetch a page of users from the database.
    
    Args:
        page_size (int): Number of users per page
        offset (int): Starting position in the dataset
        
    Returns:
        list: List of user records for the page
    """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    connection.close()
    return rows


def lazy_pagination(page_size):
    """
    Generator that implements lazy loading of paginated data.
    Only fetches the next page when needed.
    
    Args:
        page_size (int): Number of records per page
        
    Yields:
        list: A page of user records
    """
    offset = 0
    
    while True:
        page = paginate_users(page_size, offset)
        if not page:
            break
        yield page
        offset += page_size
