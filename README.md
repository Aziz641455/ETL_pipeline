# ETL_pipeline
This project is a simple ETL (Extract, Transform, Load) pipeline that ingests data from one or multiple CSV files into a SQLite database, and a REST API that exposes the recently ingested data.


## Setup

1. Install Docker on your machine.
2. Clone this repository to your local machine.
3. Navigate to the project directory in your terminal.
4. Build the Docker image with the command `docker build -t my-etl-app .`.
5. Run the Docker container with the command `docker run -p 5000:5000 my-etl-app`.

## Usage

Once the Docker container is running, you can connect to the API at `localhost:5000`. The endpoint `/read/first-chunck` returns the first 10 rows from the database in JSON format.

## Testing

Tests are located in the `test.py` file. You can run the tests with the command `pytest test.py`.
