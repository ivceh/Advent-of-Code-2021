def neighbourhood1d(i, length):
    if i > 0:
        yield i - 1
    yield i
    if i < length - 1:
        yield i + 1


class Cavern:
    def __init__(self, A):
        self.grid = [[int(c) for c in line] for line in A]
        self.step_cnt = self.flush_cnt = 0
        self.synchronized = False
        self.height = len(A)
        self.width = len(A[0])
        self.Flushed = None

    def neighbours(self, i, j):
        rows = list(neighbourhood1d(i, self.height))
        cols = list(neighbourhood1d(j, self.width))
        for row in rows:
            for col in cols:
                if row != i or col != j:
                    yield row, col

    def step_octopus(self, i, j):
        if (i, j) not in self.Flushed:
            if self.grid[i][j] < 9:
                self.grid[i][j] += 1
            else:
                self.flush(i, j)

    def flush(self, i, j):
        self.Flushed.add((i, j))
        self.flush_cnt += 1
        self.grid[i][j] = 0
        for row, col in self.neighbours(i, j):
            self.step_octopus(row, col)

    def step(self):
        self.step_cnt += 1
        self.Flushed = set()
        for i in range(self.height):
            for j in range(self.width):
                self.step_octopus(i, j)
        if len(self.Flushed) == self.height * self.width:
            self.synchronized = True


def day11(infile):
    with open(infile, "r") as file:
        cavern = Cavern(file.read().splitlines())

    for i in range(100):
        cavern.step()
    print("Part One: ", cavern.flush_cnt)

    while not cavern.synchronized:
        cavern.step()
    print("Part Two: ", cavern.step_cnt)
