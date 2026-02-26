import os
import numpy as np

class Team:
    def __init__(self, name: str, pid: str):
        self.name = name            # team number (string or int)
        self.pid = pid              # hex pager ID (as string)

    def __repr__(self):
        return f"Team(name={self.name}, pid={self.pid})"

#checking if a set of teams is legal as in not blank and within range
# Pid is the meshtastic shortname
def check_valid(team_name,pid, current_teams):
    # Skip empty rows
    if team_name == "" or pid == "":
        return None

    # Validate team number
    if not (team_name.isdigit() and 1 <= int(team_name) <= 99999):
        print(f"Invalid TeamN: {team_name}")
        return None

    # Validate PID (4 hex characters)
    if not (len(pid) == 4 and all(c in "0123456789abcdefABCDEF" for c in pid)):
        print(f"Invalid PID: {pid}")
        return None
    #check duplicate team number or duplicate pid
    new_team = Team(team_name,pid)

    if any(t.name == new_team.name for t in current_teams):
        print(f"skipping duplicate team '{new_team.name}'")
        return None
    if any(t.pid == new_team.pid for t in current_teams):
        print(f"skipping duplicate team 'new_team.pid'")
        return None

    # Create and add Team object
    return new_team

    
#save teams when we click load teams
def save_teams_to_file(teams_list):
    #get data to list
    # convert to numpy array
    team_data = [[t.name, t.pid] for t in teams_list]
    converted_array = np.array(team_data)
    np.savetxt("teams.txt",converted_array,delimiter=",",fmt='%s') 

# loading teams from file into pc ui
#loads into the teams object for use on manual mode only
def load_teams_from_file(filename="teams.txt"):
    loaded_teams = []
    if not os.path.exists(filename):
        print(f"Warning: {filename} not found ")
        return loaded_teams
    # get data from file
    # read line by line
    with open("teams.txt") as f:
        for line in f:
           #strip
           line = line.strip('\n')
           # index 0 = teamnumber
           # index 1 = pid
           text = line.split(",",2)
           #validation
           team = check_valid(text[0],text[1,loaded_teams])
           if team:
                loaded_teams.append(team)
    f.close()
    return loaded_teams
