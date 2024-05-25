def value(colors):
    rvalue = [] 
    for color in colors[0:2]: 
        color = color.lower()
        if color == "black":
            rvalue.append("0")
        elif color == "brown":
            rvalue.append("1")
        elif color == "red":
            rvalue.append("2")
        elif color == "orange":
            rvalue.append("3")
        elif color == "yellow":
            rvalue.append("4")
        elif color == "green":
            rvalue.append("5")
        elif color == "blue":
            rvalue.append("6")
        elif color == "violet":
            rvalue.append("7")
        elif color == "grey":
            rvalue.append("8")
        elif color == "white":
            rvalue.append("9")
        else:
            rvalue.append("")  
    return int("".join(rvalue))