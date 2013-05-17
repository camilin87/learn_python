#! /usr/bin/env python

def is_prime(n):
    ''' Determines if a number is prime 

    >>> print is_prime(0)
    False

    >>> print is_prime(1)
    False

    >>> print is_prime(2)
    True

    >>> print is_prime(3)
    True
    '''
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True



#to run the test
#>>> import doctest
#>>> doctest.testmod(unit_test)
