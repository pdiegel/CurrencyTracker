import sqlite3
from constants import (
    DATABASE_PATH,
    DATABASE_TABLE,
    DATABASE_CREATION_QUERY,
)


class Database:
    """This class is used to interact with the SQLite database."""

    def __init__(self, database_path: str) -> None:
        self.database_path = database_path
        self.connection = sqlite3.connect(self.database_path)
        self.cursor = self.connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.connection.close()

    def execute(self, query: str, data: tuple = None) -> None:
        """Execute a query."""
        try:
            if data is None:
                self.cursor.execute(query)
            else:
                self.cursor.execute(query, data)
            self.connection.commit()
        except sqlite3.OperationalError as e:
            print(
                f"An error occurred: {e}\nWhile executing: {query}\n\
With data: {data}"
            )
            raise

    def execute_many(self, query: str, data: list) -> None:
        """Execute a list of queries."""
        try:
            self.cursor.executemany(query, data)
            self.connection.commit()
        except sqlite3.OperationalError as e:
            print(
                f"An error occurred: {e}\nWhile executing: {query}\n\
With data: {data}"
            )
            raise

    def fetch(self, number: int = None) -> tuple:
        """Fetches the next row or rows of a query result set."""
        return (
            self.cursor.fetchmany(number) if number else self.cursor.fetchall()
        )


if __name__ == "__main__":
    with Database(DATABASE_PATH) as database:
        database.execute(DATABASE_CREATION_QUERY)
        database.execute(f"SELECT * FROM {DATABASE_TABLE}")
        print(database.fetch())
