from collections import Counter
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


def improvement_recommender(polymer: str) -> str:
    experiment_data = Counter()
    units = set(polymer.lower())
    for letter in units:
        reactants = polymer.replace(letter.upper(), '').replace(letter, '')
        product = reactor(reactants)
        experiment_data.update({letter: len(product)})
    best_improvement = experiment_data.most_common()[:-2:-1][0]
    return best_improvement


def test_reactor():
    polymer = 'dabAcCaCBAcCcaDA'
    assert reactor(polymer) == 'dabCBAcaDA'


def test_improvement():
    polymer = 'dabAcCaCBAcCcaDA'
    assert improvement_recommender(polymer) == 'c'


if __name__ == '__main__':
    stable_polymer = reactor(puzzle_input)
    unit_count = len(stable_polymer)
    unit, length = improvement_recommender(puzzle_input)
    print(f'{unit_count} units remain after fully reacting the polymer')
    print(f'Removing {unit} yields the shortest polymer of length {length}.')