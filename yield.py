#! /usr/bin/env python

def prime():
    
    l_primes = []
    cursor = 2

    while True:   

        is_prime = True

        for i in l_primes:
            if cursor % i == 0:
                is_prime = False
                break

        if is_prime:
            l_primes.append(cursor)
            yield cursor

	cursor += 1

import pprint

count = 0
for p in prime():
    print '{0:>10} = {1}'.format('[{0}]'.format(count), p)
    count += 1
    #if count > 13: break


#'{:>5}'.format('[{0}]'.format(count))
