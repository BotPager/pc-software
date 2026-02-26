import requests
import time

BASE_URL = input("Enter the base URL of the FTC Live API (e.g., ftclive.com): ")
EVENT_CODE = "4828"

url = f"http://{BASE_URL}/api/v1/events/{EVENT_CODE}/teams/"

def get_teams():
    response = requests.get(url, timeout=5)

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 429:
        print("Rate limited! Backing off...")
        return None
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

teams = get_teams()
file_path = 'team_numbers.txt'
number_of_teams = len(teams["teamNumbers"])
with open(file_path, 'w') as f_output:
    if teams:
        for team in teams["teamNumbers"]:
            print(team, file=f_output)
