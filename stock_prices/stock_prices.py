#!/usr/bin/python

import argparse

def find_max_profit(prices):
  x = 0
  y = 0
  x = min(prices)
  # y = max(prices)
  
  if x == prices[-1]:
      y = min(prices[:-1])
      primary = -y +x 
      if prices[prices.index(y) + 1 : -1]:
          secondary = -y + max(prices[prices.index(y) + 1 : -1])
          return primary if primary > secondary else secondary
      return primary
  else:
      y= max(prices[prices.index(x) + 1 :])
      return y - x
  # pass


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))