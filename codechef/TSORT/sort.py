import sys

count = int(sys.stdin.readline())

for n in sorted(map(int, sys.stdin.readlines())):
    print n

'''
l_num = map(int, sys.stdin.readlines())
l_num.sort()
for n in l_num:
    print n
'''
