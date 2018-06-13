def detect_anagrams(word, candidates):

    chars1 = sorted(list(word.lower()))
    result = []

    for candidate in candidates:
        chars2 = sorted(list(candidate.lower()))
        if chars1 == chars2 and word.lower() != candidate.lower():
            result.append(candidate)

    return result
