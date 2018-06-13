def is_isogram(string):

    isogram_set = set()

    string_modified = string.lower().replace(" ", "").replace("-","")

    for character in string_modified:

        if character in isogram_set:

            return False

        isogram_set.add(character)

    return True

