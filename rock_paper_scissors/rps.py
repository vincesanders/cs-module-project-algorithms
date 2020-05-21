#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  # Your code here
  moves = {
    0: 'rock',
    1: 'paper',
    2: 'scissors'
  }
  permutations = []
  if n is 0:
    permutations.append([])
  for _ in range(n):
    for j in range(3):
      permutations.append(moves[j]) # Get list of all possible permutations
  # flip solution 90 degrees
  solution = []
  index = 0
  while index < len(permutations):
    round = []
    for i in range(n):
      round.append(permutations[index])
      index += 1
    solution.append(round)


  return solution
  # go through each round


print(rock_paper_scissors(2))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')