import os
from string import ascii_lowercase

curdir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(curdir, 'input.txt')
with open(input_file, 'r') as fp:
    puzzle_input = fp.read().rstrip('\n')


def reactor(polymer: str) -> str:
    changes = True
    while changes:
        starting_length = len(polymer)
        for letter in ascii_lowercase:
            polymer = polymer.replace(letter + letter.upper(), '').replace(letter.upper() + letter, '')
            changes = starting_length != len(polymer)
    
    return polymer


def test_reactor():
    polymer = 'dabAcCaCBAcCcaDA'
    assert reactor(polymer) == 'dabCBAcaDA'


if __name__ == '__main__':
    stable_polymer = reactor(puzzle_input)
    unit_count = len(stable_polymer)
    print(f'{unit_count} units remain after fully reacting the polymer')