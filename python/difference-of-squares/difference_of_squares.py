
def square_of_sum(count):
    result = 0
    for num in range(count+1):
        result += num
    result = result * result
    return result


def sum_of_squares(count):
    result = 0
    for num in range(count+1):
        result += num * num
    return result

def difference(count):
    return square_of_sum(count) - sum_of_squares(count)
