import mysql.connector
from .base import BaseDatabase
from utils.db_utils import generate_insert_query


class MySQLDatabase(BaseDatabase):

    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def create(self, table, data):
        query, values = generate_insert_query(table, data)  # Unpack returned tuple into query and values
        self.cursor.execute(query, tuple(values))  # Ensure values are passed as a tuple
        self.connection.commit()

    def read(self, query, params=None):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def update(self, query, params):
        self.cursor.execute(query, params)
        self.connection.commit()

    def delete(self, query, params):
        self.cursor.execute(query, params)
        self.connection.commit()
