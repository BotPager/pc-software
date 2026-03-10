import os
import numpy as np

class Team:
    def __init__(self, name = "-", pid = "-"):
        self.name = name            # team number (string or int)
        self.pid = pid              # hex pager ID (as string)

    def __repr__(self):
        return f"Team(name={self.name}, pid={self.pid})"


def load(filename="pid.txt"):
                loaded_pagers = []
                if not os.path.exists(filename):
                        print(f"Warning: {filename} not found ")
                        return loaded_pagers
            # get data from file
            # read line by line
                with open(filename) as f:
                        for line in f:
                   #strip
                                line = line.strip('\n')
                   # index 0 = teamnumber
                   # index 1 = pid
                   #validation
                                pid = line
                                if pid:
                                        loaded_pagers.append(pid)
                f.close()
                return loaded_pagers

def load(filename="team_numbers.txt"):
    #does the same as pid but for team numbers instead
    loaded_teams = []
    if not os.path.exists(filename):
        print(f"Warning: {filname} not found")
        return loaded_teams
    with open(filename) as f:
        for line in f:
            line = line.strip('\n')
            team_number = line
            if team_number:
                loaded_teams.append(team_number)
    f.close()
    return loaded_teams

def create_teams(size=16):
        team_set = []
        for i in range (0,size):
                team_set.append(Team())
        return team_set
def save_pid(team_list):
    filename = "pid.txt"
    pid_list = []
    for i in range(0,16):
        if team_list[i].pid == '-':
            continue
        else:
             pid_list.append(team_list[i].pid)  
    print(pid_list)
    converted = np.array(pid_list)
    np.savetxt(filename,converted,delimiter=",",fmt='%s')

#now do the same as above but for team names?
def save_team_number(team_list):
    filename = "team_numbers.txt"
    team_number_list = []
    for i in range (0,16):
        if team_list[i].name = '-':
            continue
        else:
            team_number_list.append(team_list[i].name)
    print(f"teams: {team_number_list}"")
    converted = np.array(team_number_list)
    np.savetxt(filename,convertedmdelimiter=",",fmt='%s')


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
def load_teams_from_file(filename,teams_list):
    loaded_teams = []
    if not os.path.exists(filename):
        print(f"Warning: {filename} not found ")
        return teams_list
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
           team = check_valid(text[0],text[1],loaded_teams)
           if team:
                loaded_teams.append(team)
    f.close()
    if loaded_teams:
        for a in range (0,len(loaded_teams)):
            teams_list[a] = loaded_teams[a]
    return teams_list
