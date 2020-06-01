import re

out = open('clean Gone with the Wind.txt', 'w')

is_a_comment_start = False
is_a_comment_end = False
c = 0

needed = [' ']

with open('Gone with the Wind.txt', 'r', errors='ignore') as file:
    for line in file:
        out_line = ''
        for symb in line:
            if symb == '\n':
                out_line += ' '
            if symb.isalpha() or (symb in needed):
                out_line += symb
        out.write(out_line)


file.close()
out.close()