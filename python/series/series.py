def slices(series, length):

    if length <= 0 or length > len(series):
        raise ValueError("invalid input")
    int(series)
    result = []
    digits = list(series)
    substring = ""
    while len(digits) >= length:
        for i in range(0, length):
            substring = substring + (digits[i])
        result.append(substring)
        del digits[0]
        substring = ""


    return result


