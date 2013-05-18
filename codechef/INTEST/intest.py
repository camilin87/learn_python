h = raw_input()
hl = h.split()

count = int(hl[0])
div = int(hl[1])

result = 0

for i in range(0, count):
    n = int(raw_input())
    if n % div == 0:
        result += 1

print result
