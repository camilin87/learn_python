#! /usr/bin/env python


l_multiples_of_three = [x*3 for x in range(1, 11)]

print 'first ten multiples of three'
print l_multiples_of_three


l_squares = [x**2 for x in range(1,11)]
l_cubes = [x**3 for x in range(1,11) if x**3 not in l_squares]

print 'cubes of the first ten numbers that are not suqares of another number'
print l_cubes


tuple = (1, 2, 3)
x, y, z = tuple
print 'multiple tuple association'
print x, y, z

l = [1, 2, 3]
a, b, c = l
print 'multiple list association'
print a, b, c



l1 = ['a', 'b', 'c']
l2 = [1, 2, 3]

print 'iterating over parallel arrays'
for i, j in zip(l1, l2):
	print i, j
