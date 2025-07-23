import sqlite3
from datetime import datetime

def create_table():
    conn = sqlite3.connect('predictions.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS stock_predictions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    open REAL,
                    high REAL,
                    low REAL,
                    volume REAL,
                    close_1 REAL,
                    spread REAL,
                    ret REAL,
                    sma5 REAL,
                    sma10 REAL,
                    predicted_price REAL,
                    timestamp TEXT
                )''')
    conn.commit()
    conn.close()

def insert_prediction(open, high, low, volume, close_1, spread, ret, sma5, sma10, predicted_price):
    conn = sqlite3.connect('predictions.db')
    c = conn.cursor()
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    c.execute('''INSERT INTO stock_predictions (open, high, low, volume, close_1, spread, ret, sma5, sma10, predicted_price, timestamp)
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
              (open, high, low, volume, close_1, spread, ret, sma5, sma10, predicted_price, timestamp))
    conn.commit()
    conn.close()
