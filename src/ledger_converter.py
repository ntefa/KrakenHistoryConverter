import csv
from datetime import datetime
input_file = '../input/ledger.csv'
output_file = '../output/output.csv'

def format_datetime(datetime_str):
    # Format: AAAA-MM-GG hh:mm:ss
    datetime_obj = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
    return datetime_obj.strftime('%Y-%m-%d %H:%M:%S')

def parse_currency(asset):
    # Remove the last two characters to get the currency
    currency = asset[:-2]
    return currency

with open(input_file, 'r') as file:
    reader = csv.DictReader(file)
    headers = ['Data', 'Importo Ricevuto', 'Valuta Ricevuta', 'Valuta Inviata', 'Importo Inviato', 'Commissione', 'Valuta Commissione']
    rows = []

    for row in reader:
        # Check if the type is staking
        if row['type'] == 'staking':
            # Extract data from the row
            time = format_datetime(row['time'])
            received_amount = row['amount']
            received_currency = parse_currency(row['asset'])
            sent_amount = '0'
            sent_currency = 'EUR'
            fee = '0'

            # Create a new row with formatted data
            new_row = {
                'Data': time,
                'Importo Ricevuto': received_amount,
                'Valuta Ricevuta': received_currency,
                'Valuta Inviata': sent_currency,
                'Importo Inviato': sent_amount,
                'Commissione': fee,
                'Valuta Commissione': 'EUR'
            }
            rows.append(new_row)

    with open(output_file, 'a', newline='') as output:
        writer = csv.DictWriter(output, fieldnames=headers)
        writer.writerows(rows)

print("Data from the second CSV file appended successfully!")
