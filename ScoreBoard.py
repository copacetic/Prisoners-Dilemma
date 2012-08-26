class ScoreBoard:
    """
    ScoreBoard is an object meant to be shared by MatchMaster and the players.
    It is published to by MatchMaster and subscribed to by the players.
    """
    def __init__(self, _numPlayers):
        self.results = []
        self.moves = []
        self.roundNum = 0
        self.numPlayers = _numPlayers
        self.score = [0]*self.numPlayers

    def enter_round_data(self, moves, result):
        """
        MatchMaster's way of updating the ScoreBoard with the moves and results
        of a new round.
        """
        assert len(moves) == self.numPlayers
        assert len(result) == self.numPlayers
        self.moves.append(moves)
        self.results.append(result)
        self.roundNum += 1

    def get_result(self, roundNum):
        """
        Returns a tuple of form (punishment for p1, punishment for p2)
        for the round denoted by roundNum.
        """
        return self.results[roundNum]

    def get_score(self):
        """
        Returns a tuple of form (p1 score, p2 score).
        """
        return tuple(self.score)

    def get_round_number(self):
        return self.roundNum

    def get_player_move(self, roundNum, player):
        """
        Returns the Move.* done by player in round roundNum.
        """
        return (self.moves[roundNum])[player]

