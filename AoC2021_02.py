class Submarine1:
    def __init__(self):
        self.horizontal = self.depth = 0

    def exec_line(self, l):
        direction, x = l
        if direction == "forward":
            self.move_forward(x)
        elif direction == "down":
            self.move_up_down(x)
        elif direction == "up":
            self.move_up_down(-x)

    def move_forward(self, x):
        self.horizontal += x

    # positive value for down, negative for up
    def move_up_down(self, x):
        self.depth += x

    def exec_lines(self, A):
        for l in A:
            self.exec_line(l)

    def product(self):
        return self.horizontal * self.depth


class Submarine2(Submarine1):
    def __init__(self):
        super().__init__()
        self.aim = 0

    def move_up_down(self, x):
        self.aim += x

    def move_forward(self, x):
        self.horizontal += x
        self.depth += self.aim * x


def day02(infile):
    A = []
    with open(infile, "r") as file:
        for l in file.read().splitlines():
            direction, x = l.split(" ")
            A.append((direction, int(x)))

    # resolving Part One
    submarine1 = Submarine1()
    submarine1.exec_lines(A)
    print("Part One: ", submarine1.product())

    # resolving Part Two
    submarine2 = Submarine2()
    submarine2.exec_lines(A)
    print("Part Two: ", submarine2.product())
