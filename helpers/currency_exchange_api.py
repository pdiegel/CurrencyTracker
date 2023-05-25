from typing import List, Tuple

import requests
from constants import API_KEY, API_URL


class CurrencyExchangeAPI:
    """This class is used to interact with the currency exchange API."""

    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    def fetch_daily_rates(self, base_currency: str) -> dict:
        """Get the exchange rates for the given base currency."""
        try:
            response = requests.get(
                self.base_url.format(
                    api_key=API_KEY,
                    base_currency=base_currency,
                )
            )
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            raise
        else:
            return response.json()

    def format_data(self, api_data: dict) -> List[Tuple[str, str, str, float]]:
        """Format the API exchange rate data."""

        if api_data.get("result") != "success":
            raise APIResponseError("API response was not successful", api_data)

        date = api_data.get("time_last_update_utc")
        base_currency = api_data.get("base_code")
        conversion_rates = api_data.get("conversion_rates")

        return [
            (date, base_currency, target_currency, exchange_rate)
            for target_currency, exchange_rate in conversion_rates.items()
            if target_currency != base_currency
        ]


class APIResponseError(Exception):
    """
    Exception raised when API response is not successful.

    Attributes:
        message (str): Explanation of the error.
        response (dict): The full API response.
    """

    def __init__(self, message, response):
        super().__init__(message)
        self.response = response


if __name__ == "__main__":
    api = CurrencyExchangeAPI(API_URL)
    api_data = api.fetch_daily_rates("USD")
    formatted_data = api.format_data(api_data)
    print(formatted_data)
