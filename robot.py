import random

class Robot:
    def __init__(self):
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        letter1 = random.choice(letters)
        letter2 = random.choice(letters)
        numbers = random.randint(1, 999)
        self.name = letter1 + letter2 + str(numbers)

    def reset(self):
        random.seed(5)
        
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        letter1 = random.choice(letters)
        letter2 = random.choice(letters)
        numbers = random.randint(1, 999)
        self.name = letter1 + letter2 + str(numbers)