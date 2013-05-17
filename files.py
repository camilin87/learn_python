#! /usr/bin/env python

from collections import deque

l_lines = deque([])

with open('/var/log/auth.log', 'r') as file:
    for line in file:
        l_lines.append(line)
        if len(l_lines) > 5:
            l_lines.popleft()

#no need to close the file because the with is sort of a using
#file.close()

for line in l_lines:
	print line

