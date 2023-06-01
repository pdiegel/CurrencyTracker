import os
import unittest

from constants import DATABASE_SCHEMA, ROOT_DIR
from helpers.currency_exchange_api import CurrencyExchangeAPI
from helpers.database import Database

TEST_DIR = os.path.join(ROOT_DIR, "tests")
TEST_DATABASE_TABLE = "test_table"
TEST_DATABASE_CREATION_QUERY = f"""CREATE TABLE IF NOT EXISTS
 {TEST_DATABASE_TABLE} ({', '.join([f'{key} {value}' for key, value in
 DATABASE_SCHEMA.items()])})"""
TEST_DATABASE_PATH = os.path.join(TEST_DIR, "test.db")


class TestDatabase(unittest.TestCase):
    """Testing the Database class."""

    def setUp(self) -> None:
        """Setting up the test database."""
        self.database = Database(TEST_DATABASE_PATH)
        self.database.execute(TEST_DATABASE_CREATION_QUERY)

    def test_execute(self) -> None:
        """Testing the execute method.

        Schema:
            id: INTEGER PRIMARY KEY AUTOINCREMENT
            date: DATE NOT NULL
            base_currency: VARCHAR(10) NOT NULL
            target_currency: VARCHAR(10) NOT NULL
            exchange_rate: FLOAT NOT NULL

        """
        # Testing the execute method with no data.
        self.database.execute(
            f"INSERT INTO {TEST_DATABASE_TABLE}\
            (date, base_currency, target_currency, exchange_rate)\
            VALUES('2021-01-01', 'USD', 'EUR', 0.8)"
        )
        self.database.execute(f"SELECT * FROM {TEST_DATABASE_TABLE}")
        self.assertEqual(
            self.database.cursor.fetchone(),
            (1, "2021-01-01", "USD", "EUR", 0.8),
        )
        self.database.execute(
            f"INSERT INTO {TEST_DATABASE_TABLE}\
            (date, base_currency, target_currency, exchange_rate)\
            VALUES('2021-01-02', 'USD', 'EUR', 0.9)"
        )
        self.database.execute(f"SELECT * FROM {TEST_DATABASE_TABLE}")
        self.assertEqual(
            self.database.cursor.fetchall(),
            [
                (1, "2021-01-01", "USD", "EUR", 0.8),
                (2, "2021-01-02", "USD", "EUR", 0.9),
            ],
        )

        # Testing the execute method with data.
        self.database.execute(
            f"INSERT INTO {TEST_DATABASE_TABLE}\
            (date, base_currency, target_currency, exchange_rate)\
            VALUES('2021-01-03', 'USD', 'EUR', 0.7)"
        )
        self.database.execute(f"SELECT * FROM {TEST_DATABASE_TABLE}")
        self.assertEqual(
            self.database.cursor.fetchall(),
            [
                (1, "2021-01-01", "USD", "EUR", 0.8),
                (2, "2021-01-02", "USD", "EUR", 0.9),
                (3, "2021-01-03", "USD", "EUR", 0.7),
            ],
        )

        # Testing the execute method with an invalid query.
        with self.assertRaises(Exception):
            self.database.execute("SELECT * FROM invalid_table")

        # Deleting the test data.
        self.database.execute(f"DELETE FROM {TEST_DATABASE_TABLE} *")


if __name__ == "__main__":
    unittest.main()
