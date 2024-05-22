def find_anagrams(word, candidates):
    index = sorted(word.lower())
    anagram = []
    for candidate in candidates:
        target = sorted(candidate.lower())
        if target == index and candidate.lower() != word.lower():
            anagram.append(candidate)

    return anagram