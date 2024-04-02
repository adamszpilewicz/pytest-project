import psycopg2
import psycopg2.extras
from .base import BaseDatabase
from utils.db_utils import generate_insert_query


class PostgreSQL(BaseDatabase):

    def __init__(self, dsn: str) -> None:
        self.conn = psycopg2.connect(dsn)
        self.conn.autocommit = True

    def create(self, table, data):
        query, values = generate_insert_query(table, data)  # Unpack the returned query and values
        with self.conn.cursor() as cursor:
            cursor.execute(query, values)  # Use values directly
            self.conn.commit()

    def read(self, query, params=None):
        with self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            cursor.execute(query, params or ())
            return cursor.fetchall()

    def update(self, query, params):
        with self.conn.cursor() as cursor:
            cursor.execute(query, params)

    def delete(self, query, params):
        with self.conn.cursor() as cursor:
            cursor.execute(query, params)
