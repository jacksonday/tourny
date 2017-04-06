class Team:
    def __init__(self, team_name):
        self.name = team_name
        self.tournament_points = 0
        self.cumulative_score = 0
        self.games = []

    def add_win(self, game):
        self.tournament_points += 3
        self.cumulative_score += game.winner_score.points
        self.games.append(game)

    def add_loss(self, game):
        self.cumulative_score += game.loser_score.points
        self.games.append(game)

    def add_tie(self, game, team_data):
        self.cumulative_score += team_data.points
        self.tournament_points += 1
        self.games.append(game)

    def __cmp__(self, other):
        if hasattr(other, 'tournament_points'):
            val = self.tournament_points.__cmp__(other.tournament_points)

            if val == 0:
                if self.name < other.name:
                    return -1
                elif self.name == other.name:
                    return 0
                else:
                    return 1
            return -val
        return 0
