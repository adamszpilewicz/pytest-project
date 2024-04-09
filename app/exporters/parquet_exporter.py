import pyarrow as pa
import pyarrow.parquet as pq
from typing import List, Dict
import pandas as pd

NO_DATA_MESSAGE = "No data to save."


class ParquetExporter:
    def __init__(self, db):
        self.db = db

    def fetch_data(self, query: str) -> List[Dict]:
        """Fetch data from the database using the provided SQL query."""
        return self.db.read(query)

    @staticmethod
    def save_to_parquet(data: List[Dict], filename: str):
        """Save fetched data to a Parquet file."""
        if not data:
            print(NO_DATA_MESSAGE)
            return

        # Konwertuje dane do formatu, który może być zapisany jako Parquet
        table = pa.Table.from_pandas(pd.DataFrame(data))

        # Zapisuje dane do pliku Parquet
        pq.write_table(table, filename)
        print(f"Data successfully saved to {filename}.")

    @staticmethod
    def save_to_parquet_error_no_data(data: List[Dict], filename: str):
        """
        Save fetched data to a Parquet file.
        Raise a ValueError if no data is provided.
        """
        if not data:
            raise ValueError(NO_DATA_MESSAGE)

        table = pa.Table.from_pandas(pd.DataFrame(data))
        pq.write_table(table, filename)
        print(f"Data successfully saved to {filename}.")
