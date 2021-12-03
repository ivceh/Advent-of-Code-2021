import time, AoC2021_01, AoC2021_02, AoC2021_03
days = [AoC2021_01.day01, AoC2021_02.day02, AoC2021_03.day03]


def infile(i, input_add = None):
    return "inputs/input" + f"{i:02d}" +\
           ("" if input_add is None else "_" + input_add) +\
           ".txt"


def exec_day(i, input_add = None):
    start_time = time.time()
    print("Day" + f"{i:02d}")
    days[i - 1](infile(i, input_add))
    end_time = time.time()
    time_diff = (end_time - start_time)
    print(f"{time_diff:.6f}", "s")


def exec_all():
    for i in range(len(days)):
        exec_day(i + 1)
        print()


def exec_days(day = None, input_add = None):
    if day is None:
        exec_all()
    else:
        exec_day(day, input_add)
