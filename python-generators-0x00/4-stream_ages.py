#!/usr/bin/env python3
"""
Memory-efficient aggregation using generators to calculate average age
"""

import seed


def stream_user_ages():
    """
    Generator that yields user ages one by one.
    
    Yields:
        int: User age
    """
    connection = seed.connect_to_prodev()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT age FROM user_data")
            
            for row in cursor:
                yield row[0]
                
        finally:
            cursor.close()
            connection.close()


def calculate_average_age():
    """
    Calculate the average age using the generator without loading
    the entire dataset into memory.
    
    Returns:
        float: Average age of users
    """
    total_age = 0
    count = 0
    
    for age in stream_user_ages():
        total_age += age
        count += 1
    
    if count == 0:
        return 0
    
    average_age = total_age / count
    return average_age


if __name__ == "__main__":
    average = calculate_average_age()
    print(f"Average age of users: {average}")
