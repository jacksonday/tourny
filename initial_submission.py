import fileinput
import random

scores = fileinput.input("scores.txt")

# keep track of tourney points and goal totals for all teams in dictionaries.
# values of the dictionary are lists, representing tournament_points and cumulative_goals_scored, respectively.
teams = dict()

#parse scores.txt for team names and scores
for line in scores:
	line = line.split()
	for i in range(4):
		if i == 0:
			t1 = line[i]
		elif i == 1:
			s1 = "placeholder"
			while s1 == "placeholder":
				try:
					s1 = int(line[i].strip(','))
				except ValueError: #in this case, the value at line[i] is a word - part of a name, not a numerical score
					t1 += " " + line.pop(i) # add word to end of team name # remove word from list of words in the line
		elif i == 2:
			t2 = line[i]
		elif i == 3:
			s2 = "placeholder"
			while s2 == "placeholder":
				try:
					s2 = int(line[i].strip(','))
				except ValueError: #in this case, the value at line[i] is a word - part of a name, not a numerical score
					t2 += " " + line.pop(i) # add word to end of team name # remove word from list of words in the line

# update team tournament dict and award points to winners and tie-ers. also update total goals
	if t1 not in teams:
		teams[t1] = [0, 0]
	if t2 not in teams:
		teams[t2] = [0, 0]
	if s1 > s2:
		teams[t1][0] += 3
	elif s1 < s2:
		teams[t2][0] += 3
	else:
		teams[t1][0] += 1
		teams[t2][0] += 1

	teams[t1][1] += s1
	teams[t2][1] += s2

# helper function
def getpoints(item):
	return item[1][0]

def getgoals(item):
	return item[1][1]

# next step is to analyze and output team rankings with tournament points scored
# don't forget to choose randomly (50/50) if teams are tied in points and goals.
def rank_teams(teams):
	
	# srt is rankings in a list of tuples sorted by their tournament points, and then by goals scored
	srt = sorted(teams.items(), key=getgoals, reverse=True)
	srt = sorted(srt, key=getpoints, reverse=True)

	old_srt = "placeholder"
	# make sure ties in tournament points are sorted by who has the greater goal total, or randomly if the goal total is a tie
	# loop until we have the rankings down pat
	while srt is not old_srt:
		old_srt = srt
		for i in range(len(srt)-1):
			# swap if points are equal, goals are equal, and random float > .5
			if (getpoints(srt[i]) == getpoints(srt[i+1])) and (getgoals(srt[i]) == getgoals(srt[i+1])) and (random.random() > 0.5):
				_ = srt[i]
				srt[i] = srt[i+1]
				srt[i+1] = _

	# print rankings
	for i, pair in enumerate(srt):
		rank = i + 1
		team_name = srt[i][0]
		t_points = srt[i][1][0]
		t_goals = teams[team_name][1]

		print "{}. {} {}({})".format(rank, team_name, t_points, t_goals)

rank_teams(teams)