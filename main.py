import TourneyMaster
MATCH_SYSTEM = "round robin"
ROUND_SYSTEM = "random"
PLAYER_DIRECTORY = '/home/hayg/Players'

print "The tournament will be: ", MATCH_SYSTEM
tourney = TourneyMaster.TourneyMaster(_tournamentType=MATCH_SYSTEM, _roundSystem=ROUND_SYSTEM)
tourney.load_player_modules(PLAYER_DIRECTORY)
print "Ladies and gentleman, today's contestants are: ", tourney.get_player_names()
tourney.create_matches()
print "The matches are in! The matches are as follows: ", tourney.get_matches() 
tourney.start_tourney()
winner = tourney.get_winner()
print "The final score is: ", tourney.get_score()
print "...and the winner is: ", winner
