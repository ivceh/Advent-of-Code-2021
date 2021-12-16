import math
A = []
cnt = part1 = 0


def read_n_bits(n):
    global cnt
    cnt += n
    if cnt > len(A):
        raise RuntimeError("Not enough bits to read!")
    return int(A[cnt - n: cnt], base=2)


def operation(mtype, L):
    if mtype == 0:
        return sum(L)
    elif mtype == 1:
        return math.prod(L)
    elif mtype == 2:
        return min(L)
    elif mtype == 3:
        return max(L)
    else:
        a, b = L
        if mtype == 5:
            return a > b
        if mtype == 6:
            return a < b
        elif mtype == 7:
            return a == b
        else:
            raise ValueError("mtype must be valid operator!")


def read_literal_value():
    val = 0
    while read_n_bits(1) == 1:
        val = val * 16 + read_n_bits(4)
    val = val * 16 + read_n_bits(4)
    return val


def read_packet():
    global part1
    part1 += read_n_bits(3)
    mtype = read_n_bits(3)

    if mtype == 4:
        return read_literal_value()
    else:
        L = []
        if read_n_bits(1) == 0:
            sub_bits = read_n_bits(15)
            stop = cnt + sub_bits
            while cnt < stop:
                L.append(read_packet())
        else:
            num_packets = read_n_bits(11)
            for _ in range(num_packets):
                L.append(read_packet())
        return operation(mtype, L)


def day16(infile):
    global A

    with open(infile, "r") as file:
        s = file.readline().strip('\n')
        A = ""
        for d in s:
            # hex digit to 4 digit binary
            A += f'{int(d, base=16):04b}'

    part2 = read_packet()

    print("Part One: ", part1)
    print("Part Two: ", part2)
