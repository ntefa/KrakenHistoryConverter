from datetime import datetime

def format_datetime(datetime_str):
    formats = ['%Y-%m-%d %H:%M:%S.%f', '%Y-%m-%d %H:%M:%S']
    
    for fmt in formats:
        try:
            datetime_obj = datetime.strptime(datetime_str, fmt)
            return datetime_obj.strftime('%Y-%m-%d %H:%M:%S')
        except ValueError:
            continue
    
    # If no format matches, raise an error
    raise ValueError("Invalid datetime format: " + datetime_str)

def parse_currency_pair(pair):
    # Split the currency pair into received and sent currencies
    received_currency = pair[:-3]
    sent_currency = pair[-3:]
    return received_currency, sent_currency

def parse_currency_staking(asset):
    # Remove the last two characters to get the currency
    currency = asset[:-2]
    return currency