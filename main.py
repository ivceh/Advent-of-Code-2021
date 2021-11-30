import AoC2021_01

days = [AoC2021_01.Day01]


def infile(i):
    return "inputs/input" + f"{i:02d}" + ".txt"


def exec_day(i):
    print("Day" + f"{i:02d}")
    days[i-1](infile(i))


def exec_all():
    for i in range(len(days)):
        exec_day(i + 1)
        print()


exec_day(1)