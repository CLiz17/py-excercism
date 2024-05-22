def is_armstrong_number(number):
    num = number
    sum = 0
    length = len(str(number))
    if length == 1:
        return True  
    while number != 0:
        last_digit = number%10
        number = number//10
        sum = sum + (last_digit**length)
        
    return sum == num