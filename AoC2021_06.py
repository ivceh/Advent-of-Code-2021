def cache2d(width):
    def memoize(f):
        my_cache = []

        def inner(m, n):
            if m > len(my_cache):
                my_cache.extend([None] * width
                                for i in range(m - len(my_cache) + 1))
            if my_cache[m][n] is None:
                sol = f(m, n)
                my_cache[m][n] = sol
                return sol
            else:
                return my_cache[m][n]
        return inner
    return memoize


@cache2d(width = 9)
def m_days_fish_n(m, n):
    if m == 0:
        return 1
    elif n > 0:
        return m_days_fish_n(m - 1, n - 1)
    else:
        return m_days_fish_n(m - 1, 6) + m_days_fish_n(m - 1, 8)


def solution(A, m):
    return sum(m_days_fish_n(m, n) for n in A)


def day06(infile):
    with open(infile, "r") as file:
        A = [int(l) for l in file.readline().split(",")]

    # solving Part One
    print("Part One: ", solution(A, 80))

    # solving Part Two
    part2 = 0
    print("Part Two: ", solution(A, 256))
