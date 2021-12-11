import time, AoC2021_01, AoC2021_02, AoC2021_03, AoC2021_04
import AoC2021_05, AoC2021_06, AoC2021_07, AoC2021_08, AoC2021_09
import AoC2021_10, AoC2021_11

days = [AoC2021_01.day01, AoC2021_02.day02, AoC2021_03.day03,
        AoC2021_04.day04, AoC2021_05.day05, AoC2021_06.day06,
        AoC2021_07.day07, AoC2021_08.day08, AoC2021_09.day09,
        AoC2021_10.day10, AoC2021_11.day11]


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
