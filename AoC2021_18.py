import ast, copy


def magnitude(L):
    if type(L) == int:
        return L
    else:
        a, b = L
        return 3 * magnitude(a) + 2 * magnitude(b)


def check_explode(L, depth = 0):
    if depth < 4:
        if type(L) == int:
            return False
        else:
            return check_explode_inner(L, depth)
    else:
        if type(L) == int:
            return False
        else:
            a, b = L
            if type(a) == int and type(b) == int:
                return True, a, b, True
                # True, left, right, first level over
            else:
                return check_explode_inner(L, depth)


def check_explode_inner(L, depth):
    a, b = L
    res = check_explode(a, depth + 1)
    if res:
        _, l, r, f = res
        if f:
            L[0] = 0
        L[1] = L_increase_first(L[1], r)
        return True, l, None, False
    else:
        res = check_explode(b, depth + 1)
        if res:
            _, l, r, f = res
            if f:
                L[1] = 0
            L[0] = L_increase_last(L[0], l)
            return True, None, r, False
        else:
            return False


def L_increase_first(L, a):
    if a is None:
        return L
    elif type(L) == int:
        return L + a
    else:
        L[0] = L_increase_first(L[0], a)
        return L


def L_increase_last(L, a):
    if a is None:
        return L
    elif type(L) == int:
        return L + a
    else:
        L[-1] = L_increase_last(L[-1], a)
        return L


def check_split(L):
    if type(L) == int:
        if L >= 10:
            return True, [L // 2, (L + 1) // 2]
        else:
            return False, L
    else:
        b, L[0] = check_split(L[0])
        if b:
            return True, L
        else:
            b, L[1] = check_split(L[1])
            return b, L


def reduce(L):
    b = True
    while b:
        if check_explode(L):
            b = True
        else:
            b, L = check_split(L)
    return L


def add(A):
    sol = A[0]
    for i in range(1, len(A)):
        sol = reduce([sol, A[i]])
    return sol


def day18(infile):
    global A
    with open(infile, "r") as file:
        A = [ast.literal_eval(line) for line in file.read().splitlines()]

    print("Part One: ", magnitude(add(copy.deepcopy(A))))
    print("Part Two: ",
          max(magnitude(add([copy.deepcopy(a), copy.deepcopy(b)]))
              for a in A
              for b in A))
