import requests
import socket

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Doesn't actually connect, just forces IP resolution
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

BASE_URL = get_local_ip()
EVENT_CODE = 4290               #EDIT FOR OFFICIAL EVENT RUNS: 4290 is testing
number_of_teams = 16            #EDIT FOR OFFICIAL EVENT RUNS: 16 is max teams at an event

active_match_url = f"http://{BASE_URL}/api/v1/events/{EVENT_CODE}/matches/active/"

def get_active_match_details():
    try:
        response = requests.get(active_match_url, timeout=5)
    except:
        print("Error connecting to FTC Live. Check connection or restart the system")
        return None

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 429:
        print("Rate limited! Backing off...")
        return None
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None
    
def get_next_match_number():
    active_match_details = get_active_match_details()
    if not active_match_details:
        print("No active match details available.")
        return None

    matches = active_match_details.get("matches")
    if not matches:
        print("No active matches found.")
        return None

    match_number = matches[0].get("matchNumber")
    if match_number is None:
        print("Active match has no matchNumber.")
        return None

    match_number = match_number + 1
    if match_number > 80:
        print("No more matches to queue.")
        return None

    return match_number

def get_queue_match_details():
    next_match_number = get_next_match_number()
    if not next_match_number:
        return None

    queue_match_url = f"http://{BASE_URL}/api/v1/events/{EVENT_CODE}/matches/{next_match_number}"
    try:
        response = requests.get(queue_match_url, timeout=5)
    except:
        print("Error connecting to FTC Live. Check connection or restart the system")
        return None

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 429:
        print("Rate limited! Backing off...")
        return None
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None
