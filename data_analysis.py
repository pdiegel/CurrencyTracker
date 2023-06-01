import pandas as pd
import matplotlib.pyplot as plt
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
    print(df["date"])
    df["date"] = pd.to_datetime(df["date"], format="%a, %d %b %Y %H:%M:%S %z")
    print(df["date"])

    # Sort the DataFrame by date
    df.sort_values("date", inplace=True)
    print(df)

    # Calculate daily returns
    df["returns"] = df["exchange_rate"].pct_change()

    # Calculate volatility
    df["volatility"] = df["returns"].rolling(window=21).std()

    # Plot the volatility
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df["date"], df["volatility"])
    ax.set_title("Volatility of USD/EUR")
    ax.set_xlabel("Date")
    ax.set_ylabel("Volatility")

    # Configure the date axis
    plt.xticks(rotation=45)  # rotate labels 45 degrees
    plt.show()


if __name__ == "__main__":
    main()
