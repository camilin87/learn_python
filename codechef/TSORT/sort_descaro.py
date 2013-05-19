import sys


def f():
    #only by creating this function it will run faster
    count = int(sys.stdin.readline())

    big_list = [0]*1000000

    for x in map(int, sys.stdin.readlines()):
        big_list[x] += 1

    #hmmm... very intersting
    #xrange is lazy and doesn't create a list
    for i in xrange(1000000):
        if big_list[i] > 0:
            print (str(i) + '\n') * big_list[i]

    #even though this works, it is actually slower :(
    '''
    for i in xrange(1000000):
        for n in xrange(big_list[i]):
            print i
    '''

f()
