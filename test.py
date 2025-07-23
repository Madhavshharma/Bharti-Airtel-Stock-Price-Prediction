import sqlite3

# Connect to the database
conn = sqlite3.connect('predictions.db')
c = conn.cursor()

# Fetch all rows from the table
c.execute("SELECT * FROM stock_predictions")
rows = c.fetchall()

# Print each row
for row in rows:
    print(row)

conn.close()
