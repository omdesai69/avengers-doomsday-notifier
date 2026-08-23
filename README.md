# Avengers: Doomsday Ticket Notifier (Pune)

> Automated 24/7 cloud monitoring for **BookMyShow** and **Paytm / District Movies** that sends urgent push notifications the moment tickets go live in Pune.

---

## Quick Start (Pune)

Follow these steps to receive instant alerts:

### Step 1: Install ntfy
- [Download for iOS (App Store)](https://apps.apple.com/app/ntfy/id1625396347)
- [Download for Android (Google Play)](https://play.google.com/store/apps/details?id=io.heckel.ntfy)

### Step 2: Subscribe to Topic
1. Open **ntfy**.
2. Tap **Add Subscription** (`+`).
3. Enter the topic name:
   ```text
   Avengers_Doomsday_Pune
   ```
4. Tap **Subscribe**.

### Step 3: Configure Urgent Priority
1. Open topic settings in ntfy.
2. Set **Priority** to **Max / Urgent** (allows notifications in Do Not Disturb mode).
3. Select an audible alarm sound.

The background worker continuously monitors major Pune venues (IMAX, PVR INOX, Cinepolis at Phoenix Marketcity, Pavilion Mall, Seasons Mall, Westend Mall).

---

## Multi-City Support

To monitor a different city:

1. Fork this repository.
2. Under **Settings -> Secrets and variables -> Actions**, configure:
   - `TARGET_CITY`: e.g., `mumbai`, `delhi`, `bengaluru`
   - `NTFY_TOPIC`: e.g., `Avengers_Doomsday_Mumbai`
3. GitHub Actions will run the automated monitoring schedule continuously.
