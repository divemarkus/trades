
# 📊 BTC Trading System (Google Sheets + Alerts)

A **fully rule-based Bitcoin trading system** using:

* Volatility-based **buy ladder**
* Structured **sell distribution ladder**
* Real-time BTC pricing
* Automated **email alerts (no spam)**
* Minimal discretion required

---

# ⚙️ 1. Create the Sheet

1. Open **Google Sheets**
2. Create a new sheet
3. Name it:
   **`BTC Trading System`**

---

# 🧱 2. Core Inputs (Top Section)

| Cell | Label             | Value                               |
| ---- | ----------------- | ----------------------------------- |
| A1   | BTC Price         |                                     |
| B1   | *(formula below)* |                                     |
| A2   | Cycle High        | `70000` *(manual input)*            |
| A3   | Capital ($)       | `10000` *(your deployable capital)* |
| A4   | Avg Cost          | *(update after buys)*               |
| A5   | Sell Anchor       | *(formula below)*                   |

---

## 🔗 Live BTC Price

Paste into **B1**:

```excel
=GOOGLEFINANCE("CURRENCY:BTCUSD")
```

### Fallback (if needed):

```excel
=VALUE(REGEXEXTRACT(IMPORTDATA("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"),"\d+\.?\d*"))
```

---

## 📈 Sell Anchor (IMPORTANT)

In **B5**, choose ONE:

### Option A — Controlled (Recommended)

```excel
=B2
```

### Option B — Fully Dynamic

```excel
=MAX(B1,B2)
```

---

# 📉 3. Buy Ladder

Start at **Row 7**

| Cell | Label      |
| ---- | ---------- |
| A7   | Level      |
| B7   | Price      |
| C7   | Allocation |
| D7   | Capital    |
| E7   | Trigger    |

---

## Fill Rows:

### L1 (-15%)

```excel
B8 = $B$2*0.85
D8 = $B$3*0.15
E8 = IF($B$1<=B8,"🔥 BUY","")
```

### L2 (-25%)

```excel
B9 = $B$2*0.75
D9 = $B$3*0.25
E9 = IF($B$1<=B9,"🔥 BUY","")
```

### L3 (-35%)

```excel
B10 = $B$2*0.65
D10 = $B$3*0.30
E10 = IF($B$1<=B10,"🔥 BUY","")
```

### L4 (-45%)

```excel
B11 = $B$2*0.55
D11 = $B$3*0.20
E11 = IF($B$1<=B11,"🔥 BUY","")
```

### L5 (-55%)

```excel
B12 = $B$2*0.45
D12 = $B$3*0.10
E12 = IF($B$1<=B12,"🔥 BUY","")
```

---

# 📈 4. Sell Ladder

Start at **Row 15**

| Cell | Label      |
| ---- | ---------- |
| A15  | Level      |
| B15  | Price      |
| C15  | Allocation |
| D15  | Action     |
| E15  | Trigger    |

---

## Fill Rows:

### S1

```excel
B16 = $B$5*1.10
E16 = IF($B$1>=B16,"🚨 SELL","")
```

### S2

```excel
B17 = $B$5*1.20
E17 = IF($B$1>=B17,"🚨 SELL","")
```

### S3

```excel
B18 = $B$5*1.30
E18 = IF($B$1>=B18,"🚨 SELL","")
```

### S4

```excel
B19 = $B$5*1.50
E19 = IF($B$1>=B19,"🚨 SELL","")
```

### S5 (Blow-off)

```excel
B20 = $B$5*1.75
E20 = IF($B$1>=B20,"🚨 SELL","")
```

---

# 🎨 5. Conditional Formatting

## Buy Signals

* Range: `E8:E12`
* Rule: Text contains `"BUY"`
* Style: Green background, bold

---

## Sell Signals

* Range: `E16:E20`
* Rule: Text contains `"SELL"`
* Style: Red background, bold

---

## Price Proximity (Optional but Powerful)

Apply to Buy Prices:

```excel
=ABS($B$1-B8)/B8<0.03
```

👉 Highlights when price is within 3% of a level

---

# 🔔 6. Automated Alerts (Apps Script)

## Open Script Editor

* Extensions → Apps Script

---

## Paste THIS (final version — no spam, state-aware):

```javascript
function btcFullAlert() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  var price = sheet.getRange("B1").getValue();
  var props = PropertiesService.getScriptProperties();

  function checkAndAlert(name, lvl, type) {
    var key = type + "_" + name;
    var triggered = props.getProperty(key);

    if (
      (type === "BUY" && price <= lvl) ||
      (type === "SELL" && price >= lvl)
    ) {
      if (!triggered) {
        MailApp.sendEmail(
          "YOUR_EMAIL@gmail.com",
          type + " BTC ALERT: " + name,
          "BTC price: " + price + "\nLevel: " + name
        );
        props.setProperty(key, "true");
      }
    } else {
      props.deleteProperty(key);
    }
  }

  // BUY LEVELS
  [["L1","B8"],["L2","B9"],["L3","B10"],["L4","B11"],["L5","B12"]]
    .forEach(l => checkAndAlert(l[0], sheet.getRange(l[1]).getValue(), "BUY"));

  // SELL LEVELS
  [["S1","B16"],["S2","B17"],["S3","B18"],["S4","B19"],["S5","B20"]]
    .forEach(l => checkAndAlert(l[0], sheet.getRange(l[1]).getValue(), "SELL"));
}
```

---

## ⏱️ Enable Auto-Execution

1. Click **Triggers (clock icon)**
2. Add Trigger:

   * Function: `btcFullAlert`
   * Event: Time-driven
   * Frequency: Every 5 minutes

---

# 🔁 7. Daily Usage

### You DO:

* Check sheet once or twice daily
* Execute when:

  * 🔥 BUY appears
  * 🚨 SELL appears
* Update:

  * **Avg Cost (B4)** after buys
  * **Cycle High (B2)** when new regime forms

---

### You DO NOT:

* Predict tops or bottoms
* Override system emotionally
* Wait for “perfect entry”

---

# 🧠 System Philosophy

This system replaces:

> “Cycle guessing”

With:

> **Volatility execution**

---

# ⚠️ Risk Rules (Non-Negotiable)

* Never deploy 100% before L3 (-35%)
* Always keep 20–30% cash buffer
* Do not override ladder sizing
* Always sell into strength

---

# 🏁 What We Built

* 📊 Live BTC tracking
* 📉 Structured accumulation
* 📈 Structured distribution
* 🔔 Real-time alerts
* 🧠 Emotion-free execution

---
