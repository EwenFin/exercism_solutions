import string

def word_count(phrase):

    phrase = phrase.replace(',', " ").replace('_'," ").replace('.', " ").replace('-'," ")

    phrase = phrase.translate(None, string.punctuation.replace("'",""))

    words = phrase.lower().split()

    result = {}

    for word in words:
        if word[0] == "'":
            word = word[1:len(word) - 1]
        if word in result.keys():
            result[word] += 1
        else:
            result[word] = 1

    return result








