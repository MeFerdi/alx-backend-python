# Python Generators - Advanced Usage

This project demonstrates advanced usage of Python generators to efficiently handle large datasets, process data in batches, and simulate real-world scenarios involving live updates and memory-efficient computations.

## Learning Objectives

- Master Python Generators: Create and utilize generators for iterative data processing
- Handle Large Datasets: Implement batch processing and lazy loading
- Simulate Real-world Scenarios: Develop solutions for streaming contexts
- Optimize Performance: Use generators for memory-efficient aggregate calculations
- Apply SQL Knowledge: Integrate Python with databases for robust data management

## Requirements

- Python 3.x
- MySQL database server
- mysql-connector-python package
- python-dotenv package
- Understanding of yield and generator functions
- Basic SQL knowledge

## Setup

1. Install required packages:
```bash
pip install -r requirements.txt
```

2. Configure environment variables:
   - Copy `.env.example` to `.env`
   - Update the database credentials in `.env`:
   ```bash
   cp .env.example .env
   ```
   - Edit `.env` and add your MySQL password:
   ```
   DB_HOST=localhost
   DB_USER=root
   DB_PASSWORD=your_mysql_password
   DB_NAME=ALX_prodev
   ```

3. Run the seed script to populate the database:
```bash
python3 seed.py
```

## Files

- `seed.py`: Database setup and data seeding with environment variable configuration
- `0-stream_users.py`: Generator to stream users one by one
- `1-batch_processing.py`: Batch processing with generators
- `2-lazy_paginate.py`: Lazy loading paginated data
- `4-stream_ages.py`: Memory-efficient aggregation for average age calculation
- `.env`: Environment variables for database configuration (not tracked in git)
- `.env.example`: Template for environment variables
- `requirements.txt`: Python package dependencies
- `.gitignore`: Git ignore file for Python projects

## Usage

Each file contains specific generator implementations for different use cases:

### Task 0: Database Setup
```bash
# Make sure your .env file is configured first
python3 seed.py
```

### Task 1: Stream Users
```python
from stream_users import stream_users
for user in stream_users():
    print(user)
```

### Task 2: Batch Processing
```python
from batch_processing import batch_processing
batch_processing(50)  # Process in batches of 50
```

### Task 3: Lazy Pagination
```python
from lazy_paginate import lazy_pagination
for page in lazy_pagination(100):
    for user in page:
        print(user)
```

### Task 4: Memory-Efficient Aggregation
```bash
python3 4-stream_ages.py
```

## Key Features

- **Memory Efficiency**: All generators use minimal memory by processing one item at a time
- **Lazy Loading**: Data is fetched only when needed
- **Batch Processing**: Efficient handling of large datasets
- **Database Integration**: Seamless integration with MySQL database using environment variables
- **Security**: Database credentials managed through environment variables
- **Real-world Applications**: Practical implementations for data streaming scenarios
- **Easy Deployment**: Environment-based configuration for different deployment scenarios

## Environment Configuration

The project uses environment variables for secure database configuration:

- `DB_HOST`: Database host (default: localhost)
- `DB_USER`: Database username (default: root)
- `DB_PASSWORD`: Database password (required)
- `DB_NAME`: Database name (default: ALX_prodev)

## Security Notes

- Never commit your `.env` file to version control
- Use `.env.example` as a template for required environment variables
- The `.gitignore` file is configured to exclude sensitive files automatically
