

def decode(string):

    result = ''
    count = ''

    for index, char in enumerate(string):
        if char.isdigit():
            count += char
        else:
            if count:
                result += int(count) * char
            else:
                result += char
            count = ''

    return result


def encode(string):

    if string == "":
        return ""

    current = string[0]
    count = 0
    result = ''

    for index, char in enumerate(string):
        if current == char:
            count += 1
        else:
            if count == 1:
                result += current
            else:
                result += str(count) + current
            current = char
            count = 1

    if count == 1:
        result += current
    else:
        result += str(count) + current

    return result










































