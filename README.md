# 🎟️ Avengers: Doomsday Ticket Sniper (24/7 Cloud Alert)

> **Never miss IMAX or first-day tickets again.** Automatically monitors **BookMyShow** and **District / Paytm Movies** 24/7 in the cloud and triggers a **loud emergency siren alarm directly on your phone** the exact second tickets drop in your city.

---

## ⚡ Quick Start (For Anyone in Pune) — 30 Seconds Setup

You **do not need any coding knowledge or a laptop**. Just set up the alert on your phone:

### Step 1: Install the Free Alert App
1. Download **`ntfy`** on your phone:
   - 🍏 [iOS App Store](https://apps.apple.com/app/ntfy/id1625396347)
   - 🤖 [Google Play Store](https://play.google.com/store/apps/details?id=io.heckel.ntfy)

### Step 2: Subscribe to the Alert Channel
1. Open the **`ntfy`** app.
2. Tap **`+` (Add subscription)**.
3. Enter the topic name:
   ```text
   om_doomsday_pune_99
   ```
4. Tap **Subscribe**.

### Step 3: Enable Loud Alarm (Crucial!)
1. In the app, open the subscription settings:
   - Set **Priority** to **`Max / Urgent`** (this allows the siren to ring even on **Silent / Do Not Disturb** mode).
   - Choose a loud alarm sound.

🎉 **That's it!** The 24/7 cloud server is already monitoring all Pune theaters (IMAX, PVR INOX, Cinepolis at Phoenix Marketcity, Pavilion Mall, Seasons Mall, Westend Mall, etc.). The moment booking opens, your phone will ring with an emergency siren and give you the direct 1-tap booking link.

---

## 🌍 For Other Cities (Mumbai, Delhi, Bengaluru, etc.)

Want to run this for your own city?

1. **Fork this repository**.
2. Go to **Settings $\rightarrow$ Secrets and variables $\rightarrow$ Actions** in your forked repo and add:
   - `TARGET_CITY`: e.g. `mumbai`, `delhi`, `bengaluru`
   - `NTFY_TOPIC`: Your own custom topic name (e.g. `my_mumbai_alerts`)
3. The built-in **GitHub Actions 24/7 cloud runner** will automatically monitor your city around the clock for free!

---

## 🛠️ Local Execution (Optional)

If you prefer running the script on your own computer:

```bash
git clone https://github.com/omdesai69/pune-ticket-sniper.git
cd pune-ticket-sniper
pip install -r requirements.txt
python sniper.py
```

---

## 📄 License
MIT License. Built for movie fans.
