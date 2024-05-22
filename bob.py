def response(hey_bob):
    hey = hey_bob.strip()
    if hey.endswith("?") and hey.isupper():
        return "Calm down, I know what I'm doing!" 
    elif hey.endswith("?"):
        return "Sure."
    elif hey.isupper():
        return "Whoa, chill out!"
    elif hey == "":
        return "Fine. Be that way!"
    else:
        return "Whatever."