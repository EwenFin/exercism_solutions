def abbreviate(words):

    words = words.upper()
    acronym = words[0]
    for num, char in enumerate(words):
        if not char.isalpha() :
            acronym += words[num+1]

    return acronym.replace(" ","")