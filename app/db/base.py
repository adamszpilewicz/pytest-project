from abc import ABC, abstractmethod


class BaseDatabase(ABC):

    @abstractmethod
    def create(self, table, data):
        """Insert new entry into the database.
        - table: String name of the table.
        - data: Dictionary of column names and their values to insert.
        """
        pass

    @abstractmethod
    def read(self, query, params=None):
        """Retrieve entries from the database.
        - query: SQL query string.
        - params: Optional parameters to substitute into the query.
        """
        pass

    @abstractmethod
    def update(self, query, params):
        """Update entries in the database.
        - query: SQL update query string.
        - params: Parameters to substitute into the query.
        """
        pass

    @abstractmethod
    def delete(self, query, params):
        """Delete entries from the database.
        - query: SQL delete query string.
        - params: Parameters to substitute into the query.
        """
        pass
