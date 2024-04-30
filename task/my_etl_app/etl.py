# etl.py
import pandas as pd
import sqlite3

def etl_pipeline(csv_files):
    conn = sqlite3.connect('database.db')
    for file in csv_files:
        df = pd.read_csv(file)
        df.to_sql('data', conn, if_exists='append', index=False)
    conn.close()
