
# 🧾 1. File Structures (What We’re Mapping)

**When you upload CSV records to Cointracker, they expect you to use their formatting**

### ✅ Binance CSV (source)

- [Cointracker CSV Template & Write-up](https://support.cointracker.io/hc/en-us/articles/4413071299729-Convert-your-transaction-history-to-CoinTracker-CSV)

- You have fields like:

* `Time`
* `Category` (Buy, Spot Trading, Withdrawal, etc.)
* `Base Asset`, `Quote Asset`, `Primary Asset`
* Realized amounts per asset
* Fee asset + amount

👉 This is **rich but messy / multi-field**

---

### ✅ CoinTracker Template (target)

Clean, normalized schema:

| Field             | Meaning                      |
| ----------------- | ---------------------------- |
| Date              | Transaction time             |
| Received Quantity | What you got                 |
| Received Currency | Asset received               |
| Sent Quantity     | What you gave                |
| Sent Currency     | Asset sent                   |
| Fee Amount        | Fee                          |
| Fee Currency      | Fee asset                    |
| Tag               | Type (trade, transfer, etc.) |

👉 This is **strict and normalized**

---

# 🔄 2. Mapping Logic (Critical)

Here’s how its converted Binance → CoinTracker:

## 🟢 Trades (Buy / Spot Trading)

* You **receive** base asset
* You **send** quote asset

Example:

* Buy BTC with USDT:

  * Received: BTC
  * Sent: USDT

---

## 🔴 Withdrawals

* You only **send** asset

---

## 🟡 Deposits

* You only **receive** asset

---

## 💸 Fees

* Taken from:

  * `Fee Asset`
  * `Realized Amount for Fee Asset`

---

# 📤 3. Sample Output (Ready for CoinTracker)

Here’s what your transformed data looks like:

| Date                | Received Qty | Received Curr | Sent Qty    | Sent Curr     | Fee | Fee Curr | Tag          |
| ------------------- | ------------ | ------------- | ----------- | ------------- | --- | -------- | ------------ |
| 2023-03-14 20:38:09 | 43.0         | (Base Asset)  | (Quote Amt) | (Quote Asset) | fee | USD      | Spot Trading |
| 2023-03-14 20:39:12 | 80.34        | (Base Asset)  | (Quote Amt) | (Quote Asset) | fee | USD      | Buy          |
| 2023-04-14 01:12:01 | —            | —             | amount      | KDA           | fee | KDA      | Withdrawal   |

👉 This format is **directly uploadable to CoinTracker**

---

# ⚙️ 4. Full Conversion Script

- [Run this yourself for full control](convert-template.py)
- Install full Python tooling in W11 WSL (Ubuntu):

```bash
sudo apt update
sudo apt install python3-full python3-venv python3-pip -y
#delete broken venv if necessary
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install pandas
#verify
which python
which pip
#run the script
python3 convert-template.py
```

---

# ⚠️ 5. Important Fixes You MUST Review

This is where accuracy lives:

## 🔁 Transfers (CRITICAL)

Binance withdrawal → Coinbase deposit

If not matched:

* ❌ Looks like a sale (taxable)
* ❌ Then a buy (double counting)

👉 Fix inside CoinTracker:

* “Review → Link transfers”

---

## 💱 Spot Trading Ambiguity

“Spot Trading” sometimes:

* Uses `Primary Asset` instead of Base/Quote cleanly

👉 You may need edge-case handling

---

## 🧾 Fees in Different Tokens

* Binance sometimes charges fees in:

  * BNB
  * Same asset traded

👉 Already captured, but verify

---

## 🕒 Timestamp Consistency

* Ensure:

  * UTC vs local time alignment

---

# 🧩 6. Bottom Line

You now have:

✅ A working transformation model
✅ A script to automate
✅ A CoinTracker-compatible output

---

## 💡 Recommendation 

* Run this script locally
* Validate edge cases manually
* Then upload to CoinTracker

---
