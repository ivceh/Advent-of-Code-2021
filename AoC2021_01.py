def day01(infile):
    with open(infile, "r") as file:
        A = [int(l) for l in file.read().splitlines()]

    # resolving Part One
    cnt1 = 0
    for n, m in zip(A[:-1], A[1:]):
        if n < m:
            cnt1 += 1
    print("Part One: ", cnt1)

    # resolving Part Two
    cnt2 = 0
    for n, m in zip(A[:-3], A[3:]):
        if n < m:
            cnt2 += 1
    print("Part Two: ", cnt2)
