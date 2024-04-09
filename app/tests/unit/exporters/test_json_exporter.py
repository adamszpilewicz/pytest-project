import time

import pytest
import json
import os
from exporters.json_exporter import JSONExporter, NO_DATA_MESSAGE


def test_save_to_json_with_valid_data(tmpdir, sd):
    file_path = tmpdir.join("test_output.json")

    JSONExporter.save_to_json(sd, str(file_path))

    with open(file_path, 'r') as jsonfile:
        data_read = json.load(jsonfile)

        assert len(data_read) == len(sd)
        for original, read_back in zip(sd, data_read):
            assert original == read_back


def test_save_to_json_with_empty_data(tmpdir, capsys):
    file_path = tmpdir.join("empty_output.json")

    JSONExporter.save_to_json([], str(file_path))

    captured = capsys.readouterr()
    assert NO_DATA_MESSAGE in captured.out

    assert not os.path.exists(file_path)


def test_save_to_json_error_no_data(tmpdir):
    file_path = tmpdir.join("empty_output.json")

    with pytest.raises(ValueError) as exc_info:
        JSONExporter.save_to_json_error_no_data([], str(file_path))

    assert NO_DATA_MESSAGE in str(exc_info.value)

    assert not os.path.exists(file_path)


# -----------------------------------------------------------------------------------------
# ERROR: Zmienna sample_data_auto jest nazwą fixture, a w przypadku fixture z autouse=True,
# nie musisz (i nie możesz) jawnie przekazywać jej jako argument do funkcji testowej.
# @pytest.fixture(autouse=True)
# def sample_data_auto():
#     return [
#         {"id": "1", "name": "Alice", "email": "alice@example.com"},
#         {"id": "2", "name": "Bob", "email": "bob@example.com"}
#     ]
#
#
# def test_save_to_json_with_valid_data_autouse(tmpdir):
#     # Teraz nie musimy jawnie przekazywać 'sample_data' do funkcji testowej
#     file_path = tmpdir.join("test_output.json")
#     JSONExporter.save_to_json(sample_data_auto, str(file_path))
#
#     with open(file_path, 'r') as jsonfile:
#         data_read = json.load(jsonfile)
#
#         assert len(data_read) == len(sample_data_auto)
#         for original, read_back in zip(sample_data_auto, data_read):
#             assert original == read_back
# -----------------------------------------------------------------------------------------

# # Fixture automatycznie używana przed każdym testem w module
@pytest.fixture(autouse=True)
def log_test_timing():
    start_time = time.time()
    # Kod przed testem
    print("\nTest rozpoczyna się...")

    # yield zwraca sterowanie do testu, po którym kod poniżej zostanie wykonany jako "teardown"
    yield

    # Kod po teście
    end_time = time.time()
    print("Test zakończony. Czas trwania: {:.2f}s".format(end_time - start_time))