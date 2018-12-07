import os
import re

curdir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(curdir, 'input.txt')
with open(input_file, 'r') as fp:
    puzzle_input = fp.read().rstrip('\n')


def reactor(polymer: str) -> str:
    unit_pattern = re.compile(r'((\w)(\2))', re.IGNORECASE)
    polarity_pattern = re.compile(r'(\w)(?!\1)')
    unit_matches = unit_pattern.findall(polymer)
    product = ''
    changes = False

    for unit_match in unit_matches:
        reactant = unit_match[0]
        if polarity_pattern.search(reactant):
            product = re.sub(reactant, '', polymer)
            changes = True
    
    if changes:
        return reactor(product)
    else:
        return polymer



def test_reactor():
    polymer = 'dabAcCaCBAcCcaDA'
    assert reactor(polymer) == 'dabCBAcaDA'


if __name__ == '__main__':
    stable_polymer = reactor(puzzle_input)
    unit_count = len(stable_polymer)
    print(f'{unit_count} units remain after fully reacting the polymer')