def fold1d(x, over):
    if x <= over:
        return x
    else:
        return 2 * over - x


def fold_dots_over(dots, along, over):
    dots2 = set()
    for x, y in dots:
        if along == 'x':
            x2 = fold1d(x, over)
            dots2.add((x2, y))
        else:  # along == 'y'
            y2 = fold1d(y, over)
            dots2.add((x, y2))
    return dots2


def day13(infile):
    dots = set()
    part1 = None
    with open(infile, "r") as file:
        for line in file.read().splitlines():
            if ',' in line:
                x, y = (int(w) for w in line.split(','))
                dots.add((x, y))
            elif 'x' in line:
                over = int(line.split('=')[1])
                dots = fold_dots_over(dots, 'x', over)
                if part1 is None:
                    part1 = len(dots)
            elif 'y' in line:
                over = int(line.split('=')[1])
                dots = fold_dots_over(dots, 'y', over)
                if part1 is None:
                    part1 = len(dots)

    print("Part One: ", part1)
    print("Part Two: ")
    maxx, maxy = (max(axis) for axis in zip(*dots))
    for j in range(maxy + 1):
        for i in range(maxx + 1):
            print('#' if (i, j) in dots else ' ', end='')
        print()
