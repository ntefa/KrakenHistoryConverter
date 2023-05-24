from src.csv_handler import initialize_csv, process_trades, process_ledger

def main():
    # Initialize the CSV with headers
    initialize_csv()

    # Process the first CSV file
    process_trades()

    # Process the second CSV file
    process_ledger()

    print("Data from both CSV files appended successfully!")

if __name__ == "__main__":
    main()
