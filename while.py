#! /usr/bin/env python

'''
i = 0

while i < 100:
	print i
	i += 1

print 'I\'m done'
'''

def fib (n):
	if n < 2:
		return 1
	else:
		return fib(n-1) + fib(n-2)

#print fib(2)
#print range(0,3)

fibArr = []
i = 0
while i < 10:
	#this is more slow
	#fibArr += [fib(i)]
	fibArr.append(fib(i))
	i += 1

#print fibArr

#foreach in python
print 'printing all'
for i in fibArr:
	print i

print 'printing from arr[4] to arr[6]'
for i in fibArr[4:7]:
	print i

print 'printing the same range that according to nico is faster'
for i in range(4, 7):
	print fibArr[i]

print 'for int i = 0; i < arr.length; i++'
for i in range(len(fibArr)):
	print fibArr[i]
	#print i


print 'only even indices'
for i in range(0, len(fibArr), 2):
	print '[{0}] = {1}'.format(i, fibArr[i])

#print range(1, 10)
