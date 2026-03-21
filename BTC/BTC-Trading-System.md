
# BTC Trading System
- Gmail + Google Sheet.
- 10 mins to 20 mins setup.

---

# ⚙️ STEP 0 — CREATE THE SHEET

1. Go to **Google Sheets**
2. Create new sheet → name it:
   **`BTC Trading System`**

---

# 🧱 STEP 1 — CORE INPUTS (TOP SECTION)

In **Row 1–5**, enter exactly:

| Cell | Label             | Value                               |
| ---- | ----------------- | ----------------------------------- |
| A1   | BTC Price         |                                     |
| B1   | *(formula below)* |                                     |
| A2   | Cycle High        | 70000 *(example — update manually)* |
| A3   | Capital ($)       | 10000 *(your deployable capital)*   |
| A4   | Avg Cost          | *(leave blank for now)*             |

---

## 🔗 Live BTC Price Formula

In **B1**, paste:

```excel
=GOOGLEFINANCE("CURRENCY:BTCUSD")
```

👉 If this fails (it sometimes does), use fallback:

```excel
=INDEX(IMPORTXML("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd","//body"),1,1)
```

---

# 📉 STEP 2 — BUY LADDER

Start at **Row 7**

| Cell | Label        | Formula |
| ---- | ------------ | ------- |
| A7   | Level        |         |
| B7   | Price        |         |
| C7   | Allocation % |         |
| D7   | Capital      |         |
| E7   | Trigger      |         |

---

### Fill rows:

#### L1 (-15%)

* A8: `L1 (-15%)`
* B8:

```excel
=$B$2*0.85
```

* C8: `15%`
* D8:

```excel
=$B$3*0.15
```

---

#### L2 (-25%)

* A9: `L2 (-25%)`
* B9:

```excel
=$B$2*0.75
```

* C9: `25%`
* D9:

```excel
=$B$3*0.25
```

---

#### L3 (-35%)

* A10: `L3 (-35%)`
* B10:

```excel
=$B$2*0.65
```

* C10: `30%`
* D10:

```excel
=$B$3*0.30
```

---

#### L4 (-45%)

* A11: `L4 (-45%)`
* B11:

```excel
=$B$2*0.55
```

* C11: `20%`
* D11:

```excel
=$B$3*0.20
```

---

#### L5 (-55%)

* A12: `L5 (-55%)`
* B12:

```excel
=$B$2*0.45
```

* C12: `10%`
* D12:

```excel
=$B$3*0.10
```

---

# 🚨 STEP 3 — AUTO TRIGGERS

In **E8**, paste:

```excel
=IF($B$1<=B8,"🔥 BUY","")
```

Drag down to **E12**

👉 Now the sheet **tells you when to act**

---

# 📈 STEP 4 — SELL LADDER

Start at **Row 15**

| Cell | Label      | Formula |
| ---- | ---------- | ------- |
| A15  | Sell Level |         |
| B15  | Price      |         |
| C15  | Action     |         |

---

### Fill:

#### S1 (+25%)

* A16: `S1 (+25%)`
* B16:

```excel
=$B$4*1.25
```

* C16: `Trim 15%`

---

#### S2 (+50%)

* A17: `S2 (+50%)`
* B17:

```excel
=$B$4*1.50
```

* C17: `Sell 25%`

---

#### S3 (+75%)

* A18: `S3 (+75%)`
* B18:

```excel
=$B$4*1.75
```

* C18: `Sell 25%`

---

#### S4 (+100%)

* A19: `S4 (+100%)`
* B19:

```excel
=$B$4*2.00
```

* C19: `Sell 25%`

---

# 🎨 STEP 5 — CONDITIONAL FORMATTING (IMPORTANT)

## Buy Signals:

1. Select **E8:E12**
2. Format → Conditional Formatting
3. Rule:

   * Text contains: `BUY`
4. Make it:

   * Green background
   * Bold

---

## Price Zones:

Highlight when price is near buy levels:

Formula:

```excel
=ABS($B$1-B8)/B8<0.03
```

👉 Shows when within 3% of level

---

# 🔔 STEP 6 — AUTOMATED ALERTS (APPS SCRIPT)

## Open Script:

* Extensions → Apps Script

---

## Paste THIS:

```javascript
function btcAlert() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  var price = sheet.getRange("B1").getValue();

  var levels = [
    {name: "L1", cell: "B8"},
    {name: "L2", cell: "B9"},
    {name: "L3", cell: "B10"},
    {name: "L4", cell: "B11"},
    {name: "L5", cell: "B12"},
  ];

  levels.forEach(level => {
    var lvl = sheet.getRange(level.cell).getValue();
    if (price <= lvl) {
      MailApp.sendEmail("YOUR_EMAIL@gmail.com",
        "BTC BUY ALERT: " + level.name,
        "BTC hit " + level.name + " at price: " + price);
    }
  });
}
```

---

## ⏱️ Set Trigger:

* Click **Triggers (clock icon)**
* Add Trigger:

  * Function: `btcAlert`
  * Event: Time-driven
  * Every 5 minutes

---

# 🔁 STEP 7 — SYSTEM RESET (IMPORTANT HABIT)

When BTC makes a **new major high**:

👉 Update:

* `B2 (Cycle High)`

Everything recalculates automatically.

---

# 🧠 HOW TO USE THIS DAILY

### You do NOT:

* Predict bottoms
* Watch charts all day

---

### You DO:

1. Check sheet
2. If “🔥 BUY” → execute
3. Update Avg Cost (B4) after buys
4. Sell based on ladder

---

# 🏁 FINAL RESULT

You now have:

✅ Live BTC price
✅ Auto-calculated buy zones
✅ Capital allocation
✅ Sell targets
✅ Real alerts
✅ Zero guesswork

---
