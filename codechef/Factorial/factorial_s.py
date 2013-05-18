global_fact_cursor = 1
global_fact_result = 1


def fact(n):
    global global_fact_cursor
    global global_fact_result

    #print 'globals', global_fact_cursor, global_fact_result

    fact_cursor = global_fact_cursor
    fact_result = global_fact_result

    #we'll continue where we left off to speed things up
    #for this particular exercise
    if n < fact_cursor:
        fact_cursor = 1
        fact_result = 1

    while fact_cursor <= n:
        fact_result *= fact_cursor
        fact_cursor += 1

    global_fact_cursor = fact_cursor - 1
    global_fact_result = fact_result

    return fact_result

#this calculates the leading zeroes in a rather slow way


def leadz(n):
    result = 0

    while n % 10 == 0:
        result += 1
        n /= 10

    return result


def leadz_s(n):
    s = str(n)
    result = 0
    i = len(s) - 1

    while i >= 0:
        if s[i] == '0':
            result += 1
        else:
            break
        i -= 1

    return result


count = int(raw_input())

i = 0
while i < count:
    #print leadz(fact(int(raw_input())))

    n = int(raw_input())
    f = fact(n)
    z = leadz_s(f)
    #z = leadz(f)

    #print n, f, z
    print z

    i += 1
