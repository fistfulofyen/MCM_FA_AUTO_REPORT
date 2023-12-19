# Student Data Analysis with Pandas

This repository contains a Python script that utilizes the Pandas library to analyze student data from a CSV file. The script performs various data manipulations and calculations to obtain statistics based on FA specific criteria.

## Getting Started

To use the script, follow these steps:

1. Clone the repository to your local machine.
2. Make sure you have Python and the Pandas library installed.
3. Replace the file path in the script (`data = pd.read_csv("path_to_your_data.csv")`) with the path to your own student data CSV file.
4. Uncomment and complete the academic program mapping section if applicable.
5. Run the script using a Python interpreter.

## Script Overview

The script performs the following tasks:

1. Loads student data from a CSV file.
2. Filters and removes duplicate rows based on evaluation numbers.
3. Attempts to map UHMML academic programs to faculty fields (incomplete).
4. Calculates statistics for each faculty:
   - Total number of matriculated students
   - Number of matriculated students, separated by domestic and international status
   - Number of eligible students based on specific criteria
   - Number of eligible students, separated by domestic and international status
   - Number of top 10% students based on specific criteria
   - Number of top 10% students, separated by domestic and international status
5. Displays the calculated statistics for each faculty.

## Requirements

- Python (3.x recommended)
- Pandas library (`pip install pandas`)

## License

This project is licensed under the MIT License

## Author
ME
