class Board:
    def __init__(self, lines):
        self.numbers = [[int(w)
                         for w in line.split(" ")
                         if w != '']
                        for line in lines]
        self.marked = [[False] * 5 for _ in range(5)]
        self.winner = False
        self.score = None

    def mark(self, n):
        for i, line in enumerate(self.numbers):
            for j, number in enumerate(line):
                if number == n:
                    self.marked[i][j] = True
                    self.check_winner(n)

    def check_winner(self, n):
        if (not self.winner and
            (any(all(self.marked[i][j]
                     for i in range(5))
                 for j in range(5)) or
             any(all(self.marked[i][j]
                     for j in range(5))
                 for i in range(5)))):
            self.winner = True
            self.score = n * sum(self.numbers[i][j]
                                 for i in range(5)
                                 for j in range(5)
                                 if not self.marked[i][j])


class Bingo:
    def __init__(self, in_str):
        self.number_stack = [int(w) for w in in_str[0].split(",")]
        self.number_stack.reverse()
        self.boards = []
        for l in range(len(in_str) // 6):
            self.boards.append(Board(in_str[6 * l + 2: 6 * l + 7]))

    def step(self):
        n = self.number_stack.pop()
        for board in self.boards:
            board.mark(n)

    def count_winners(self):
        return sum(board.winner for board in self.boards)


def day04(infile):
    with open(infile, "r") as file:
        bingo = Bingo(file.read().splitlines())

    # solving Part One
    while bingo.count_winners() == 0:
        bingo.step()
    for board in bingo.boards:
        if board.winner:
            print("Part One: ", board.score)

    # solving Part Two
    while bingo.count_winners() < len(bingo.boards) - 1:
        bingo.step()
    for board in bingo.boards:
        if not board.winner:
            last_board = board
    while bingo.count_winners() < len(bingo.boards):
        bingo.step()
    print("Part Two: ", last_board.score)
