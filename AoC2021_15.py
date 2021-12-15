import heapq


# Dijkstra's algorithm
# input: function for neighbours of arbitrary point, start, end,
#        function for cost of path between arbitrary two points
# output: minimal cost from start to end
def dijkstra(neighbours, start, end, cost):
    H = [(0, start)]
    visited = set()
    while H:
        dist, p = heapq.heappop(H)
        if p not in visited:
            if p == end:
                return dist
            visited.add(p)
            for p2 in neighbours(p):
                heapq.heappush(H, (dist + cost(p, p2), p2))


def my_neighbours(width, height):
    def neighbours(p):
        i, j = p
        if i > 0:
            yield i - 1, j
        if i < height - 1:
            yield i + 1, j
        if j > 0:
            yield i, j - 1
        if j < width - 1:
            yield i, j + 1
    return neighbours


def p2cost(cost):
    def f(_, p2):
        i, j = p2
        return cost(i, j)
    return f


def B(i, j, height, width):
    return (int(A[i % height][j % width]) - 1
            + i // height
            + j // width) % 9 + 1


def day15(infile):
    global A
    with open(infile, "r") as file:
        A = file.read().splitlines()
    height = len(A)
    width = len(A[0])
    print("Part One: ", dijkstra(my_neighbours(height, width),
                                 (0, 0),
                                 (height - 1, width - 1),
                                 p2cost(lambda i, j: int(A[i][j]))))
    print("Part Two: ", dijkstra(my_neighbours(height * 5, width * 5),
                                 (0, 0),
                                 (height * 5 - 1, width * 5 - 1),
                                 p2cost(lambda i, j:
                                        B(i, j, height, width))))
