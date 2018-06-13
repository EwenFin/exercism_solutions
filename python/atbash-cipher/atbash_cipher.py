import string

def encode(plain_text):

    plain_text = plain_text.lower().translate(None, string.punctuation)

    result = atbash(plain_text)

    result = " ".join(result[i:i+5] for i in range(0, len(result),5))

    return result


def decode(ciphered_text):

    return atbash(ciphered_text)


def atbash(string):

    string.replace(" ", "")
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    reversed_alphabet = "zyxwvutsrqponmlkjihgfedcba"
    result = ""

    for num, char in enumerate(string):

        if char.isdigit():
            result += char

        if char.isalpha():
            i = alphabet.index(char)
            result += reversed_alphabet[i]

    return result



