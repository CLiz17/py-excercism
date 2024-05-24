def is_valid(isbn):
    isbn = isbn.replace("-","").replace(" ", "")
    if len(isbn) != 10:
        return False
    
    sum = 0
    index = 10
    
    for char in isbn[:-1]:
        if not char.isdigit():
            return False
        sum += int(char) * index
        index -= 1
    
    if isbn[-1] == 'X':
        sum += 10
    elif isbn[-1].isdigit():
        sum += int(isbn[-1])
    else:
        return False
    
    return sum % 11 == 0