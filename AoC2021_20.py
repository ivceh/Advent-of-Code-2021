def neighbourhood1d(i):
    yield i - 1
    yield i
    yield i + 1


def neighbours(i, j):
    rows = list(neighbourhood1d(i))
    cols = list(neighbourhood1d(j))
    for row in rows:
        for col in cols:
            yield row, col


def step():
    global default
    S1 = set()
    S2 = set()
    global S
    for i, j in S:
        for k, l in neighbours(i, j):
            S1.add((k, l))
    next_default = alg[0 if default == '.' else -1]
    for i, j in S1:
        bin9 = []
        for k, l in neighbours(i, j):
            if ((k, l) in S) == (default == '.'):
                bin9.append('1')
            else:
                bin9.append('0')
        if alg[int("".join(bin9), base=2)] != next_default:
            S2.add((i, j))
    S = S2
    default = next_default


def day20(infile):
    global S, alg, default
    with open(infile, "r") as file:
        A = file.read().splitlines()
        alg = A[0]
        default = '.'
        S = {(i - 2, j)
             for i in range(len(A))
             for j in range(len(A[i]))
             if i >= 2 and A[i][j] == '#'}

    for i in range(2):
        step()
    print("Part One: ", len(S))

    for i in range(48):
        step()
    print("Part Two: ", len(S))
