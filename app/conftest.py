# conftest.py is a file where you can define fixtures for your tests.
# Fixtures are functions, which will run before each test function to which they are passed.
import pytest


def mock_db(mocker):
    # Use mocker.patch to return a MagicMock object for db operations
    return mocker.patch('app.db.postgresdb.PostgreSQL')