# api.py
from flask import Flask, jsonify
import pandas as pd
import sqlite3

app = Flask(__name__)

@app.route('/read/first-chunck', methods=['GET'])
def get_data():
    conn = sqlite3.connect('database.db')
    df = pd.read_sql_query("SELECT * from data LIMIT 10", conn)
    conn.close()
    return jsonify(df.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
