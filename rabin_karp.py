def toint(nucleobase):
    '''
    A - Adenine
    G - Guanine
    C - Cytosine
    T - Thymine

    return number for each nucleobase or rise ValueError
    '''
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


def get_hash(p, l, r):
    '''
    A - base of n-number system
    l - left border
    r - right border (not included)
    n - hash

    return hash of slice of string
    '''
    global A

    n = 0
    for i in range(l, r):
        n = n * A + toint(p[i])
    return n


def RabinKarp(t, p):
    '''
    A - base of n-number system
    N_hash - hash of slice of the main string
    M_hash - hash of the substring

    return index from which substring starting in the main string
    or 'Not found' if the substring is not found in the main string
    '''
    global A

    A = 4
    len_t = len(t)
    len_p = len(p)
    if len_t <= 0 or len_p <= 0:
        raise ValueError("Check input nucleobases")
    elif len_t < len_p:
        raise ValueError("Check input nucleobases")
    M_hash = get_hash(p, 0, len_p)
    for i in range(len_t - len_p + 1):
        N_hash = get_hash(t, i, len_p + i)
        if M_hash == N_hash:
            return i
        #N_hash = (N_hash % n) * A + toint(t[len_p + i])
    return 'Not found'


def main():
    '''
    t - the main string
    p - the substring which we should find in the main string
    '''
    with open('inputs.txt', 'r') as inputs:
        t = inputs.readline().strip()
        p = inputs.readline().strip()
    print(RabinKarp(t, p))


if __name__ == '__main__':
    main()
