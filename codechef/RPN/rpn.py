import sys

l_operators = '()+-*/^'

def rpn(expr):
    op_stack = []
    result = ''
    for c in expr:
        if c in l_operators:
            if c == ')':
                #while len(op_stack) > 0:
                for i in range(len(op_stack)):
                    op = op_stack.pop()
                    if op == '(':
                        break
                    else:
                        result += op
            else:
                op_stack.append(c)
        else:
            result += c

    op_stack.reverse()
    return result + ''.join(op_stack)


def main(args):
    count = sys.stdin.readline()
    for line in sys.stdin.readlines():
        print rpn(line)


if __name__=='__main__':
    main(sys.argv)
