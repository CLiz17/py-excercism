def rotate(text, key):
    small = "abcdefghijklmnopqrstuvwxyz"
    captial = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    result = []
    for char in text:
        if char in small:
            new_index = (small.index(char)+key)%26
            result.append(small[new_index])
        elif char in captial:
            new_index = (captial.index(char)+key)%26
            result.append(captial[new_index])
        else:
            result.append(char)

    return "".join(result)