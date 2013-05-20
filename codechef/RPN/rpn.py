import sys

l_operators = '()+-*/'

def rpn(expr):
    op_stack = []
    result = []
    for c in expr:
        if c in l_operators:
            result.append(c)

    return ''.join(result)


def main(args):
    count = sys.stdin.readline()
    for line in sys.stdin.readlines():
        print rpn(line)


if __name__=='__main__':
    main(sys.argv)
