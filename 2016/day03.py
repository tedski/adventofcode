with open('day03_input.txt') as f:
    puzzle_input = [x for x in f.readlines()]

count = 0

# Part 1
for line in puzzle_input:
    triple = tuple(int(i) for i in line.split())
    if len(triple) != 3:
        continue
    elif triple[0]+triple[1] <= triple[2]:
        continue
    elif triple[0]+triple[2] <= triple[1]:
        continue
    elif triple[1]+triple[2] <= triple[0]:
        continue
    else:
        count += 1

# Part 2

print 'Part 1: There are {} valid triangles.'.format(count)
