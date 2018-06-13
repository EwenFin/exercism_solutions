import math

def sieve(limit):
    result = []
    if limit >= 2:
        result.append(2)
    for x in range(3, limit+1, 2):
        if is_prime(x):
            result.append(x)
    return result

def is_prime(n):
    i = 3
    while (i <= math.sqrt(n)):
        if (n % i == 0):
            return False
        i += 2
    return True