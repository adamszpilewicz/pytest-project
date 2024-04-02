import pytest
import csv
import os
from app.exporters.csv_exporter import CSVExporter, NO_DATA_MESSAGE


@pytest.fixture
def sample_data():
    return [
        {"id": "1", "name": "Alice", "email": "alice@example.com"},
        {"id": "2", "name": "Bob", "email": "bob@example.com"}
    ]


def test_save_to_csv_with_valid_data(tmpdir, sample_data):
    # Generate a file path in the temporary directory
    file_path = tmpdir.join("test_output.csv")

    # Call the static method to save data to CSV
    CSVExporter.save_to_csv(sample_data, str(file_path))

    # Read back the CSV file to check its contents
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data_read = list(reader)

        # Assert that the data read from the CSV matches the original data
        assert len(data_read) == len(sample_data)
        for original, read_back in zip(sample_data, data_read):
            assert original == dict(read_back)


def test_save_to_csv_with_empty_data(tmpdir, capsys):
    file_path = tmpdir.join("empty_output.csv")

    CSVExporter.save_to_csv([], str(file_path))

    # Capture the printed output to verify the function's behavior
    captured = capsys.readouterr()
    assert NO_DATA_MESSAGE in captured.out

    # Ensure the file was not created
    assert not os.path.exists(file_path)


class MockDatabase:
    def __init__(self):
        self.data = [{"id": "1", "name": "Alice", "email": "alice@example.com"}]

    def read(self, query):
        # Simulate a 'SELECT *' query
        if "SELECT *" in query:
            return self.data
        return []


# Function-scope fixture for test data
@pytest.fixture(scope="function")
def func_scope_data():
    return [{"id": "2", "name": "Bob", "email": "bob@example.com"}]


# Module-scope fixture for database connection
# Adjusting the mod_scope_db fixture to session scope
@pytest.fixture(scope="session")
def mod_scope_db():
    db = MockDatabase()
    return db


# Session-scope fixture for CSVExporter
# Adjusting the sess_scope_exporter fixture to module scope, for example
@pytest.fixture(scope="module")
def sess_scope_exporter(mod_scope_db):
    exporter = CSVExporter(db=mod_scope_db)
    return exporter


def test_fetch_data_with_function_scope(func_scope_data, mod_scope_db):
    mod_scope_db.data = func_scope_data  # Update DB data with function-scoped fixture
    exporter = CSVExporter(db=mod_scope_db)
    data = exporter.fetch_data("SELECT *")
    assert data == func_scope_data


def test_save_to_csv_with_module_scope(tmpdir, mod_scope_db, sess_scope_exporter):
    # Use the module-scoped DB and session-scoped CSVExporter
    file_path = tmpdir.join("module_scope.csv")
    sess_scope_exporter.save_to_csv(mod_scope_db.data, str(file_path))
    with open(file_path, 'r') as f:
        content = f.read()
    assert "Alice" in content


def test_no_data_message_with_session_scope(capsys, sess_scope_exporter):
    sess_scope_exporter.save_to_csv([], "unused_filename.csv")
    captured = capsys.readouterr()
    assert NO_DATA_MESSAGE in captured.out
