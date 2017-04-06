# Main Entry Point
import fileinput

from Tournament import Tournament

the_tournament = Tournament()

for line in fileinput.input():
    the_tournament.add_game(line)

teams = the_tournament.teams.values()
sorted_teams = sorted(teams)
rankings = Tournament.get_rankings(sorted_teams)
Tournament.print_results(rankings)