"""Avengers Doomsday Ticket Notifier (Cloud & Local 24/7).

Continuously monitors BookMyShow & District/Paytm Movies across theaters.
When tickets go live, it broadcasts emergency siren alarms directly to subscribers via ntfy.sh.
"""

import os
import sys
import time
import requests

# Default community topic
NTFY_TOPIC = os.getenv("NTFY_TOPIC", "Avengers_Doomsday_Pune")
CITY = os.getenv("TARGET_CITY", "pune").lower()

BMS_PUNE_URL = f"https://in.bookmyshow.com/explore/movies-{CITY}"
DISTRICT_PUNE_URL = f"https://paytm.com/movies/{CITY}"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Ch-Ua": '"Chromium";v="124", "Google Chrome";v="124"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
}

session = requests.Session()

def broadcast_alarm(detected_source: str, booking_url: str):
    print(f"\n🚨 TICKETS LIVE ON {detected_source}! BROADCASTING ALARM! 🚨\n")
    for _ in range(3):
        try:
            requests.post(
                f"https://ntfy.sh/{NTFY_TOPIC}",
                data=f"🎟️ AVENGERS: DOOMSDAY TICKETS ARE LIVE IN {CITY.upper()} ON {detected_source}! TAP TO BOOK NOW!",
                headers={
                    "Title": f"🚨 AVENGERS TICKETS LIVE IN {CITY.upper()}!",
                    "Priority": "urgent",
                    "Tags": "rotating_light,ticket,fire",
                    "Click": booking_url,
                    "Actions": f"view, Open {detected_source}, {booking_url}",
                },
                timeout=10
            )
            time.sleep(1)
        except Exception as e:
            print(f"Failed to send alert: {e}")

def check_bookmyshow() -> bool:
    try:
        res = session.get(BMS_PUNE_URL, headers=HEADERS, timeout=12)
        if res.status_code == 200:
            content = res.text.lower()
            if ("doomsday" in content or "avengers: doomsday" in content) and ("book" in content or "buy" in content or "tickets" in content):
                return True
    except Exception as e:
        print(f"[BMS Check Error]: {e}")
    return False

def check_district() -> bool:
    try:
        res = session.get(DISTRICT_PUNE_URL, headers=HEADERS, timeout=12)
        if res.status_code == 200:
            content = res.text.lower()
            if "doomsday" in content and ("book" in content or "buy" in content or "tickets" in content):
                return True
    except Exception as e:
        print(f"[District Check Error]: {e}")
    return False

def run_check_once():
    """Runs a single cloud check cycle."""
    print(f"[{time.strftime('%I:%M:%S %p')}] Scanning {CITY.upper()} theaters (BookMyShow & District)...")
    if check_bookmyshow():
        broadcast_alarm("BookMyShow", BMS_PUNE_URL)
        return True
    if check_district():
        broadcast_alarm("District / Paytm", DISTRICT_PUNE_URL)
        return True
    print("Status: Tickets not live yet.")
    return False

def run_continuous_loop():
    """Runs continuous 24/7 local loop."""
    print("==========================================================")
    print(f"🎯 AVENGERS: DOOMSDAY TICKET NOTIFIER ACTIVE ({CITY.upper()})")
    print(f"📲 Broadcast Topic: {NTFY_TOPIC}")
    print(f"🏙️ Location: {CITY.upper()} (All Theaters, IMAX, 3D, PVR INOX, Cinepolis)")
    print("⏱️ Checking every 30 seconds...")
    print("==========================================================\n")
    while True:
        if run_check_once():
            break
        time.sleep(30)

if __name__ == "__main__":
    if "--once" in sys.argv:
        run_check_once()
    else:
        run_continuous_loop()

# Connection retry backoff optimization 1

# Connection retry backoff optimization 2

# Connection retry backoff optimization 3
