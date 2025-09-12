# Context Managers & Async Programming in Python

This project shows how to manage database connections and run queries efficiently using context managers and asynchronous programming.

## Key Concepts

- **Context Managers:**
	- Use the `with` statement to set up and clean up resources automatically.
	- `__enter__` starts the resource, `__exit__` cleans it up (even if there’s an error).

- **Database Connection Management:**
	- Context managers open and close database connections for you, preventing leaks.

- **Asynchronous Programming:**
	- Use `async`/`await` and `aiosqlite` to run database operations without blocking your program.
	- Lets you run multiple queries at the same time.

- **Concurrent Execution:**
	- `asyncio.gather()` lets you run several async tasks together, making things faster when tasks are independent.

## Tools Used

- `sqlite3` and `aiosqlite` for database work
- `asyncio` for async programming
- `contextlib` for context manager utilities

## Real-World Examples

- Web apps: Make sure database connections are always closed after each request.
- Data pipelines: Easily run many similar queries with reusable code.
- Dashboards: Load multiple datasets at once for faster reports.
- Microservices: Handle many requests at the same time efficiently.
- Testing: Clean up test databases after each test automatically.

---
This summary helps you understand how context managers and async programming make Python code safer, faster, and easier to maintain.