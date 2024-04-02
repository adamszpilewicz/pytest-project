import csv
from typing import List, Dict

NO_DATA_MESSAGE = "No data to save."


class CSVExporter:
    def __init__(self, db):
        self.db = db

    def fetch_data(self, query: str) -> List[Dict]:
        """Fetch data from the database using the provided SQL query."""
        return self.db.read(query)

    @staticmethod
    def save_to_csv(data: List[Dict], filename: str):
        """Save fetched data to a CSV file."""
        if not data:
            print(NO_DATA_MESSAGE)
            return

        keys = data[0].keys()
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)
        print(f"Data successfully saved to {filename}.")
