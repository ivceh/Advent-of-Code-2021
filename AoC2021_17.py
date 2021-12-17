import re


def reaches(vx, vy):
    x = y = 0
    while y >= y1:
        if y <= y2 and x1 <= x <= x2:
            return True
        x += vx
        if vx > 0:
            vx -= 1
        y += vy
        vy -= 1
    return False


def day17(infile):
    global x1, x2, y1, y2
    with open(infile, "r") as file:
        line = file.readline()
        match_obj = re.match(r'target area: x=(-?\d+)\.\.(-?\d+), y=(-?\d+)\.\.(-?\d+)',
                             line)
        x1, x2, y1, y2 = (int(match_obj.group(i)) for i in range(1, 5))

    print("Part One: ", y1 * (y1 + 1) // 2)

    print("Part Two: ",
          sum(reaches(vx, vy)
              for vx in range(x2 + 1)
              for vy in range(y1, -y1 + 1)))
