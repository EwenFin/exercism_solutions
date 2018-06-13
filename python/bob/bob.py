def hey(phrase):

    phrase_length = len(phrase.strip())
    phrase_numbers = any(char.isdigit() for char in phrase)

    if phrase_length == 0:
        return "Fine. Be that way!"

    elif phrase.upper() == phrase and ":)" not in phrase and not phrase_numbers:
        if phrase[phrase_length-1] == "?":
            return "Calm down, I know what I'm doing!"
        else:
            return "Whoa, chill out!"

    elif phrase_numbers:
        if phrase[phrase_length - 1] == "?":
            return "Sure."
        elif phrase[phrase_length - 1] == "!":
            return "Whoa, chill out!"
        else:
            return "Whatever."

    elif phrase[phrase_length-1] == "?":
        return "Sure."
    else:
        return "Whatever."
