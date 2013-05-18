def fact(n):
    i = 1
    result = 1

    while i <= n:
        result *= i
        i += 1

    return result


def leadz(n):
    result = 0

    while n % 10 == 0:
        result += 1
        n /= 10

    return result


count = int(raw_input())

i = 0
while i < count:
    #print leadz(fact(int(raw_input())))

    n = int(raw_input())
    f = fact(n)
    z = leadz(f)

    #print n, f, z
    print z

    i += 1
