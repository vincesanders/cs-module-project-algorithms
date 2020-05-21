#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  # Your code here
  moves = {
    0: 'rock',
    1: 'paper',
    2: 'scissors'
  }
  
  def track_permutations():
    index = 0
    return get_move
  def get_move():
    move = moves[index % 3]
    index += 1
    return move
  move = track_permutations()
  for p in range(3**n):
    round = []
    for i in range(n):
      round.append(move())


  return solution
  # go through each round


print(rock_paper_scissors(2))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')