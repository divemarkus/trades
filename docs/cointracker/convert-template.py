import pandas as pd

binance = pd.read_csv("Scrubbed-Binance-202604080739.csv")

def transform(row):
    date = row['Time']
    fee_amt = abs(row.get('Realized Amount for Fee Asset', 0)) if pd.notna(row.get('Realized Amount for Fee Asset', 0)) else ''
    fee_cur = row.get('Fee Asset','')
    
    cat = row['Category']
    
    received_qty = ''
    received_cur = ''
    sent_qty = ''
    sent_cur = ''
    
    if cat in ['Buy','Spot Trading']:
        received_qty = row.get('Realized Amount For Base Asset','')
        received_cur = row.get('Base Asset','')
        sent_qty = abs(row.get('Realized Amount for Quote Asset',''))
        sent_cur = row.get('Quote Asset','')
        
    elif cat == 'Withdrawal':
        sent_qty = abs(row.get('Realized Amount For Primary Asset',''))
        sent_cur = row.get('Primary Asset','')
        
    elif cat == 'Deposit':
        received_qty = row.get('Realized Amount For Primary Asset','')
        received_cur = row.get('Primary Asset','')
    
    return pd.Series([
        date, received_qty, received_cur,
        sent_qty, sent_cur,
        fee_amt, fee_cur, cat
    ])

out = binance.apply(transform, axis=1)

out.columns = [
    "Date",
    "Received Quantity",
    "Received Currency",
    "Sent Quantity",
    "Sent Currency",
    "Fee Amount",
    "Fee Currency",
    "Tag"
]

out.to_csv("cointracker_ready.csv", index=False)
