resistor_color = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4, "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9}

def label(colors):
    result = []
    for color in colors[:2]:
        result.append(str(resistor_color.get(color)))

    if result[0] == "0" and result[1] == "0":
        result = "0"
        power = 0
    elif result[0] != "0" and result[1] == "0":
        result = result[0]
        power = 1
    elif result[0] == "0" and result[1] != "0":
        result = result[1]
        power = 0
    else:
        power = 0
        
    power += resistor_color.get(colors[2])
    
    if power < 3:
        result = str(int(''.join(result))*(10**power)) + " ohms"
    elif power >= 3 and power < 6:
        power = power - 3
        result = str(int(''.join(result))*(10**power)) + " kiloohms"
    elif power >= 6 and power < 9:
        power = power - 6
        result = str(int(''.join(result))*(10**power)) + " megaohms"
    elif power >= 9 and power < 12:
        power = power - 9
        result = str(int(''.join(result))*(10**power)) + " gigaohms"

    return result