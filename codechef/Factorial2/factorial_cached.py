cache = {
    1: 1
}

prev_i = 1
for i in range(2, 101):
    cache[i] = prev_i * i
    prev_i = cache[i]


count = int(raw_input())

i = 0
while i < count:
    n = int(raw_input())
    print cache[n]
    i += 1
