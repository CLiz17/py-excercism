# def reverse(text):
#     length = len(text)
#     reverse_str = []
#     for char in text:
#         new_index = length - text.index(char)
#         reverse_str.append(text[new_index])

#     return "".join(reverse_str)

# reverse("cat")

def reverse(text):
    return text[::-1]