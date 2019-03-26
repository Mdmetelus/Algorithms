#!/usr/bin/python

import sys

def rock_paper_scissors(n):
    choices = ['rock', 'paper', 'scissors']
	  all_game_choices = []

	  if n == 0:
		    return [[]]

	# def game_round(g_round, n_round):
	# 	  for i in range(0, len(choices)):
	# 		    g_round.append(choices[i])
	# 		if (n_round == n):
	# 			  all_game_choices.append
	# 		else:
	# 			  

	"""game_round([], 1)
    return all_game_choices 
  """


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')