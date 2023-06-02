import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd

from constants import DATABASE_PATH, DATABASE_TABLE
from helpers.database import Database


def main():
    # Connect to the SQLite database
    database = Database(DATABASE_PATH)

    # Query to fetch data
    query = f"SELECT date, exchange_rate FROM {DATABASE_TABLE} WHERE\
 base_currency = 'USD' AND target_currency = 'EUR'"

    # Read the SQL query into a DataFrame
    df = pd.read_sql_query(query, database.connection)

    # Ensure 'date' is a datetime type
    df["date"] = pd.to_datetime(df["date"], format="%a, %d %b %Y %H:%M:%S %z")
    df["date"] = pd.to_datetime(df["date"])
    df["date"] = df["date"].dt.tz_localize(None)

    # Sort the DataFrame by date
    df.sort_values("date", inplace=True)

    # Calculate daily returns
    df["returns"] = df["exchange_rate"].pct_change()

    # Calculate volatility
    df["volatility"] = df["returns"].rolling(window=2).std()

    # Plot the volatility
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot_date(df["date"], df["volatility"], linestyle="-", marker="")

    # Format the x-axis dates
    ax.xaxis.set_major_locator(mdates.AutoDateLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))

    ax.set_title("Volatility of USD/EUR")
    ax.set_xlabel("Date")
    ax.set_ylabel("Volatility")

    # Rotate and align the x labels
    fig.autofmt_xdate()

    print(df)

    plt.show()


if __name__ == "__main__":
    main()
