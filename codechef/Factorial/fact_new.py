'''
def lead_z(n):
    result = 0
    i = 1

    while True:
        five_to_the_i = 5 ** i
        if five_to_the_i > n:
            break
        else:
            result += int(n/five_to_the_i)
        i += 1

    return result
'''


def lead_z(n):
    result = 0

    while n >= 5:
        n /= 5
        result += n

    return result


count = int(raw_input())

i = 0
while i < count:
    n = int(raw_input())
    print lead_z(n)

    i += 1
