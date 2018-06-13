def is_armstrong(number):

    num_list = [int(num) for num in str(number)]
    order_magnitude = len(num_list)
    total = 0

    for num in num_list:
        powers = pow(num, order_magnitude)
        total += powers

    if total == number:
        return True
    else:
        return False