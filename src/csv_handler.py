import config
import csv
from src.utils import format_datetime, parse_currency_pair,parse_currency_staking

def initialize_csv():
    headers = ['Data', 'Importo Ricevuto', 'Valuta Ricevuta', 'Valuta Inviata', 'Importo Inviato', 'Commissione', 'Valuta Commissione']
    with open(config.OUTPUT_CSV, 'w', newline='') as output:
        writer = csv.writer(output)
        writer.writerow(headers)
        
def append_data(time, received_amount, received_currency, sent_currency, sent_amount, fee):
    data = [time, received_amount, received_currency, sent_currency, sent_amount, fee, 'EUR']
    with open(config.OUTPUT_CSV, 'a', newline='') as output:
        writer = csv.writer(output)
        writer.writerow(data)
        
def process_trades():
    with open(config.TRADES_CSV, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            time = format_datetime(row['time'])
            received_amount = row['vol']
            received_currency, sent_currency = parse_currency_pair(row["pair"])
            sent_amount = row['cost']
            fee = row['fee']
            append_data(time, received_amount, received_currency, sent_currency, sent_amount, fee)
            
            
def process_ledger():
    with open(config.LEDGER_CSV, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['type'] == 'staking':
                time = format_datetime(row['time'])
                received_amount = row['amount']
                received_currency = parse_currency_staking(row['asset'])
                sent_currency = 'EUR'
                sent_amount = '0'
                fee = '0'
                append_data(time, received_amount, received_currency, sent_currency, sent_amount, fee)