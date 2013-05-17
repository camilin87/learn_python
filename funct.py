#! /usr/bin/env python

#default parameter values are defined only once
#if they are mutalble they are changed foreach function call
def show_message(msg, title=''):
	print 'show_message two params', msg, title

#no function overloads
'''
def show_message(msg):
	print 'show_message one param', msg
'''

show_message('msg1', 'title1')
show_message('msg2')


dbl = lambda x: x * 2

print dbl(2)


#warning extreme geek content

def create_multiplier_for(n):
	return lambda x: x*n

two_mult = create_multiplier_for(2)

print two_mult(5)
print two_mult(11)


#remembering the map from F#

#map(lambda x: x * 2, range(1,11)) 

dbl = lambda x: x * 2

l = range (1, 11)

dbl_list = map(dbl, l)

print 'We\'ll double this list', l
print dbl_list 

print 'It could also be written like this'
print map(lambda x: x*2, range(1,11) )

print 'printing only the multiples of three'
print filter(lambda x: x%3 == 0, range(1,11))

print 'factorial'
print reduce(lambda x, y: x*y, range(1, 11))
