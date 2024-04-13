import os

import pytest
import pandas as pd
from exporters.parquet_exporter import ParquetExporter, NO_DATA_MESSAGE


@pytest.fixture(scope="session")
def shared_temp_dir(tmpdir_factory):
    """Stworzenie wspólnego katalogu na poziomie sesji."""
    return tmpdir_factory.mktemp("shared_data")


@pytest.fixture
def sample_data():
    """Przykładowa fixture dostarczająca dane testowe."""
    return [
        {"id": "1", "name": "Alice", "email": "alice@example.com"},
        {"id": "2", "name": "Bob", "email": "bob@example.com"}
    ]


def test_save_to_parquet_with_valid_data(shared_temp_dir, sample_data):
    """Użycie wspólnego katalogu dla testu."""
    file_path = shared_temp_dir.join("test_output.parquet")
    ParquetExporter.save_to_parquet(sample_data, str(file_path))

    data_read = pd.read_parquet(file_path)
    assert len(data_read) == len(sample_data)
    for original, read_back in zip(sample_data, data_read.to_dict('records')):
        assert original == read_back


def test_access_shared_data(shared_temp_dir):
    """Dodatkowy test korzystający z tego samego katalogu."""
    file_path = shared_temp_dir.join("test_output.parquet")
    assert os.path.exists(file_path), "Plik powinien istnieć po poprzednich testach."


def test_save_to_parquet_with_empty_data(tmpdir, capsys):
    file_path = tmpdir.join("empty_output.parquet")

    ParquetExporter.save_to_parquet([], str(file_path))

    captured = capsys.readouterr()
    assert NO_DATA_MESSAGE in captured.out
    print("Przechwycony stdout:", captured.out)
    print("Przechwycony stderr:", captured.err)
    assert not os.path.exists(file_path)


def test_save_to_parquet_error_no_data(tmpdir):
    file_path = tmpdir.join("empty_output.parquet")

    with pytest.raises(ValueError) as exc_info:
        ParquetExporter.save_to_parquet_error_no_data([], str(file_path))

    assert NO_DATA_MESSAGE in str(exc_info.value)

    assert not os.path.exists(file_path)
