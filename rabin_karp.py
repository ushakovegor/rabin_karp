def toint(nucleobase):
    if nucleobase == 'A':
        return 0
    elif nucleobase == 'G':
        return 1
    elif nucleobase == 'C':
        return 2
    elif nucleobase == 'T':
        return 3
    else:
        raise ValueError("Check input nucleobases")


def get_hash(p, l):
    global A

    n = 0

    for i in range(l):
        n = n * A + toint(p[i])
    return n


def RabinKarp(t, p):
    global A

    A = 4
    len_t = len(t)
    len_p = len(p)
    M_hash = get_hash(p, len_p)
    N_hash = get_hash(t, len_p)
    n = A**(len(p) - 1)
    for i in range(len_t - len_p):
        if M_hash == N_hash:
            return i
        N_hash = (N_hash % n) * A + toint(t[len_p + i])
    return 'Not found'


def main():
    with open('inputs.txt', 'r') as inputs:
        t = inputs.readline().strip()
        p = inputs.readline().strip()
    print(RabinKarp(t, p))


if __name__ == '__main__':
    main()
