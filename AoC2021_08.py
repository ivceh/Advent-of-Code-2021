def sort_str(s):
    return "".join(sorted(s))

C = "abcdefg"
nums = ((0, 1, 2, 4, 5, 6),
        (2, 5),
        (0, 2, 3, 4, 6),
        (0, 2, 3, 5, 6),
        (1, 2, 3, 5),
        (0, 1, 3, 5, 6),
        (0, 1, 3, 4, 5, 6),
        (0, 2, 5),
        (0, 1, 2, 3, 4, 5, 6),
        (0, 1, 2, 3, 5, 6))


def code_to_nums(a, x):
    count_segments = [a.count(c) for c in C]
    D = [None] * 7
    for i, n in enumerate(count_segments):

        # only upper left segment is on in 6 numbers
        if n == 6:
            D[1] = C[i]

        # only lower left segment is on in 4 numbers
        elif n == 4:
            D[4] = C[i]

        # only lower right segment is on in 9 numbers
        elif n == 9:
            D[5] = C[i]

        # middle and down segment are on in 7 numbers
        elif n == 7:
            # middle segment is on in digit 4
            if any(len(s) == 4 and C[i] in s for s in x):
                D[3] = C[i]
            else:
                D[6] = C[i]

        # up and upper right segment are on in 8 numbers
        elif n == 8:
            # upper right segment is on in digit 1
            if any(len(s) == 2 and C[i] in s for s in x):
                D[2] = C[i]
            else:
                D[0] = C[i]
        else:
            raise ValueError("Unknown display segment!")

    codes = [sort_str([D[i] for i in num]) for num in nums]
    return {s: i for i, s in enumerate(codes)}


def day08(infile):
    with open(infile, "r") as file:
        A = file.read().splitlines()

    part1 = part2 = 0
    for l in A:
        # parsing input
        a, b = l.split(" | ")
        y = b.split(" ")
        x = a.split(" ")

        # solving part1
        part1 += sum(len(i) in (2, 3, 4, 7) for i in y)

        # solving part2
        code_dict = code_to_nums(a, x)
        N = 0
        for s in y:
            N *= 10
            N += code_dict[sort_str(s)]
        part2 += N

    print("Part One: ", part1)
    print("Part Two: ", part2)
