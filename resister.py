def value(colors):
    for color in colors:
        color = color.lower()
        resister_value = []
        if color == "black":
            resister_value.append("0")
        elif color == "brown":
            resister_value.append("1")
        elif color == "red":
            resister_value.append("2")
        elif color == "orange":
            resister_value.append("3")
        elif color == "yellow":
            resister_value.append("4")
        elif color == "green":
            resister_value.append("5")
        elif color == "blue":
            resister_value.append("6")
        elif color == "violet":
            resister_value.append("7")
        elif color == "grey":
            resister_value.append("8")
        elif color == "white":
            resister_value.append("9")
        else:
            resister_value.append("")
    return "".join(resister_value)

value("brown", "black")