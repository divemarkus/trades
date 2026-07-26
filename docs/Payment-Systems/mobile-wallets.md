# Mobile Wallets

Below are the setup procedures for each scenario. One important note first:

> **Google Pay** (the payment service) and **Google Wallet** (the app that stores cards, passes, and payment credentials) are closely integrated. On Android, you'll generally use the **Google Wallet** app to configure tap-to-pay.

---

# 1. Samsung Galaxy Fold using Google Wallet (Recommended)

Although Samsung phones come with Samsung Wallet, you can absolutely use Google Wallet instead.

## Step 1 — Install or Update Google Wallet

* Open Google Play Store
* Search for **Google Wallet**
* Install or update it
* Sign in with your Google Account

---

## Step 2 — Add Your Credit Card

Open:

> Google Wallet → Add to Wallet → Payment Card

Choose:

* Scan card
* Enter manually

Verify with:

* SMS
* Email
* Bank app
* Phone call

---

## Step 3 — Set Google Wallet as Default

Go to:

Settings

→ Connections

→ NFC and Contactless Payments

→ Contactless Payments

Select:

✅ Google Wallet

instead of Samsung Wallet.

(Some One UI versions place this under **Settings → Apps → Default Apps → Tap & Pay**.)

---

## Step 4 — Enable NFC

Settings

→ Connections

→ NFC

Turn ON

---

## Step 5 — Enable Device Security

Google Wallet requires:

* Fingerprint
* Face Unlock
* PIN
* Pattern

No screen lock = No Wallet payments.

---

## Step 6 — Test

Unlock phone

Hold near terminal

Done.

---

# 2. Google Wallet on Google Pixel

This is Google's reference implementation.

---

### Install

Most Pixels already include Google Wallet.

If missing:

Play Store

→ Google Wallet

---

### Add Card

Wallet

→ Add Card

→ Scan

→ Verify

---

### Enable NFC

Settings

→ Connected Devices

→ Connection Preferences

→ NFC

ON

---

### Set Default

Normally already default.

If needed:

Settings

→ Default Apps

→ Wallet App

Select Google Wallet.

---

### Pay

Unlock phone

Tap terminal

Finished.

---

# 3. Google Pay on an Apple iPhone

Unfortunately, **you cannot use Google Wallet for NFC tap-to-pay on iPhone**.

| Feature                    | Android | iPhone  |
| -------------------------- | ------- | ------- |
| Google Wallet stores cards | ✅       | Limited |
| Google Wallet tap-to-pay   | ✅       | ❌       |
| Apple Pay                  | ❌       | ✅       |

Apple restricts NFC payment access on iPhone to Apple Wallet for consumer tap-to-pay.

You can still use Google apps and services on iPhone, but **contactless card payments must go through Apple Pay**.

---

# 4. Setting Up Apple Pay

## Step 1

Open:

Wallet

Tap:

➕

---

## Step 2

Choose:

Debit or Credit Card

---

## Step 3

Scan the card

or

Enter manually

---

## Step 4

Verify

Usually:

* SMS
* Banking App
* Email
* Phone Call

---

## Step 5

Done

The card appears in Wallet.

---

## Step 6

Double-click Side Button

Authenticate:

* Face ID
* Touch ID
* Passcode

Tap payment terminal.

---

## Apple Watch

Open Watch app

Wallet & Apple Pay

Add card

Now you can pay even if the iPhone stays in your pocket.

---

# 5. Setting Up Samsung Wallet

Samsung Wallet includes payments plus storage for IDs, digital keys, loyalty cards, boarding passes, and more (availability varies by region).

---

### Step 1

Open:

Samsung Wallet

Sign in with Samsung Account.

---

### Step 2

Tap:

Add

Credit/Debit Card

---

### Step 3

Scan card

or

Manual entry

---

### Step 4

Verify with your bank.

---

### Step 5

Enable Security

Samsung Wallet requires one of:

* Fingerprint
* PIN
* Face Recognition

---

### Step 6

Enable NFC

Settings

→ Connections

→ NFC

ON

---

### Step 7

Pay

Swipe up (if configured) or open Samsung Wallet

Authenticate

Tap payment terminal

Done.

---

# Feature Comparison

| Feature                            |      Google Wallet      |          Apple Pay          | Samsung Wallet |
| ---------------------------------- | :---------------------: | :-------------------------: | :------------: |
| Android                            |            ✅            |              ❌              |  Samsung only  |
| iPhone                             | Limited (no tap-to-pay) |              ✅              |        ❌       |
| Samsung Phones                     |            ✅            |              ❌              |        ✅       |
| Pixel Phones                       |            ✅            |              ❌              |        ❌       |
| NFC Payments                       |            ✅            |              ✅              |        ✅       |
| Biometric Authentication           |            ✅            |              ✅              |        ✅       |
| Tokenization                       |            ✅            |              ✅              |        ✅       |
| Secure Hardware                    |            ✅            |              ✅              |        ✅       |
| Boarding Passes                    |            ✅            |              ✅              |        ✅       |
| Loyalty Cards                      |            ✅            |              ✅              |        ✅       |
| Car Keys (supported models)        |           Some          |    Many supported brands    |      Some      |
| Government IDs (supported regions) |         Limited         | Supported in select regions |     Limited    |

## Which Should You Use?

| Device                  | Recommended Wallet                                                                                                                                                                      | Why                                                                                                        |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Samsung Galaxy Fold     | **Google Wallet** if you want consistency across Android devices; **Samsung Wallet** if you want Samsung-exclusive features like supported digital car keys and ecosystem integrations. |                                                                                                            |
| Google Pixel            | **Google Wallet**                                                                                                                                                                       | Native, deeply integrated with Android.                                                                    |
| Apple iPhone            | **Apple Pay**                                                                                                                                                                           | The only option for NFC tap-to-pay on iPhone.                                                              |
| Multiple Android brands | **Google Wallet**                                                                                                                                                                       | Consistent experience when switching between Samsung, Pixel, Motorola, OnePlus, and other Android devices. |

If you frequently switch Android phones or travel internationally, **Google Wallet** is generally the most portable choice. If you're heavily invested in the Samsung ecosystem, **Samsung Wallet** offers additional ecosystem features while maintaining a similar level of payment security.
