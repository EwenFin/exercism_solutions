import string

def is_pangram(sentence):

    alphabet_set = set(string.ascii_lowercase)
    input_set = set(sentence.lower())

    output = alphabet_set.intersection(input_set)

    if len(output) == 26:
        return True
    else:
        return False





