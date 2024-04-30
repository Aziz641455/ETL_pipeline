# test.py
import pytest
import pandas as pd
import sqlite3
import etl
import api
import json

def test_etl_pipeline():
    # Test that the ETL pipeline correctly loads a CSV file into the database
    etl.etl_pipeline(['test.csv'])
    conn = sqlite3.connect('database.db')
    df = pd.read_sql_query("SELECT * from data", conn)
    conn.close()
    assert not df.empty, "The database should not be empty after running the ETL pipeline"

def test_get_data(client):
    # Test that the API correctly returns the first 10 rows from the database
    response = client.get('/read/first-chunck')
    data = json.loads(response.data)
    assert response.status_code == 200, "The API should return a 200 status code"
    assert len(data) == 10, "The API should return 10 rows"

@pytest.fixture
def client():
    api.app.config['TESTING'] = True
    with api.app.test_client() as client:
        yield client
