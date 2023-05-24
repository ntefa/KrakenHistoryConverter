# Kraken History Converter

The Kraken History Converter is a Python script that converts transaction history data from Kraken cryptocurrency exchange into a customized CSV format. It handles two different types of input CSV files and performs the necessary data transformations to generate an output CSV file with the desired format.

## Features

- Converts transaction history data from Kraken into a custom CSV format
- Handles two types of input CSV files with different column structures
- Parses datetime strings in various formats
- Extracts specific columns and applies data transformations
- Generates an output CSV file with the transformed data

## Requirements

- Python 3.x

## Usage

1. Clone the repository:

   git clone https://github.com/ntefa/KrakenHistoryConverter.git
2. Install the required dependencies:
    
    pip install -r requirements.txt
3. Modify the config.py file:
    Update the input_file1 and input_file2 variables with the paths to your input CSV files.
4.  Prepare your input CSV files:
    For the first type of input CSV file, ensure that it follows the format described in the example CSV.
    For the second type of input CSV file, ensure that it follows the format described in the example CSV.
5. Run the script:

    python main.py

6. The script will generate an output CSV file named output.csv containing the converted data.

## Customization

If you need to customize the data transformation logic or modify the CSV output format, you can make changes to the relevant functions in csv_handling.py.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

Please note that this is the markdown version of the text, which is meant to b