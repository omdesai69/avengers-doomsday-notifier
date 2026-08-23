# 🎟️ Avengers: Doomsday — Ticket Drop Notifier (Pune)

> Automatically monitors **BookMyShow** and **District / Paytm Movies** 24/7 in the cloud and sends a **loud alarm notification directly to your phone** the moment tickets go live in Pune.

---

## ⚡ Quick Start (For Anyone in Pune) — 30 Seconds Setup

No coding or setup required. Follow these 3 simple steps:

### Step 1: Install the Free `ntfy` App
- 🍏 [Download for iOS (App Store)](https://apps.apple.com/app/ntfy/id1625396347)
- 🤖 [Download for Android (Google Play)](https://play.google.com/store/apps/details?id=io.heckel.ntfy)

### Step 2: Subscribe to the Pune Alert Channel
1. Open **`ntfy`**.
2. Tap **`+` (Add subscription)**.
3. Type the topic name:
   ```text
   Avengers_Doomsday_Pune
   ```
4. Tap **Subscribe**.

### Step 3: Enable Urgent Alarm
1. Open the topic settings inside `ntfy`.
2. Set **Priority** to **`Max / Urgent`** (this allows the siren to ring even in **Silent / Do Not Disturb** mode).
3. Select a loud alarm ringtone.

🎉 **Done!** The 24/7 cloud runner is actively monitoring all Pune theaters (IMAX, PVR INOX, Cinepolis at Phoenix Marketcity, Pavilion Mall, Seasons Mall, Westend Mall, etc.). When tickets drop, your phone will ring and give you the direct booking link.

---

## 🌍 For Other Cities (Mumbai, Delhi, Bengaluru, etc.)

To run this for your own city:
1. **Fork this repository**.
2. Add these variables under **Settings $\rightarrow$ Secrets and variables $\rightarrow$ Actions**:
   - `TARGET_CITY`: e.g. `mumbai`, `delhi`, `bengaluru`
   - `NTFY_TOPIC`: e.g. `Avengers_Doomsday_Mumbai`
3. The built-in **GitHub Actions 24/7 cloud runner** will monitor your city around the clock for free.
