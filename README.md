# FastAPI Todo App

This is a simple Todo list application built with FastAPI. It allows users to create, read, update, and delete todo items.

## Project Structure

```
fastapidemo
├── app
│   ├── crud.py          # CRUD operations for the database
│   ├── database.py      # Database connection and setup
│   ├── main.py          # Entry point of the application
│   ├── models.py        # Database models for todo items
│   ├── routes.py        # Routes for todo item CRUD operations
│   └── schemas.py       # Pydantic schemas for request and response validation
├── tests
│   └── test_main.py     # Test cases for the application
├── .env                 # Environment variables
├── pyproject.toml       # Poetry configuration file
├── README.md            # Project documentation
└── test.db              # SQLite database file (will be created if not present)
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd fastapidemo
   ```

2. Install Poetry:
   ```
   pip install poetry
   ```

3. Install the dependencies:
   ```
   poetry install
   ```

## Usage

1. Run the application:
   ```
   poetry run uvicorn app.main:app --reload
   ```

2. Access the API documentation at `http://127.0.0.1:8000/docs`.

## API Endpoints

- `GET /todos`: Retrieve all todo items.
- `POST /todos`: Create a new todo item.
- `GET /todos/{id}`: Retrieve a specific todo item by ID.

**Todo**:
   - `PUT /todos/{id}`: Update a specific todo item by ID.
   - `DELETE /todos/{id}`: Delete a specific todo item by ID.

## Running Tests

To run the tests, use the following command:
```
poetry run pytest tests/test_main.py
```

## License

This project is licensed under the MIT License.