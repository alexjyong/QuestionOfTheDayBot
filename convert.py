import pandas as pd
import sqlite3

# Load the CSV data into a pandas DataFrame
df = pd.read_csv('tds.csv')

# Create a connection to the SQLite database
# (it will be created if it doesn't exist)
conn = sqlite3.connect('tds.db')

# Write the data to a new SQLite table
df.to_sql('tds', conn, if_exists='replace', index=False)

# Close the connection to the SQLite database
conn.close()