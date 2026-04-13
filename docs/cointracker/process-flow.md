

## Overview

This guide documents a **reliable, audit-safe workflow** for handling crypto taxes when using:

- Coinbase (primary exchange)
- Ledger (self-custody wallet)
- CoinTracker (aggregation + tax engine)
- TurboTax (filing)

It also covers:
- Wallet reconciliation
- CSV imports (Binance, KuCoin, etc.)
- Avoiding common tax errors

---

# 🧠 Core Principle

> Crypto tax accuracy depends on **complete transaction chains**, not just trades.

You must capture:
- Trades (Coinbase API)
- Transfers (Ledger + other wallets)
- Historical cost basis (manual or CSV)

---

# 🔄 Flow: Coinbase → Ledger → Coinbase

## Example Lifecycle

```

Buy BTC on Coinbase
→ Send BTC to Ledger
→ Send BTC back to Coinbase
→ Sell BTC on Coinbase

```

---

## Correct Tax Interpretation

| Step | Tax Treatment |
|------|-------------|
| Buy | Cost basis established |
| Send to Ledger | Transfer (non-taxable) |
| Send back | Transfer (non-taxable) |
| Sell | Taxable event |

👉 Only the **final sale** should be taxed.

---

## ❌ What Happens If Ledger Is Missing

CoinTracker sees:

```

Coinbase withdrawal → ❌ interpreted as sale
Coinbase sale → ❌ second sale

```

Result:
- Double counting
- Inflated gains
- Incorrect taxes

---

## ✅ Correct Setup

You must include:

### 1. Coinbase API
- Sync all trades
- Automatically pulls buys/sells

---

### 2. Ledger Wallet Addresses

Add ALL relevant addresses:
- BTC
- ETH
- SOL
- Any other chains used

👉 These are added as **wallets**, not exchanges.

---

# 🔍 Finding Your Ledger Addresses

## Best Method (Recommended)

From Coinbase:

1. Go to a **Send transaction**
2. Copy:
```

"To address"

```

👉 This is your Ledger receive address.

---

## Avoid This

- ❌ Do NOT use mempool INPUT addresses
- ❌ Do NOT use Coinbase hot wallets
- ❌ Do NOT guess addresses

---

## Important: Multiple Addresses

Ledger uses HD wallets:

- New address per receive
- You may have multiple addresses

### Minimum
- Add at least 1 address

### Best Practice
- Add all addresses used in transfers

---

# 🔁 Transfer Matching in CoinTracker

After adding wallets:

CoinTracker should automatically match:

```

Withdrawal (Coinbase)
↓
Deposit (Ledger)

```

→ becomes:

```

Transfer (non-taxable)

```

---

## Verification

Go to:
```

Transactions → Review

```

Look for:
- ❌ Unmatched withdrawals
- ❌ Unmatched deposits

Fix until:
- All transfers are paired

---

# 📊 Coinbase API Setup

## Steps

1. Connect Coinbase account via API
2. Sync transactions
3. Verify:
   - Buys
   - Sells
   - Fees

---

## What API Covers

| Data Type | Covered |
|----------|--------|
| Trades | ✅ |
| Fees | ✅ |
| Transfers | Partial |

👉 Wallet data still required separately.

---

# 📂 CSV Uploads (Binance, KuCoin, etc.)

## When Needed

Use CSV if:
- Exchange API unavailable
- Historical data needed
- Exchange no longer exists

---

## CoinTracker CSV Format

Required columns:

```

Date
Received Quantity
Received Currency
Sent Quantity
Sent Currency
Fee Amount
Fee Currency
Tag

```

---

## Example (Buy)

```

01/01/2022 12:00:00,0.1,BTC,3000,USD,,

```

---

## Example (Sell)

```

02/01/2022 12:00:00,4000,USD,0.1,BTC,,

```

---

## Example (Transfer)

```

03/01/2022 12:00:00,, ,0.1,BTC,,

```

---

# ⚠️ CSV Rules

- No NaN values
- Blank fields = empty string
- Fees must have BOTH:
  - amount
  - currency
- Dates must be consistent format

---

# 🔄 Binance / KuCoin Notes

## Binance
- Mixed schema (market + ledger)
- Requires custom transformation logic

## KuCoin
- Two types:
  - Trade history → buy/sell logic
  - Ledger history → deposit/withdrawal logic

---

# 🧠 Key Mapping Logic

| Action | Received | Sent |
|--------|--------|------|
| Buy | Base | Quote |
| Sell | Quote | Base |
| Deposit | Asset | — |
| Withdrawal | — | Asset |

---

# 🧾 TurboTax Integration

## DO NOT Use
- 1099-DA import ❌
- Digital Assets option ❌

---

## Use Instead

```

Stocks, Bonds, Mutual Funds → Summary entry

```

---

## Enter

From CoinTracker:

| Category | Input |
|----------|------|
| Short-term proceeds | ✔ |
| Short-term cost basis | ✔ |
| Long-term proceeds | ✔ |
| Long-term cost basis | ✔ |

---

## Sales Section Type

Use:

```

Non-covered (NOT reported to IRS)

```

---

## Attach

Upload:
```

Form 8949 (from CoinTracker)

```

---

# ⚠️ Common Mistakes

| Mistake | Impact |
|--------|--------|
| Missing Ledger wallet | Fake gains |
| Using wrong BTC address | Massive data errors |
| Duplicate CSV + API | Double counting |
| Missing cost basis | Overpay taxes |
| Using 1099-DA import | Broken return |

---

# 🧩 Final Checklist

Before filing:

- [ ] Coinbase API synced
- [ ] Ledger addresses added
- [ ] Transfers matched
- [ ] No unmatched withdrawals
- [ ] CSV imports validated
- [ ] No duplicate transactions
- [ ] Summary matches CoinTracker totals
- [ ] 8949 attached in TurboTax

---

# 💡 Final Insight

> Accuracy comes from **complete visibility of asset movement**, not just trades.

---

# 🚀 Optional Enhancements

- Add all wallets across chains
- Use HIFO vs FIFO optimization
- Generate reconciliation reports
- Audit for missing cost basis

---

# ✅ Outcome

If done correctly:

- Accurate gains/losses
- No double counting
- Audit-ready documentation
- Clean TurboTax filing

---
