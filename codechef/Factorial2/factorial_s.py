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

    global_fact_cursor = n
    global_fact_result = fact_result

    return fact_result


count = int(raw_input())

i = 0
while i < count:
    n = int(raw_input())
    f = fact(n)
    print f

    i += 1
