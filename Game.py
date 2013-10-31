# valid moves
RAT_OUT = 0
STAY_SILENT = 1

# payoff matrix
results = {
    (RAT_OUT, RAT_OUT): (3, 3),
    (RAT_OUT, STAY_SILENT): (0, 7),
    (STAY_SILENT, RAT_OUT): (7, 0),
    (STAY_SILENT, STAY_SILENT): (1, 1)
}


def solve(move1, move2):
    return results[(move1, move2)]
