import functools


def part1(pos1, pos2):
    score1 = score2 = 0
    dice = 1
    while score2 < 1000:
        pos1 = (pos1 + 3 * dice + 3 - 1) % 10 + 1
        score1 += pos1
        dice += 3
        pos1, pos2, score1, score2 = pos2, pos1, score2, score1
    return score1 * (dice - 1)


D = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}
@functools.cache
def part2_wins(pos1, pos2, score1=0, score2=0):
    if score2 >= 21:
        return 0, 1
    else:
        A = tuple((part2_wins(pos2, (pos1 + k - 1) % 10 + 1,
                              score2,
                              score1 + (pos1 + k - 1) % 10 + 1),
                   v)
                  for k, v in D.items())
        B = ((a[1] * b, a[0] * b) for a, b in A)
        return tuple(sum(el) for el in zip(*B))


def day21(infile):
    with open(infile, "r") as file:
        pos1, pos2 = (int(line.split(": ")[1])
                      for line in file.read().splitlines())
    print("Part One: ", part1(pos1, pos2))
    print("Part Two: ", max(part2_wins(pos1, pos2)))
