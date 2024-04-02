# tests/test_mysqldb.py
from app.db.mysqldb import MySQLDatabase


def test_create(mocker):
    # Patch the `connect` method to return a MagicMock object
    mocker.patch('mysql.connector.connect', return_value=mocker.MagicMock())

    # Now, when MySQLDatabase initializes, it uses the patched connect method
    db = MySQLDatabase(host="mock", user="mock", password="mock", database="mock")

    # Setup mock cursor and connection
    mocked_cursor = mocker.MagicMock()
    db.cursor = mocked_cursor
    db.connection = mocker.MagicMock()

    # Execute the method under test
    db.create("users", {"username": "testuser", "email": "test@example.com"})

    # Assert that cursor.execute() was called once
    mocked_cursor.execute.assert_called_once()
    # Assert that connection.commit() was called once
    db.connection.commit.assert_called_once()
