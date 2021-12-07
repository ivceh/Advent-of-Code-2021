def ternary_search_min(low, high, f):
    diff = high - low
    if diff < 3:
        return min(f(i) for i in range(low, high + 1))
    else:
        mid1 = low + diff // 3
        mid2 = high - diff // 3
        if f(mid1) < f(mid2):
            return ternary_search_min(low, mid2, f)
        else:
            return ternary_search_min(mid1, high, f)


def solution(A, distance_cost):
    return ternary_search_min(min(A), max(A),
                              lambda x: sum(distance_cost(abs(i - x))
                                            for i in A))


def day07(infile):
    with open(infile, "r") as file:
        A = [int(l) for l in file.readline().split(",")]

    # solving Part One
    print("Part One: ", solution(A, lambda x: x))

    # solving Part Two
    print("Part Two: ", solution(A, lambda x: x * (x + 1) // 2))
