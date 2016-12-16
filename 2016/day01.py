#!/usr/bin/env python

def course_change(turn, heading):
    """given a current heading and a right (R) or left (L) turn, return the new heading"""
    turns = {'R': 90, 'L': -90}
    heading += turns[turn]
    return (heading + 360) % 360

def move(cur_pos, heading):
    """given a position in a cartesian plane (x,y) and a heading (0-360), 
    return the new position in the cartesian plane."""
    x, y = cur_pos
    destination = {
            0: (x, y+1),
            90: (x+1, y),
            180: (x, y-1),
            270: (x-1, y),
            360: (x, y+1)
        }
    return destination[heading]

if __name__ == "__main__":

    # convert the puzzle input to turn, distance tuples
    puzzle_input = ['L4', 'L1', 'R4', 'R1', 'R1', 'L3', 'R5', 'L5', 'L2', 'L3', 'R2', 'R1', 'L4', 'R5', 'R4', 'L2', 'R1', 'R3', 'L5', 'R1', 'L3', 'L2', 'R5', 'L4', 'L5', 'R1', 'R2', 'L1', 'R5', 'L3', 'R2', 'R2', 'L1', 'R5', 'R2', 'L1', 'L1', 'R2', 'L1', 'R1', 'L2', 'L2', 'R4', 'R3', 'R2', 'L3', 'L188', 'L3', 'R2', 'R54', 'R1', 'R1', 'L2', 'L4', 'L3', 'L2', 'R3', 'L1', 'L1', 'R3', 'R5', 'L1', 'R5', 'L1', 'L1', 'R2', 'R4', 'R4', 'L5', 'L4', 'L1', 'R2', 'R4', 'R5', 'L2', 'L3', 'R5', 'L5', 'R1', 'R5', 'L2', 'R4', 'L2', 'L1', 'R4', 'R3', 'R4', 'L4', 'R3', 'L4', 'R78', 'R2', 'L3', 'R188', 'R2', 'R3', 'L2', 'R2', 'R3', 'R1', 'R5', 'R1', 'L1', 'L1', 'R4', 'R2', 'R1', 'R5', 'L1', 'R4', 'L4', 'R2', 'R5', 'L2', 'L5', 'R4', 'L3', 'L2', 'R1', 'R1', 'L5', 'L4', 'R1', 'L5', 'L1', 'L5', 'L1', 'L4', 'L3', 'L5', 'R4', 'R5', 'R2', 'L5', 'R5', 'R5', 'R4', 'R2', 'L1', 'L2', 'R3', 'R5', 'R5', 'R5', 'L2', 'L1', 'R4', 'R3', 'R1', 'L4', 'L2', 'L3', 'R2', 'L3', 'L5', 'L2', 'L2', 'L1', 'L2', 'R5', 'L2', 'L2', 'L3', 'L1', 'R1', 'L4', 'R2', 'L4', 'R3', 'R5', 'R3', 'R4', 'R1', 'R5', 'L3', 'L5', 'L5', 'L3', 'L2', 'L1', 'R3', 'L4', 'R3', 'R2', 'L1', 'R3', 'R1', 'L2', 'R4', 'L3', 'L3', 'L3', 'L1', 'L2']
    directions = [(step[0], int(step[1:])) for step in puzzle_input]
    

    # Where we landed, facing north
    heading = 0 
    position = (0, 0)
    visited = [(0,0)]
    hq = None

    for instruction in directions:
        turn, distance = instruction
        heading = course_change(turn, heading)
        for step in range(distance):
            position = move(position, heading)
            if hq:
                continue
            elif position in visited:
                hq = position
            else:
                visited.append(position)

    x, y = position
    xhq, yhq = hq

    def taxidist(start, end):
        p1, p2 = start
        q1, q2 = end
        return abs(p1-q1)+abs(p2-q2)

    part1dist = taxidist((0,0), position)
    part2dist = taxidist((0,0), hq)

    print 'Part 1: You are {} blocks away from Easter Bunny HQ.'.format(part1dist)
    print 'Part 2: You are {} blocks away from the real EB HQ.'.format(part2dist)
