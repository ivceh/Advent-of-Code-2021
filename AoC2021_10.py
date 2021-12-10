def day10(infile):
    with open(infile, "r") as file:
        A = file.read().splitlines()

    part1 = 0
    part2 = []
    scores1 = {')': 3, ']': 57, '}': 1197, '>': 25137}
    scores2 = {'(': 1, '[': 2, '{': 3, '<': 4}
    for line in A:
        Stack = []
        corrupted = False
        for c in line:
            if c in ('(', '[', '{', '<'):
                Stack.append(c)
            else:
                c2 = Stack.pop()
                if (c2, c) not in (('(', ')'), ('[', ']'),
                                   ('{', '}'), ('<', '>')):
                    corrupted = True
                    part1 += scores1[c]
                    break
        if not corrupted:
            score2 = 0
            while len(Stack) > 0:
                c = Stack.pop()
                score2 *= 5
                score2 += scores2[c]
            part2.append(score2)

    print("Part One: ", part1)

    part2.sort()
    print("Part Two: ", part2[len(part2) // 2])
