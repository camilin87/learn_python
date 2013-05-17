#! /usr/bin/env python

class Dog:
    weight = 10
    name = 'Fido'

    def __str__(self):
        return 'Dog [Weight: {0}, Name: {1}]'.format(self.weight, self.name)


d = Dog()
d.weight = 25
d.name = 'Pete'

l_dogs = [d, Dog()]

print 'l_dogs before serialization'
for d in l_dogs:
    print d

full_path = 'serialized_file'

import pickle

with open(full_path, 'w+') as file:
    pickle.dump(l_dogs, file)

del l_dogs

with open(full_path, 'r') as file:
    l_dogs = pickle.load(file)

print 'l_dogs after being deserialized from the file'
for dog in l_dogs:
    print dog
