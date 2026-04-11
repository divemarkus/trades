import pandas as pd
import numpy as np

# Load CSV
binance = pd.read_csv("Scrubbed-Binance-202604080739.csv", dtype=str)
binance = binance.fillna('')


# =========================
# Helpers
# =========================
def to_str(x):
    return str(x).strip() if x not in [None, '', np.nan] else ''


def to_number(x):
    try:
        if x in [None, '', np.nan]:
            return ''
        v = float(x)
        if np.isfinite(v):
            return str(abs(v))
    except:
        pass
    return ''


def format_date(ts):
    try:
        dt = pd.to_datetime(ts, utc=True, errors='coerce')
        if pd.isna(dt):
            return ''
        return dt.strftime('%m/%d/%Y %H:%M:%S')
    except:
        return ''


# =========================
# Core Transform
# =========================
def transform(row):
    date = format_date(row.get('Time'))

    cat = to_str(row.get('Category')).lower()
    op = to_str(row.get('Operation')).lower()

    base_amt = row.get('Realized Amount For Base Asset')
    quote_amt = row.get('Realized Amount for Quote Asset')
    primary_amt = row.get('Realized Amount For Primary Asset')

    base_asset = to_str(row.get('Base Asset'))
    quote_asset = to_str(row.get('Quote Asset'))
    primary_asset = to_str(row.get('Primary Asset'))

    fee_amt = to_number(row.get('Realized Amount for Fee Asset'))
    fee_cur = to_str(row.get('Fee Asset'))

    received_qty = ''
    received_cur = ''
    sent_qty = ''
    sent_cur = ''

    # =========================
    # 1. Spot / Buy / Sell
    # =========================
    if cat in ['buy'] or (cat == 'spot trading' and op == 'buy'):
        received_qty = to_number(base_amt)
        received_cur = base_asset
        sent_qty = to_number(quote_amt)
        sent_cur = quote_asset

    elif cat in ['sell'] or (cat == 'spot trading' and op == 'sell'):
        received_qty = to_number(quote_amt)
        received_cur = quote_asset
        sent_qty = to_number(base_amt)
        sent_cur = base_asset

    # Fallback for missing operation
    elif cat == 'spot trading':
        try:
            b = float(base_amt or 0)
            if b > 0:
                received_qty = to_number(base_amt)
                received_cur = base_asset
                sent_qty = to_number(quote_amt)
                sent_cur = quote_asset
            else:
                received_qty = to_number(quote_amt)
                received_cur = quote_asset
                sent_qty = to_number(base_amt)
                sent_cur = base_asset
        except:
            pass

    # =========================
    # 2. Deposits / Withdrawals
    # =========================
    elif cat in ['deposit', 'crypto deposit', 'receive']:
        received_qty = to_number(primary_amt)
        received_cur = primary_asset

    elif cat in ['withdrawal', 'crypto withdrawal', 'send']:
        sent_qty = to_number(primary_amt)
        sent_cur = primary_asset

    # =========================
    # 3. Income / Rewards
    # =========================
    elif cat in [
        'staking', 'staking rewards', 'distribution',
        'airdrop', 'rewards', 'interest', 'mining'
    ]:
        received_qty = to_number(primary_amt)
        received_cur = primary_asset
        # Optional tagging:
        # tag = 'income'

    # =========================
    # 4. Fees-only rows
    # =========================
    elif cat in ['fee']:
        sent_qty = fee_amt
        sent_cur = fee_cur

    # =========================
    # 5. Fallback (VERY IMPORTANT)
    # =========================
    if not received_qty and not sent_qty:
        # Try salvage from primary asset
        if primary_amt not in ['', None]:
            val = float(primary_amt)
            if val > 0:
                received_qty = to_number(primary_amt)
                received_cur = primary_asset
            else:
                sent_qty = to_number(primary_amt)
                sent_cur = primary_asset

    tag = ''  # keep blank per CoinTracker spec

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
# Apply transform
# =========================
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

# Final cleanup
out = out.fillna('')

# =========================
# Validation (CRITICAL)
# =========================
bad_rows = out[
    (out["Received Quantity"] == '') &
    (out["Sent Quantity"] == '')
]

print(f"⚠️ Rows with no value detected: {len(bad_rows)}")

if len(bad_rows) > 0:
    bad_rows.to_csv("cointracker_bad_rows.csv", index=False)
    print("⚠️ Exported problematic rows → cointracker_bad_rows.csv")

# =========================
# Export
# =========================
out.to_csv("cointracker_ready.csv", index=False)

print("✅ Conversion complete: cointracker_ready.csv")