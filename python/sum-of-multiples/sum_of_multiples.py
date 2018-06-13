
def sum_of_multiples(limit, multiples):

    multiple_set = set()

    for i in range(0, limit):
        for num in multiples:
            if i % num == 0:
                multiple_set.add(i)

    return sum(multiple_set)