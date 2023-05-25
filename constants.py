import os

# Root directory of the project
ROOT_DIR = os.path.abspath(os.path.dirname(__file__))

# Path to the directory containing the data
DATA_DIR = os.path.join(ROOT_DIR, "data")
DATABASE_PATH = os.path.join(DATA_DIR, "data.db")
DATABASE_TABLE = "ExchangeRates"

# Create the data directory if it doesn't exist
if not os.path.exists(DATA_DIR):
    os.mkdir(DATA_DIR)

# Database schema
DATABASE_SCHEMA = {
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
    "date": "DATE NOT NULL",
    "base_currency": "VARCHAR(10) NOT NULL",
    "target_currency": "VARCHAR(10) NOT NULL",
    "exchange_rate": "FLOAT NOT NULL",
}
