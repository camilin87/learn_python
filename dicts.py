#! /usr/bin/env python

spanish = {
	'a': 'primera letra del alfabeto',
	'b': 'la b de burro'
}

spanish['n'] = 'la primera letra de nicolas'

print 'we can iterate like this'
for k in spanish.keys():
	print k, spanish[k]

print 'this is the correct way of iterating'
for k, v in spanish.iteritems():
	print k, v
