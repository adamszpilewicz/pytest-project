import json
from typing import List, Dict

NO_DATA_MESSAGE = "No data to save."


class JSONExporter:
    def __init__(self, db):
        self.db = db

    def fetch_data(self, query: str) -> List[Dict]:
        """Fetch data from the database using the provided SQL query."""
        return self.db.read(query)

    @staticmethod
    def save_to_json(data: List[Dict], filename: str):
        """Save fetched data to a JSON file."""
        if not data:
            print(NO_DATA_MESSAGE)
            return

        with open(filename, 'w') as jsonfile:
            json.dump(data, jsonfile, indent=4)
        print(f"Data successfully saved to {filename}.")

    @staticmethod
    def save_to_json_error_no_data(data: List[Dict], filename: str):
        """
        Save fetched data to a JSON file.
        Raise a ValueError if no data is provided.
        """
        if not data:
            raise ValueError(NO_DATA_MESSAGE)

        with open(filename, 'w') as jsonfile:
            json.dump(data, jsonfile, indent=4)
        print(f"Data successfully saved to {filename}.")
