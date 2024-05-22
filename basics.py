# List
fruits = ["apple","Banana"]

# Tuple
fruits = ('apple', 'banana')

# Set
fruits = {'apple', 'banana'}

# Dictionary
names = {1:"cat", 2:'dog'}

########
# String Manipulations
sentence = "there was a cat"

sentence.title() #There was a cat

sentence.endswith("cat") #True

sentence.strip() #removes spaces

print(sentence.strip("cat")) #here was a

sentence = "there was a cat."
sentence.rstrip('.') # sentence = "there was a cat"

sentence.replace("cat", "dog") #there was a dog