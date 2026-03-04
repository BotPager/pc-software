import teams
import os
def main():
	team_set = []
	for i in range (0,16):
		team_set.append(teams.Team())
	pid = load("pid.txt")
	if pid:
		print(len(pid))
		for a in range(0,len(pid)):
			team_set[a].pid  = pid[a]
	for i in range (0,16):
		print(i)
		print(f"team {team_set[i].name} data {team_set[i].pid} ")
	print(len(team_set))
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


