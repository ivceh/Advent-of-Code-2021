def neighbours(i, j, height, width):
    if i > 0:
        yield i - 1, j
    if i < height - 1:
        yield i + 1, j
    if j > 0:
        yield i, j - 1
    if j < width - 1:
        yield i, j + 1


def explore(A, i, j, Visited):
    if A[i][j] == '9' or (i, j) in Visited:
        return
    else:
        Visited.add((i, j))
        for i2, j2 in neighbours(i, j, len(A), len(A[0])):
            explore(A, i2, j2, Visited)


def basin_size(A, i, j):
    S = set()
    explore(A, i, j, S)
    return len(S)


def day09(infile):
    with open(infile, "r") as file:
        A = file.read().splitlines()

    height = len(A)
    width = len(A[0])
    part1 = 0
    Basin_sizes = []
    for i in range(height):
        for j in range(width):
            if all(A[i][j] < A[i2][j2]
                   for i2, j2 in neighbours(i, j, height, width)):
                part1 += int(A[i][j]) + 1
                Basin_sizes.append(basin_size(A, i, j))

    print("Part One: ", part1)
    Basin_sizes.sort(reverse=True)
    print("Part Two: ",
          Basin_sizes[0] * Basin_sizes[1] * Basin_sizes[2])
