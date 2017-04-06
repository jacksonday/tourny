class Score:
    def __init__(self, name, points):
        self.name = name
        self.points = points

class Game:
    def __init__(self, game_string):
        self.scores = self.parse_scores(game_string)
        self.visitor_score = self.scores[0]
        self.home_score = self.scores[1]

        self.did_tie = False

        if self.visitor_score.points == self.home_score.points:
            self.did_tie = True
        elif self.visitor_score.points > self.home_score.points:
            self.winner_score = self.visitor_score
            self.loser_score = self.home_score
        else:
            self.winner_score = self.home_score
            self.loser_score = self.visitor_score

    @staticmethod
    def parse_scores(game_string):
        score_parts = game_string.split(",")

        # line = game_string
        # for i in range(4):
        #     if i == 0:
        #         t1 = line[i]
        #     elif i == 1:
        #         s1 = "placeholder"
        #         while s1 == "placeholder":
        #             try:
        #                 s1 = int(line[i].strip(','))
        #             except ValueError: #in this case, the value at line[i] is a word - part of a name, not a numerical score
        #                 t1 += " " + line.pop(i) # add word to end of team name # remove word from list of words in the line
        #     elif i == 2:
        #         t2 = line[i]
        #     elif i == 3:
        #         s2 = "placeholder"
        #         while s2 == "placeholder":
        #             try:
        #                 s2 = int(line[i].strip(','))
        #             except ValueError: #in this case, the value at line[i] is a word - part of a name, not a numerical score
        #                 t2 += " " + line.pop(i) # add word to end of team name # remove word from list of words in the line
            


        parsed_scores = []
        for score in score_parts:
            team_and_score = score.split()
            team_name = ' '.join(team_and_score[0:-1])
            points = int(team_and_score[-1])
            parsed_scores.append(Score(team_name,points))

        return parsed_scores
