#!/usr/bin/python

import sys

def making_change(amount, denominations):
  t = [[0 for x in range(5)] for x in range(amount + 1)]

  for i in range(5):
  	t[0][i] = 1

  for i in range(1, amount + 1):
  	for j in range(5):
  		x = t[i - denominations[j]][j] if i - denominations[j] >= 0 else 0

  		y = t[i][j-1] if j >= 1 else 0

  		t[i][j] = x + y

  return t[amount][4] 


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")