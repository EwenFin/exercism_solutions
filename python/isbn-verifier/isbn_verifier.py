def verify(isbn):

    isbn = isbn.replace("-","")
    list = []

    if len(isbn) != 10:
            return False

    for isbn_index, char in enumerate (isbn, start=0):
        if isbn_index < 9:
            try:
                list.append(int(char))
            except ValueError:
                return False
        elif isbn_index == 9:
            if char == "X":
                list.append(10)
            else:
                try:
                    list.append(int(char))
                except ValueError:
                    return False
        else:
            return False


    total = 0

    for modifier, i in enumerate(list, start=0):
        total += i * (10 - modifier)


    return total % 11 == 0







