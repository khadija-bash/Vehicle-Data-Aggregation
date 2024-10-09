# FastAPI Electric Vehicle Data Aggregation API

This FastAPI project provides an API to retrieve aggregated electric vehicle (EV) data from the Washington State Department of Licensing. The API accepts a vehicle model year and returns the number of vehicles and the average electric range for vehicles grouped by vehicle make.

## Features

- Fetches data from an external API.
- Aggregates vehicle data by make for a specific model year.
- Returns the total number of vehicles and the average electric range for each make.


## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-repo-url

2. Navigate to the project directory:
   `cd project-root`

3. Set up a virtual environment
   `python -m venv venv`
   `source venv/bin/activate`  # On Windows: venv\Scripts\activate

4. Install the dependencies
   pip install -r requirements.txt

## Running the Application

1. Start the application using `uvicorn app.main:app --reload`
2. Open browser and open this URL: `http://127.0.0.1:8000/ev-data/{model_year}`


## To Run Tests

1. Run the command `pytest`
