# Currency Exchange Rates Tracker

This Python application fetches currency exchange rates data from a public API, formats it, and stores it into an SQLite database. The main aim of this project is to periodically capture the exchange rates data for further analysis. It is built using good programming practices, includes comprehensive error handling, logging, and securely handles sensitive information.

## Key Features

- Fetches real-world data from an exchangerate-api
- Stores the fetched data in an SQLite database
- Incorporates error handling and logging to make debugging easier
- Secures sensitive information (API key) by storing it in environment variables
- Configured to run daily to gather currency exchange rates periodically

## Technologies

- Python 3
- SQLite3 for database
- requests library for API calls
- logging for logging information
- os and dotenv for handling environment variables

## How to run

1. Clone the repository to your local machine.
2. Install the required Python packages found in the `requirements.txt` file.
```pip install -r requirements.txt```
3. Add a `.env` file at the root of the project. You should include your API key for the ExchangeRate-API service in this file like so:
```API_KEY=your_api_key_here```
4. Run the `main.py` module to execute the program. You can also set it up to run automatically on your system using task schedulers.

## Future Improvements

1. Implement unit tests to ensure each part of the script functions as expected.
2. Expand the range of data gathered from the API to include additional exchange rate information.
3. Implement data analysis functions to extract useful insights from the stored data.

## Note

Remember, to run this application you will need to register on [ExchangeRate-API](https://www.exchangerate-api.com/) website and get your own API key. The free plan offers limited requests per month. If you want to perform more requests, consider upgrading your plan.

## Contributions

Contributions, issues, and feature requests are welcome. Feel free to check issues page if you want to contribute.

## Author

Philip Diegel

- Github: @[https://github.com/pdiegel]
- LinkedIn: @[https://www.linkedin.com/in/philip-diegel-2b1a45245/]

## Show your support

Give a ⭐️ if you like this project!
