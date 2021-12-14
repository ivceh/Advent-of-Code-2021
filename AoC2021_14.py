from functools import lru_cache
from collections import Counter


@lru_cache(maxsize=4500)
def count_elements_between(a, b, steps):
    if steps == 0:
        return Counter()
    else:
        c = day14.rules[a + b]
        return count_elements_between(a, c, steps - 1) + \
            count_elements_between(c, b, steps - 1) + \
            Counter(c)


def count_elements_after(polymer, steps):
    return sum((count_elements_between(a, b, steps)
                for a, b in zip(polymer, polymer[1:])),
               start=Counter(polymer))


def solution(polymer, steps):
    counts = count_elements_after(polymer, steps).values()
    return max(counts) - min(counts)


def day14(infile):
    with open(infile, "r") as file:
        lines = file.read().splitlines()
    polymer = lines[0]
    day14.rules = {}
    for line in lines[2:]:
        k, v = line.split(" -> ")
        day14.rules[k] = v

    print("Part One: ", solution(polymer, 10))
    print("Part Two: ", solution(polymer, 40))
