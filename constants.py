import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

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
DATABASE_COLUMNS = ", ".join(
    [key for key in DATABASE_SCHEMA.keys() if key != "id"]
)
DATABASE_CREATION_QUERY = f"CREATE TABLE IF NOT EXISTS {DATABASE_TABLE}\
 ({', '.join([f'{key} {value}' for key, value in DATABASE_SCHEMA.items()])})"

# Currency Exchange API URL and API key
API_URL = "https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}"
API_KEY = os.getenv("API_KEY")  # API key is stored in .env file

# Logging configuration
LOGGING_DIR = os.path.join(ROOT_DIR, "logs")
LOG_FILE_PATH = os.path.join(LOGGING_DIR, "currency_exchange.log")

# Create the logs directory if it doesn't exist
if not os.path.exists(LOGGING_DIR):
    os.mkdir(LOGGING_DIR)
