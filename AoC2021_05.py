def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


def points_between(x1, y1, x2, y2):
    if x1 == x2:
        n = abs(y1 - y2)
    else:
        n = abs(x1 - x2)
    stepx = sign(x2 - x1)
    stepy = sign(y2 - y1)
    for i in range(n + 1):
        yield x1 + i * stepx, y1 + i * stepy


def solution(A, part):
    points = {}
    for x1, y1, x2, y2 in A:
        if part == 2 or x1 == x2 or y1 == y2:
            for x, y in points_between(x1, y1, x2, y2):
                if (x, y) in points:
                    points[(x, y)] += 1
                else:
                    points[(x, y)] = 1
    # count items in points with value > 1
    return sum(1 for key, value in points.items()
               if value > 1)


def day05(infile):
    with open(infile, "r") as file:
        A = []
        for l in file.read().splitlines():
            p1, p2 = l.split(" -> ")
            x1, y1 = p1.split(",")
            x2, y2 = p2.split(",")
            A.append((int(x1), int(y1), int(x2), int(y2)))

    # solving Part One
    print("Part One: ", solution(A, part=1))

    # solving Part Two
    print("Part Two: ", solution(A, part=2))
