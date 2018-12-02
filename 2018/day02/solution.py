import os

curdir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(curdir, 'input.txt')

twice = 0
thrice = 0

prevline = ''

data = []
with open(input_file, 'r') as f:
    for line in f:
        line = line.rstrip('\n')
        data.append(line)

for line in data:
    letters = {}
    for letter in line:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1

    for letter, count in letters.items():
        if count == 2:
            twice += 1
            break

    for letter, count in letters.items():
        if count == 3:
            thrice += 1
            break

    for compare in data:
        diffcount = 0
        for index in range(len(line)):
            if compare[index] != line[index]:
                diffcount += 1
        
        if diffcount == 1:
            similar = [i for i, j in zip(compare, line) if i == j]    

print(f'Checksum: {twice * thrice}')
print(f'Similar letters: {"".join(similar)}')