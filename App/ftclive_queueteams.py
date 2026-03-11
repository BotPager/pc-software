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
EVENT_CODE = input("Enter the event code: ")
number_of_teams = int(input("Enter the number of teams: "))

active_match_url = f"http://{BASE_URL}/api/v1/events/{EVENT_CODE}/matches/active/"

def get_active_match_details():
    response = requests.get(active_match_url, timeout=5)

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
    if active_match_details.get("matches"):
        match_number = active_match_details["matches"][0].get("matchNumber")
    else:
        print("No active matches found.")
        return

    match_number = match_number + 1
    if match_number > number_of_teams:
        print("No more matches to queue.")
    return match_number

def get_queue_match_details():
    next_match_number = get_next_match_number()
    if not next_match_number:
        return None

    queue_match_url = f"http://{BASE_URL}/api/v1/events/{EVENT_CODE}/matches/{next_match_number}"
    response = requests.get(queue_match_url, timeout=5)

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 429:
        print("Rate limited! Backing off...")
        return None
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

queue_match_details = get_queue_match_details()
if queue_match_details:
    file_path = 'queue_teams.txt'
    red_team1 = queue_match_details["matchBrief"]["red"]["team1"]
    red_team2 = queue_match_details["matchBrief"]["red"]["team2"]
    blue_team1 = queue_match_details["matchBrief"]["blue"]["team1"]
    blue_team2 = queue_match_details["matchBrief"]["blue"]["team2"]
    with open(file_path, 'w') as f_output:
        print(red_team1, file=f_output)
        print(red_team2, file=f_output)
        print(blue_team1, file=f_output)
        print(blue_team2, file=f_output)



