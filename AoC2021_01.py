from itertools import islice

def day01(infile):
    with open(infile, "r") as file:
        A = [int(l) for l in file.read().splitlines()]

    # resolving Part One
    cnt1 = 0
    for n, m in zip(islice(A, 0, len(A) - 1),
                    islice(A, 1, None)):
        if n < m:
            cnt1 += 1
    print("Part One: ", cnt1)

    # resolving Part Two
    cnt2 = 0
    for n, m in zip(islice(A, 0, len(A) - 3),
                    islice(A, 3, None)):
        if n < m:
            cnt2 += 1
    print("Part Two: ", cnt2)
