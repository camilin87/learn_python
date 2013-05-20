import sys

l_operators = '()+-*/'

def rpn(expr):
    op_stack = []
    for c in expr:
        if c in l_operators:
            print c

def main(args):
    print 'lolo'

if __name__=='__main__':
    main(sys.argv)
