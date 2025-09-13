#!/usr/bin/env python3
"""
This script demonstrates how to run multiple database queries concurrently
using asyncio.gather() and the aiosqlite library.
"""

import asyncio
import aiosqlite
import os

DB_PATH = "users.db"

async def setup_database():
    """Sets up a dummy database with a users table."""
    # Using a synchronous connection for the one-time setup
    # to avoid mixing async and sync database operations.
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("DROP TABLE IF EXISTS users")
        await db.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
        
        # Insert some dummy data
        users_data = [
            ("Alice", 25),
            ("Bob", 42),
            ("Charlie", 30),
            ("Diana", 45),
            ("Eve", 50),
            ("Frank", 35)
        ]
        await db.executemany("INSERT INTO users (name, age) VALUES (?, ?)", users_data)
        await db.commit()
    print("Database setup complete.")


async def async_fetch_users():
    """
    Asynchronous function to fetch all users from the database.
    This coroutine pauses to let other tasks run while waiting for I/O.
    """
    print("\nStarting to fetch all users...")
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT * FROM users") as cursor:
            users = await cursor.fetchall()
            print("Completed fetching all users:")
            for user in users:
                print(f"  {user}")
            return users


async def async_fetch_older_users():
    """
    Asynchronous function to fetch users older than 40.
    """
    print("\nStarting to fetch older users...")
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT * FROM users WHERE age > ?", (40,)) as cursor:
            older_users = await cursor.fetchall()
            print("Completed fetching older users:")
            for user in older_users:
                print(f"  {user}")
            return older_users


async def fetch_concurrently():
    """
    The main asynchronous function that orchestrates the concurrent queries.
    It first sets up the database, then uses asyncio.gather() to run
    the two fetch coroutines concurrently.
    """
    # First, make sure the database is set up
    await setup_database()
    
    # Use asyncio.gather() to run both queries at the same time
    print("\nRunning both queries concurrently with asyncio.gather() ...")
    all_users, older_users = await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )
    
    print("\nAll queries have completed. Results received.")
    print(f"Total users fetched: {len(all_users)}")
    print(f"Total older users fetched: {len(older_users)}")


if __name__ == "__main__":
    # Remove the old database file if it exists to ensure a clean run
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    
    # Run the main asynchronous function
    asyncio.run(fetch_concurrently())
