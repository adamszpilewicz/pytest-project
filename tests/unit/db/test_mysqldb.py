# tests/test_mysqldb.py
from db.mysqldb import MySQLDatabase
import pytest

# Przykładowe dane do testowania metody `create`
test_data = [
    ("users", {"username": "testuser1", "email": "test1@example.com"}),
    ("users", {"username": "testuser2", "email": "test2@example.com"}),
]


# Parametryzowana fixture dostarczająca dane do testów
@pytest.fixture(params=test_data, ids=lambda d: f"table={d[0]},username={d[1]['username']}", name="sd")
def sample_data(request):
    return request.param


def test_create_with_parametrized_data(mocker, sd):
    # Patch `connect` method
    mocker.patch('mysql.connector.connect', return_value=mocker.MagicMock())

    # Initialize the database with mock credentials
    db = MySQLDatabase(host="mock", user="mock", password="mock", database="mock")

    # Mock cursor and connection
    mocked_cursor = mocker.MagicMock()
    db.cursor = mocked_cursor
    db.connection = mocker.MagicMock()

    # Extract table and data from the parametrized fixture
    table, data = sd

    # Generate the expected SQL query based on the method logic and test data
    # This needs to match how `db.create` method generates its query
    expected_query = f"INSERT INTO {table} ({', '.join(data.keys())}) VALUES ({', '.join(['%s'] * len(data))})"
    expected_args = tuple(data.values())

    # Execute the `create` method with parametrized data
    db.create(table, data)

    # Assert that cursor.execute() was called once with the expected query and arguments
    mocked_cursor.excute.assert_called_once_with(expected_query, expected_args)

    # Assert that connection.commit() was called
    db.connection.commit.assert_called_once()
