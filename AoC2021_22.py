import re
from sortedcontainers import SortedSet


def union_area(A):
    Sx = SortedSet()
    for i, (s, x1, x2, y1, y2, z1, z2) in enumerate(A):
        Sx.add((x1, i))
        Sx.add((x2, i))

    volume = 0
    Sy = SortedSet()
    for (x1, x1i), (x2, _) in zip(Sx, Sx[1:]):
        if x1 == A[x1i][1]:
            Sy.add((A[x1i][3], x1i))
            Sy.add((A[x1i][4], x1i))
        else:  # x1 == A[x1i][2]
            Sy.remove((A[x1i][3], x1i))
            Sy.remove((A[x1i][4], x1i))
        if x1 < x2:
            Sz = SortedSet()
            for (y1, y1i), (y2, _) in zip(Sy, Sy[1:]):
                if y1 == A[y1i][3]:
                    Sz.add((A[y1i][5], y1i))
                    Sz.add((A[y1i][6], y1i))
                else:  # y1 == A[y1i][4]
                    Sz.remove((A[y1i][5], y1i))
                    Sz.remove((A[y1i][6], y1i))
                if y1 < y2:
                    Cuboids = SortedSet()
                    for (z1, z1i), (z2, _) in zip(Sz, Sz[1:]):
                        if z1 == A[z1i][5]:
                            Cuboids.add(z1i)
                        else:  # z1 == A[z1i][6]
                            Cuboids.remove(z1i)
                        if (z1 < z2 and Cuboids and
                                A[Cuboids[-1]][0] == "on"):
                            volume += (x2 - x1) * (y2 - y1) *\
                                      (z2 - z1)
    return volume


def day22(infile):
    A = []
    with open(infile, "r") as file:
        for line in file.read().splitlines():
            match_obj = re.match(r'([a-z]+) x=(-?\d+)\.\.(-?\d+),'
                                 r'y=(-?\d+)\.\.(-?\d+),'
                                 r'z=(-?\d+)\.\.(-?\d+)', line)
            A.append((match_obj.group(1),
                      int(match_obj.group(2)),
                      int(match_obj.group(3)) + 1,
                      int(match_obj.group(4)),
                      int(match_obj.group(5)) + 1,
                      int(match_obj.group(6)),
                      int(match_obj.group(7)) + 1))

    B = [(s, x1, x2, y1, y2, z1, z2)
         for s, x1, x2, y1, y2, z1, z2 in A
         if x1 <= 50 and x2 >= -51 and
            y1 <= 50 and y2 >= -51 and
            z1 <= 50 and z2 >= -51]
    print("Part One: ", union_area(B))
    print("Part Two: ", union_area(A))
