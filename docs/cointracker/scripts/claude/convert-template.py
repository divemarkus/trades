import csv
from datetime import datetime

rows = []
with open('/mnt/user-data/uploads/Binance-Historical-2022.csv', 'r') as f:
    reader = csv.DictReader(f)
    for r in reader:
        # Strip \r from values
        r = {k.strip(): v.strip() for k, v in r.items()}
        
        # Reformat date: "2022-01-03 8:42:03" -> "01/03/2022 08:42:03"
        dt = datetime.strptime(r['Time'], '%Y-%m-%d %H:%M:%S')
        date = dt.strftime('%m/%d/%Y %H:%M:%S')
        
        cat = r['Category']
        recv_qty = recv_cur = sent_qty = sent_cur = fee_amt = fee_cur = tag = ''
        
        if cat == 'Spot Trading':
            # Sell: base asset sold, quote asset received
            sent_qty = r['Realized Amount For Base Asset']
            sent_cur = r['Base Asset']
            recv_qty = r['Realized Amount for Quote Asset']
            recv_cur = r['Quote Asset']
            fee_amt = r['Realized Amount for Fee Asset']
            fee_cur = r['Fee Asset']
        
        elif cat == 'Buy':
            # Buy: quote asset is what you get, base asset is what you spend
            sent_qty = r['Realized Amount For Base Asset']
            sent_cur = r['Base Asset']
            recv_qty = r['Realized Amount for Quote Asset']
            recv_cur = r['Quote Asset']
            fee_amt = r['Realized Amount for Fee Asset']
            fee_cur = r['Fee Asset']
        
        elif cat == 'Withdrawal':
            sent_qty = r['Realized Amount For Primary Asset']
            sent_cur = r['Primary Asset']
            fee_amt = r['Realized Amount for Fee Asset']
            fee_cur = r['Fee Asset']
        
        elif cat == 'Deposit':
            recv_qty = r['Realized Amount For Primary Asset']
            recv_cur = r['Primary Asset']
        
        elif cat == 'Distribution':
            recv_qty = r['Realized Amount For Primary Asset']
            recv_cur = r['Primary Asset']
            tag = 'staked'
        
        rows.append([date, recv_qty, recv_cur, sent_qty, sent_cur, fee_amt, fee_cur, tag])

# Sort by date
rows.sort(key=lambda x: datetime.strptime(x[0], '%m/%d/%Y %H:%M:%S'))

with open('/mnt/user-data/outputs/Binance-CoinTracker-2022.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Date','Received Quantity','Received Currency','Sent Quantity','Sent Currency','Fee Amount','Fee Currency','Tag'])
    w.writerows(rows)

print("Done. Rows:", len(rows))
