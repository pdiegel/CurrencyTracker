import sqlite3
from Currency_API_Project.constants import (
    DATABASE_PATH,
    DATABASE_TABLE,
    DATABASE_SCHEMA,
)


class Database:
    """This class is used to interact with the SQLite database."""

    def __init__(self, database_path: str) -> None:
        self.database_path = database_path
        self.connection = sqlite3.connect(self.database_path)
        self.cursor = self.connection.cursor()

    def execute(self, query: str) -> None:
        """Execute a query."""
        self.cursor.execute(query)
        self.connection.commit()

    def create_table(self, table_name: str, data_schema: dict) -> None:
        """Create a table in the database."""
        columns = ", ".join(
            [f"{key} {value}" for key, value in data_schema.items()]
        )
        self.execute(f"CREATE TABLE {table_name}({columns})")


if __name__ == "__main__":
    database = Database(DATABASE_PATH)
    database.create_table(DATABASE_TABLE, DATABASE_SCHEMA)
