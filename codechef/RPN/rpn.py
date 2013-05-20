import sys

l_operators = '()+-*/^'

def rpn(expr):
    op_stack = []
    result = []
    for c in expr:
        if c in l_operators:
            if c == ')':
                while len(op_stack) > 0:
                    op = op_stack.pop()
                    if op == '(':
                        break
                    else:
                        result.append(op)
            else:
                op_stack.append(c)
        else:
            result.append(c)

    while len(op_stack) > 0:
        result.append(op_stack.pop())

    return ''.join(result)


def main(args):
    count = sys.stdin.readline()
    for line in sys.stdin.readlines():
        print rpn(line)


if __name__=='__main__':
    main(sys.argv)
