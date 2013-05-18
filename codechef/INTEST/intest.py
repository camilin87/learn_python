import sys

h = sys.stdin.readline()
hl = h.split()

count = int(hl[0])
div = int(hl[1])

result = 0

'''
for i in range(0, count):
    n = int(sys.stdin.readline())
    if n % div == 0:
        result += 1
'''

for line in sys.stdin.readlines():
    if int(line) % div == 0:
        result += 1

print result
