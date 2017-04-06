from Game import Game
from Team import Team


class Tournament:
    def __init__(self):
        self.teams = {}
        self.games = []

    def add_game(self, game_string):
        game = Game(game_string)

        self.games.append(game)

        if game.did_tie:
            return self.add_tied_game(game)
        self.find_team(game.winner_score.name).add_win(game)
        self.find_team(game.loser_score.name).add_loss(game)

    def add_tied_game(self, game):
        self.find_team(game.home_score.name).add_tie(game, game.home_score)
        self.find_team(game.visitor_score.name).add_tie(game, game.visitor_score)

    def find_team(self, team_name):
        if team_name not in self.teams:
            self.teams[team_name] = Team(team_name)
        return self.teams[team_name]

    # Assumes the passed rankings are already sorted correctly
    @staticmethod
    def get_rankings(sorted_teams):
        ranking = {}
        last_rank = 0
        next_rank = 1
        last_points = False

        for team in sorted_teams:
            this_rank = Tournament.determine_rank(last_rank, next_rank, last_points, team.tournament_points)

            if this_rank not in ranking:
                ranking[this_rank] = []

            ranking[this_rank].append(team)

            last_points = team.tournament_points
            last_rank = this_rank
            next_rank += 1

        return ranking

    @staticmethod
    def determine_rank(last_rank, next_rank, last_points, this_points):
        if last_rank == 0:
            return 1

        if last_points == this_points:
            return last_rank

        return next_rank

    @staticmethod
    def print_results(rankings):
        print "~~~~~~~~ Tournament Results ~~~~~~~~"
        for rank, teams in rankings.iteritems():
            for team in teams:
                print "{}. {} {}".format(rank, team.name, team.tournament_points)
