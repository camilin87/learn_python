import sys


'''
with open(sys.argv[1], 'r') as file_in:
    with open(sys.argv[2], 'w') as file_out:
        for line in file_in:
            if line.startswith('42'):
                break
            else:
                file_out.write(line)
'''

#python TEST.py < in_1.txt > out_1.txt

while True:
    line = raw_input()
    if line == '42':
        break
    else:
        print line
