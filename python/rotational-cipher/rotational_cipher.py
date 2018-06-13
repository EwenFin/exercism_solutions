def rotate(text, key):

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    char_list = []
    result = ""

    for char in alphabet:
        char_list.append(char)

    modified_alphabet = char_list[-key:] + char_list[:-key]

    for char in text:
        upper = False
        if char.isupper():
            char = char.lower()
            upper = True
        if char.isalpha():
            i = modified_alphabet.index(char)
            new_char = alphabet[i]
            if upper:
                result += new_char.upper()
            else:
                result += new_char
        else:
            result += char

    return result
