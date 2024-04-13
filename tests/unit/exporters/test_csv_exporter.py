import pytest
import csv
import os
from exporters.csv_exporter import CSVExporter, NO_DATA_MESSAGE


# @pytest.fixture
# def sample_data():
#     return [
#         {"id": "1", "name": "Alice", "email": "alice@example.com"},
#         {"id": "2", "name": "Bob", "email": "bob@example.com"}
#     ]


def test_save_to_csv_with_valid_data(tmpdir, sd):
    # Generate a file path in the temporary directory
    file_path = tmpdir.join("test_output.csv")

    # Call the static method to save data to CSV
    CSVExporter.save_to_csv(sd, str(file_path))

    # Read back the CSV file to check its contents
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data_read = list(reader)

        # Assert that the data read from the CSV matches the original data
        assert len(data_read) == len(sd)
        for original, read_back in zip(sd, data_read):
            assert original == dict(read_back)


def test_save_to_csv_with_empty_data(tmpdir, capsys):
    file_path = tmpdir.join("empty_output.csv")

    CSVExporter.save_to_csv([], str(file_path))

    # Capture the printed output to verify the function's behavior
    captured = capsys.readouterr()
    assert NO_DATA_MESSAGE in captured.out

    # Ensure the file was not created
    assert not os.path.exists(file_path)


def test_save_to_csv_error_no_data(tmpdir):
    file_path = tmpdir.join("empty_output.csv")

    with pytest.raises(ValueError) as exc_info:
        CSVExporter.save_to_csv_error_no_data([], str(file_path))

    # Ensure the error message is as expected
    assert NO_DATA_MESSAGE in str(exc_info.value)

    # Ensure the file was not created
    assert not os.path.exists(file_path)


class MockDatabase:
    def __init__(self, initial_data=None):
        if initial_data is None:
            initial_data = [
                {"id": "1", "name": "Alice", "email": "alice@example.com"},
                {"id": "2", "name": "Bob", "email": "bob@example.com"}
            ]
        self.data = initial_data

    def read(self, query):
        # Symulacja zapytania 'SELECT *'
        if "SELECT *" in query:
            return self.data
        return []


# Fixture z danymi testowymi o zasięgu funkcji
@pytest.fixture(scope="function")
def func_scope_data():
    return [{"id": "2", "name": "Bob", "email": "bob@example.com"}]


# Fixture dla CSVExporter o zasięgu modułu
@pytest.fixture(scope="module")
def module_scope_exporter(session_scope_db):
    print("Inicjalizacja CSVExporter o zasięgu modułu")
    exporter = CSVExporter(db=session_scope_db)
    return exporter


# Fixture z danymi do bazy danych o zasięgu sesji
@pytest.fixture(scope="session")
def session_scope_db():
    print("Inicjalizacja MockDatabase o zasięgu sesji")
    return MockDatabase()


def test_save_to_csv_with_module_scope(tmpdir, session_scope_db, module_scope_exporter):
    # Tutaj wykorzystujemy DB o zasięgu sesji i CSVExporter o zasięgu modułu
    file_path = tmpdir.join("module_scope.csv")
    module_scope_exporter.save_to_csv(session_scope_db.data, str(file_path))
    with open(file_path, 'r') as f:
        content = f.read()
    assert "Alice" in content and "Bob" in content


def test_fetch_data_with_function_scope(tmpdir, func_scope_data, session_scope_db):
    session_scope_db.data = func_scope_data  # Aktualizacja danych w DB
    file_path = tmpdir.join("func_scope_test.csv")
    exporter = CSVExporter(db=session_scope_db)
    exporter.save_to_csv(session_scope_db.data, str(file_path))
    with open(file_path, 'r') as f:
        content = f.read()
    assert "Bob" in content  # Upewniamy się, że dane funkcji zostały użyte


def test_no_data_message_with_session_scope(capsys, module_scope_exporter):
    module_scope_exporter.save_to_csv([], "unused_filename.csv")
    captured = capsys.readouterr()
    assert NO_DATA_MESSAGE in captured.out
