# Hawaii Climate Analysis

This repository contains Python code for analyzing climate data for Hawaii. This is Part 1 of the analysis.

## Overview

In this part of the analysis, we connect to a SQLite database containing climate data for Hawaii and perform various queries and visualizations to gain insights into the dataset.

## Requirements

To run the code, ensure you have the following libraries installed:

- #matplotlib
- #numpy
- #pandas
- #sqlalchemy

## Usage

1. Clone the repository to your local machine:

    ```
    git clone <repository_url>
    ```

2. Navigate to the cloned directory:

    ```
    cd sqlalchemy-challenge
    ```

3. Execute the Python script `climate_analysis_part1.py`:

    ```
    python climate_analysis_part1.py
    ```

## Contents

- **climate_analysis_part1.py**: Python script containing the code for Part 1 of the analysis.
- **Resources**: Directory containing the SQLite database (`hawaii.sqlite`) used in the analysis.

## Analysis Steps

1. Connect to the SQLite database containing climate data for Hawaii.
2. Retrieve the most recent date in the dataset.
3. Calculate the date one year prior to the most recent date.
4. Retrieve precipitation data for the last 12 months and plot the results.
5. Calculate summary statistics for the precipitation data.
6. Determine the total number of weather stations in the dataset.
7. Find the most active weather station.
8. Calculate the lowest, highest, and average temperature for the most active station.
9. Retrieve temperature observation data for the last 12 months for the most active station and plot the results as a histogram.

## Results

The analysis provides insights into the precipitation and temperature data for Hawaii, allowing for further investigation into the climate patterns of the region.

# Hawaii Climate Analysis Part 2

This repository contains Python code for analyzing climate data for Hawaii. This is Part 2 of the analysis, which includes setting up a Flask API to serve the climate analysis results.

## Overview

In this part of the analysis, we use Flask to create a RESTful API to serve the climate analysis results from Part 1.

## Requirements

To run the code, ensure you have the following libraries installed:

- #flask
- #sqlalchemy
- #datetime

## Usage

1. Clone the repository to your local machine:

    ```
    git clone <repository_url>
    ```

2. Navigate to the cloned directory:

    ```
    cd sqlalchemy-challenge
    ```

3. Execute the Python script `climate_app.py`:

    ```
    python climate_app.py
    ```

4. Once the Flask server is running, you can access the API endpoints using a web browser or a tool like Postman.

## Contents

- **climate_app.py**: Python script containing the Flask application code to set up the API endpoints.
- **Resources**: Directory containing the SQLite database (`hawaii.sqlite`) used in the analysis.

## API Endpoints

- **GET /api/v1.0/precipitation**: Returns the last 12 months of precipitation data as JSON.
- **GET /api/v1.0/stations**: Returns a list of weather stations from the dataset as JSON.
- **GET /api/v1.0/tobs**: Returns temperature observations for the previous year of data for the most active weather station as JSON.
- **GET /api/v1.0/&lt;start&gt;**: Returns the minimum, average, and maximum temperatures for all dates greater than or equal to the specified start date.
- **GET /api/v1.0/&lt;start&gt;/&lt;end&gt;**: Returns the minimum, average, and maximum temperatures for dates between the specified start and end dates (inclusive).

## Results

The Flask API allows users to easily access climate analysis results through various endpoints, providing flexibility in retrieving specific data based on user requirements.