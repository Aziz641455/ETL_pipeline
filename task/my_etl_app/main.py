# main.py
import etl
import api

if __name__ == '__main__':
    etl.etl_pipeline(['file1.csv', 'file2.csv'])  # Add your CSV files here
    api.app.run(debug=True)
