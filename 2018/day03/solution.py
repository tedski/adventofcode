import os
from collections import Counter
from typing import List

curdir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(curdir, 'input.txt')

with open(input_file, 'r') as fp:
    puzzle_input = fp.read().splitlines()

def get_points(claim: str) -> List[tuple]:
    points = []
    claimid, _, raw_addr, raw_size = claim.split()
    addr = tuple(map(int, raw_addr.rstrip(':').split(',')))
    size = tuple(map(int, raw_size.split('x')))

    for y in range(1, size[1] + 1):
        for x in range(1, size[0] + 1):
            points.append((addr[0] + x, addr[1] + y))

    return points


def overlap_checker(claims: list) -> int:
    used_points = set()
    overlap_points = set()
    for claim in claims:

        points = get_points(claim)

        for point in points:
            if point in used_points:
                overlap_points.add(point)
            else:
                used_points.add(point)

    for claim in claims:
        points = get_points(claim)

        overlap = False
        for point in points:
            if point in overlap_points:
                overlap = True
                break
        
        if not overlap:
            claimid, _, _, _ = claim.split()
            no_overlap_claim = claimid.lstrip('#')

    return len(overlap_points), no_overlap_claim


def test_get_points():
    expected = Counter([(4, 3), (5, 3), (6, 3), (7, 3), (8, 3),
                        (4, 4), (5, 4), (6, 4), (7, 4), (8, 4),
                        (4, 5), (5, 5), (6, 5), (7, 5), (8, 5),
                        (4, 6), (5, 6), (6, 6), (7, 6), (8, 6)])
    assert Counter(get_points('#123 @ 3,2: 5x4')) == expected


def test_overlap_points():
    claims = ['#1 @ 1,3: 4x4',
              '#2 @ 3,1: 4x4',
              '#3 @ 5,5: 2x2']
    assert overlap_checker(claims) == (4, '3')

    
if __name__ == '__main__':
    count, good_claim = overlap_checker(puzzle_input)
    print(f'Square inches of fabric within two or more claims: {count}')
    print(f'Santa\'s suit can be made with claim: {good_claim}')