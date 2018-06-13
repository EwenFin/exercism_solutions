def distance(strand_a, strand_b):

    if len(strand_a) != len(strand_b):
        raise ValueError("length of strands does not match")

    hamming = 0

    for i, char in enumerate(strand_a, start=0):
        if strand_a[i] != strand_b[i]:
            hamming += 1

    return hamming
