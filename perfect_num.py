def classify(number):
    asum = 0
    if number == 0 or number < 0:
        raise ValueError("Classification is only possible for positive integers.")
        
    for i in range(1, int(number/2 + 1)):
        if number%i == 0:
            asum += i

    if asum == number:
        return "perfect"
    elif asum > number:
        return "abundant"
    else:
        return "deficient"