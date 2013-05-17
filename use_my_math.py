#! /usr/bin/env python

import my_math

#this works
#print my_math.factorial(5)

import sys

#print sys.argv

if len(sys.argv) > 1:
	print 'an argument was passed => {0}'.format(sys.argv[1])
	
	try:
		n = int(sys.argv[1])
		print my_math.factorial(n)

	except:	
		print 'non numeric argument passed => {0}'.format(sys.argv[1])

else:
	print 'no argument passed'
	print 'pass a numeric argument to calculate its factorial'

	#calculating a default value	
	'''
	print 'for now, we\'ll calculate 5\'s factorial'
	print my_math.factorial(5)
	'''

	raw_n = raw_input('Enter a number: ')
	try:
		n = int(raw_n)
		print my_math.factorial(n)
	except:
		print 'You must enter a valid number'

		



 
