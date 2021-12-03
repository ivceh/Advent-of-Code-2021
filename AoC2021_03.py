def count_bits(A, i):
    cnt0 = cnt1 = 0
    for n in A:
        if n[i] == '0':
            cnt0 += 1
        elif n[i] == '1':
            cnt1 += 1
        else:
            raise ValueError("Bits must be either 0 or 1!")
    return cnt0, cnt1


def gamma_epsilon_rate(A):
    gamma = ""
    epsilon = ""
    for i in range(len(A[0])):
        cnt0, cnt1 = count_bits(A, i)
        if cnt0 > cnt1:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'
    return gamma, epsilon


def power_consumption(A):
    gamma, epsilon = gamma_epsilon_rate(A)
    return int(gamma, base=2) * int(epsilon, base=2)


def filter_by_bit_criteria(A, i, value):
    B = []
    for l in A:
        if l[i] == value:
            B.append(l)
    return B


# ox=True for oxygen generator rating, ox=False for CO2 scrubber rating
def gas_rating(A, ox):
    i = 0
    while len(A) > 1:
        cnt0, cnt1 = count_bits(A, i)
        A = filter_by_bit_criteria(A, i,
                                   '0'
                                   if (cnt0 > cnt1) == ox
                                   else '1')
        i += 1
    return A[0]


def life_support_rating(A):
    oxygen_generation_rating = gas_rating(A, ox=True)
    co2_scrubber_rating = gas_rating(A, ox=False)
    return (int(oxygen_generation_rating, base=2) *
            int(co2_scrubber_rating, base=2))


def day03(infile):
    A = []
    with open(infile, "r") as file:
        A = file.read().splitlines()

    # resolving Part One
    print("Part One: ", power_consumption(A))

    # resolving Part Two
    print("Part Two: ", life_support_rating(A))
