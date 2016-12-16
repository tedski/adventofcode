#!/usr/bin/env python

def course_change(turn, heading):
    """given a current heading and a right (R) or left (L) turn, return the new heading"""
    turns = {'R': 90, 'L': -90}
    heading += turns[turn]
    return (heading + 360) % 360

def move(cur_pos, heading, distance):
    """given a position in a cartesian plane (x,y), a heading (0-360), 
    and a distance (int), return the new position in the cartesian plane."""
    x, y = cur_pos
    if (heading / 90) % 2:
        if heading == 270:
            x -= distance
        else:
            x += distance
    else:
        if heading == 180:
            y -= distance
        else:
            y += distance
    return (x, y)

if __name__ == "__main__":

    # convert the puzzle input to turn, distance tuples
    puzzle_input = ['L4', 'L1', 'R4', 'R1', 'R1', 'L3', 'R5', 'L5', 'L2', 'L3', 'R2', 'R1', 'L4', 'R5', 'R4', 'L2', 'R1', 'R3', 'L5', 'R1', 'L3', 'L2', 'R5', 'L4', 'L5', 'R1', 'R2', 'L1', 'R5', 'L3', 'R2', 'R2', 'L1', 'R5', 'R2', 'L1', 'L1', 'R2', 'L1', 'R1', 'L2', 'L2', 'R4', 'R3', 'R2', 'L3', 'L188', 'L3', 'R2', 'R54', 'R1', 'R1', 'L2', 'L4', 'L3', 'L2', 'R3', 'L1', 'L1', 'R3', 'R5', 'L1', 'R5', 'L1', 'L1', 'R2', 'R4', 'R4', 'L5', 'L4', 'L1', 'R2', 'R4', 'R5', 'L2', 'L3', 'R5', 'L5', 'R1', 'R5', 'L2', 'R4', 'L2', 'L1', 'R4', 'R3', 'R4', 'L4', 'R3', 'L4', 'R78', 'R2', 'L3', 'R188', 'R2', 'R3', 'L2', 'R2', 'R3', 'R1', 'R5', 'R1', 'L1', 'L1', 'R4', 'R2', 'R1', 'R5', 'L1', 'R4', 'L4', 'R2', 'R5', 'L2', 'L5', 'R4', 'L3', 'L2', 'R1', 'R1', 'L5', 'L4', 'R1', 'L5', 'L1', 'L5', 'L1', 'L4', 'L3', 'L5', 'R4', 'R5', 'R2', 'L5', 'R5', 'R5', 'R4', 'R2', 'L1', 'L2', 'R3', 'R5', 'R5', 'R5', 'L2', 'L1', 'R4', 'R3', 'R1', 'L4', 'L2', 'L3', 'R2', 'L3', 'L5', 'L2', 'L2', 'L1', 'L2', 'R5', 'L2', 'L2', 'L3', 'L1', 'R1', 'L4', 'R2', 'L4', 'R3', 'R5', 'R3', 'R4', 'R1', 'R5', 'L3', 'L5', 'L5', 'L3', 'L2', 'L1', 'R3', 'L4', 'R3', 'R2', 'L1', 'R3', 'R1', 'L2', 'R4', 'L3', 'L3', 'L3', 'L1', 'L2']
    directions = [(step[0], int(step[1:])) for step in puzzle_input]
    

    # Where we landed, facing north
    heading = 0 
    position = (0, 0)

    # Part 1
    for step in directions:
        heading = course_change(step[0], heading)
        position = move(position, heading, step[1])

    x, y = position

    print 'Part 1: You are {} blocks away from Easter Bunny HQ.'.format(abs(x+y))
