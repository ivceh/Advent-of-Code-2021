def paths(cave_map, cave, small_caves_visited = None,
          twice_allowed = False, depth=0):
    if small_caves_visited is None:
        small_caves_visited = set()

    if cave == "end":
        return 1
    else:
        if cave.islower():
            if cave in small_caves_visited:
                if twice_allowed:
                    twice_allowed = False
                else:
                    return 0
            else:
                small_caves_visited.add(cave)
        return sum(paths(cave_map, cave2, small_caves_visited.copy(),
                         twice_allowed, depth + 1)
                   for cave2 in cave_map[cave]
                   if cave2 != "start")


def day12(infile):
    cave_map = {}
    with open(infile, "r") as file:
        for line in file.read().splitlines():
            k, v = line.split('-')
            if k in cave_map:
                cave_map[k].add(v)
            else:
                cave_map[k] = {v}
            if v in cave_map:
                cave_map[v].add(k)
            else:
                cave_map[v] = {k}

    print("Part One: ", paths(cave_map, "start", twice_allowed=False))
    print("Part One: ", paths(cave_map, "start", twice_allowed=True))
