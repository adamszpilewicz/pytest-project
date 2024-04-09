# conftest.py is a file where you can define fixtures for your tests.
# Fixtures are functions, which will run before each test function to which they are passed.
import pytest


@pytest.fixture
def sd():
    return [
        {"id": "1", "name": "Alice", "email": "alice@example.com"},
        {"id": "2", "name": "Bob", "email": "bob@example.com"}
    ]