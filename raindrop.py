def convert(number):
    s = ""
    if number%3 == 0:
      s += "Pling"
        
    if number%5 == 0:
      s += "Plang"
        
    if number%7 == 0:
      s += "Plong"

    if number%3 != 0 and number%5 != 0 and number%7 != 0:
        s += str(number)

    return s