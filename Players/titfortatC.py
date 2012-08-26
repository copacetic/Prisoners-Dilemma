import ScoreBoard
import Game 

class Player():
    def __init__(self, _scoreboard, _ID):
        self.scoreboard = _scoreboard
        self.ID = _ID

    def get_move(self):
        roundNum = self.scoreboard.get_round_number()
        if roundNum == 0:
            myMove = Game.COOPERATE
        else:
            myMove = self.scoreboard.get_player_move(roundNum-1, self.ID ^ 1)
        return myMove
