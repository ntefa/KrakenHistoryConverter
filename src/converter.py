#TODO do the same for ledger but only staking

import csv
from datetime import datetime

input_file = '../input/trades.csv'
output_file = '../output.csv'

def format_datetime(datetime_str):
    # Format: AAAA-MM-GG hh:mm:ss
    datetime_obj = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S.%f')
    return datetime_obj.strftime('%Y-%m-%d %H:%M:%S')

def parse_currency_pair(pair):
    # Split the currency pair into received and sent currencies
    received_currency = pair[:-3]
    sent_currency = pair[-3:]
    return received_currency, sent_currency

with open(input_file, 'r') as file:
    reader = csv.DictReader(file)
    headers = ['Data', 'Importo Ricevuto', 'Valuta Ricevuta', 'Valuta Inviata', 'Importo Inviato', 'Commissione', 'Valuta Commissione']
    rows = []

    for row in reader:
        # Extract data from the row
        time = format_datetime(row['time'])
        vol = row['vol']
        received_currency, sent_currency = parse_currency_pair(row['pair'])
        cost = row['cost']
        fee = row['fee']

        # Create a new row with formatted data
        new_row = {
            'Data': time,
            'Importo Ricevuto': vol,
            'Valuta Ricevuta': received_currency,
            'Valuta Inviata': sent_currency,
            'Importo Inviato': cost,
            'Commissione': fee,
            'Valuta Commissione': 'EUR'
        }
        rows.append(new_row)

    with open(output_file, 'w', newline='') as output:
        writer = csv.DictWriter(output, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)

print("New CSV file created successfully!")
