from constants import (
    API_URL,
    DATABASE_COLUMNS,
    DATABASE_CREATION_QUERY,
    DATABASE_PATH,
    DATABASE_TABLE,
    API_KEY,
)
from helpers.currency_exchange_api import CurrencyExchangeAPI
from helpers.database import Database
from helpers.logging import logger


def main():
    try:
        database = Database(DATABASE_PATH)
        database.execute(DATABASE_CREATION_QUERY)
    except Exception:
        logger.error(
            "An error occurred when attempting to interact with the database",
            exc_info=True,
        )
        return

    try:
        currency_exchange_api = CurrencyExchangeAPI(API_URL)
        currency_exchange_rates = currency_exchange_api.fetch_daily_rates(
            "USD", API_KEY
        )
        formatted_exchange_rates = currency_exchange_api.format_data(
            currency_exchange_rates
        )
    except Exception:
        logger.error(
            "An error occurred when attempting to fetch/format exchange rates",
            exc_info=True,
        )
        return

    try:
        database.execute_many(
            query=f"INSERT INTO {DATABASE_TABLE} ({DATABASE_COLUMNS})\
 VALUES(?, ?, ?, ?)",
            data=formatted_exchange_rates,
        )
        database.execute(f"SELECT * FROM {DATABASE_TABLE}")
    except Exception:
        logger.error(
            "An error occurred when attempting to insert data into the\
 database or fetch data",
            exc_info=True,
        )
        return


if __name__ == "__main__":
    main()
