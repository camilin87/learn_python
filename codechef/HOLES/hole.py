import sys 

l_holes = {
    'A': 1,
    'B': 2,
    'D': 1,
    'O': 1,
    'P': 1,
    'Q': 1,
    'R': 1
}

def holes_in_string(s):
    result = 0
    for c in s:
        if l_holes.has_key(c):
            result += l_holes[c]
    return result


def main(args):
    count = sys.stdin.readline()

    for line in sys.stdin.readlines():
        print holes_in_string(line)


if __name__ == '__main__':
    main(sys.argv)
