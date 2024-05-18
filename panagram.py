def is_pangram(sentence):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for a in alpha:
        if a not in sentence.lower():
            return False
    return True