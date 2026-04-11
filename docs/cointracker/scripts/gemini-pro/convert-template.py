import pandas as pd
import numpy as np

# Load the Binance CSV
input_file = "Scrubbed-Binance-202604080739.csv"
output_file = "cointracker_ready.csv"

binance = pd.read_csv(input_file, dtype=str)
binance = binance.fillna('')

# =========================
# Helpers
# =========================
def to_number(x):
    """Safely convert strings to positive floats, returning an empty string if invalid."""
    try:
        if pd.isna(x) or str(x).strip() == '':
            return ''
        v = float(x)
        if np.isfinite(v):
            return str(abs(v))
    except ValueError:
        pass
    return ''

def format_date(ts):
    """Convert Binance timestamp to CoinTracker format (MM/DD/YYYY HH:MM:SS)"""
    try:
        dt = pd.to_datetime(ts, utc=True, errors='coerce')
        if pd.isna(dt):
            return ''
        return dt.strftime('%m/%d/%Y %H:%M:%S')
    except Exception:
        return ''

# =========================
# Core Transform
# =========================
def transform(row):
    date = format_date(row.get('Time'))

    operation = str(row.get('Operation', '')).strip().lower()
    category = str(row.get('Category', '')).strip().lower()

    # Extract all possible asset and amount combinations
    base_asset = str(row.get('Base Asset', '')).strip()
    base_amt = to_number(row.get('Realized Amount For Base Asset'))
    
    quote_asset = str(row.get('Quote Asset', '')).strip()
    quote_amt = to_number(row.get('Realized Amount for Quote Asset'))
    
    primary_asset = str(row.get('Primary Asset', '')).strip()
    primary_amt = to_number(row.get('Realized Amount For Primary Asset'))

    # Extract Fees
    fee_amt = to_number(row.get('Realized Amount for Fee Asset'))
    fee_cur = str(row.get('Fee Asset', '')).strip()

    # Initialize CoinTracker columns
    received_qty = ''
    received_cur = ''
    sent_qty = ''
    sent_cur = ''
    tag = ''

    # 1. Handle Trades (Buy / Sell)
    if operation in ['buy', 'sell'] or category in ['spot trading', 'buy']:
        # In Binance.US exports, the asset disposed of is the Base Asset,
        # and the asset acquired is the Quote Asset, regardless of buy/sell designation.
        if base_asset and quote_asset:
            sent_qty = base_amt
            sent_cur = base_asset
            received_qty = quote_amt
            received_cur = quote_asset

    # 2. Handle Withdrawals
    elif 'withdrawal' in operation or 'withdrawal' in category:
        sent_qty = primary_amt
        sent_cur = primary_asset

    # 3. Handle Deposits
    elif 'deposit' in operation or 'deposit' in category:
        received_qty = primary_amt
        received_cur = primary_asset

    # 4. Handle Staking / Rewards (Optional mapping for CoinTracker)
    elif 'reward' in operation or 'staking' in category:
        received_qty = primary_amt
        received_cur = primary_asset
        tag = 'staked'

    return pd.Series([
        date,
        received_qty,
        received_cur,
        sent_qty,
        sent_cur,
        fee_amt,
        fee_cur,
        tag
    ])

# =========================
# Apply Transform & Export
# =========================
out = binance.apply(transform, axis=1)

# Apply CoinTracker exact header names
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

out = out.fillna('')

# Validation Check
bad_rows = out[(out["Received Quantity"] == '') & (out["Sent Quantity"] == '')]
if len(bad_rows) > 0:
    print(f"⚠️ Warning: {len(bad_rows)} rows have neither a sent nor received amount.")

out.to_csv(output_file, index=False)
print(f"✅ Conversion complete! Formatted file saved as '{output_file}'")