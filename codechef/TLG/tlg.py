import sys

def main(args):

    count = sys.stdin.readline()
    max_diff = 0

    for round_str in sys.stdin.readlines():
        round_values = map(int, round_str.split())
        player_1 = round_values[0]
        player_2 = round_values[1]

        temp_max_diff = player_1 - player_2
        if abs(temp_max_diff) > abs(max_diff):
            max_diff = temp_max_diff


    if max_diff > 0:
        print 1, max_diff
    else:
        print 2, abs(max_diff)

if __name__=='__main__':
    main(sys.argv)
