# valid moves
COOPERATE = 0
RESIST = 1

# payoff matrix
results = {
    (COOPERATE, COOPERATE): (3, 3),
    (COOPERATE, RESIST): (0, 7),
    (RESIST, COOPERATE): (7, 0),
    (RESIST, RESIST): (1, 1)
}


def solve(move1, move2):
    return results[(move1, move2)]
