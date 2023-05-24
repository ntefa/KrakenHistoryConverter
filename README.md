# Kraken History Converter

The Kraken History Converter is a Python script that converts transaction history data from Kraken cryptocurrency exchange into a CSV format suited for OKIPO. OKIPO is a cryptocurrency investment and tax reports tracking app. More information can be found at https://okipo.io. 

This script handles the ledger and trades csvs from Kraken and performs the necessary data transformations to generate an output CSV file with the desired format.

## Features

- Converts transaction history data from Kraken into a OKIPO CSV format
- Handles two types of input CSV files with different column structures
- Parses datetime strings in various formats
- Extracts specific columns and applies data transformations
- Generates an output CSV file with the transformed data

## Requirements
```console
- Python 3.x
```
## Usage

1. Clone the repository:
   ```console
   git clone https://github.com/ntefa/KrakenHistoryConverter.git
   ```

2. Modify the config.py file:
    Update the input and output variables with the paths to your input and output CSV files.
3.  Prepare your input CSV files:
    The first one is the trades.csv;
    The second one is the ledger.csv.
    Both can be exported from Kraken UI
4. Run the script:
    ```console  
    python main.py
    ```
5. The script will generate an output CSV file named kraken_history.csv containing the converted data.

## Customization

If you need to customize the data transformation logic or modify the CSV output format, you can make changes to the relevant functions in csv_handling.py.

## License

This project is licensed under the MIT License. See the LICENSE file for details.