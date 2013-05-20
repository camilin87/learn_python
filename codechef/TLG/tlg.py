import sys
import math

count = sys.stdin.readline()

max_diff = 0

for round_str in sys.stdin.readlines():
    round_values = map(int, round_str.split())
    player_1 = round_values[0]
    player_2 = round_values[1]

    print player_1, player_2
