# List - mutable, any datatype
fruits = ["apple","Banana"]
fruits.append("grapes") #add item to list

# Tuple - immutable, any datatype
fruits = ('apple', 'banana')

# Dictionary - key:value
names = {1:"cat", 2:'dog'}


# String Manipulations
sentence = "there is a cat"

sentence.title() #There is a cat

sentence.endswith("cat") #True

sentence.strip() #remove space

#remove char at beginning and end only 
print(sentence.strip("cat"))
# right only
print(sentence.rstrip("cat"))

sentence.replace("cat", "dog") #there was a dog

word = apple
sorted(word) #aelpp

raise ValueError()
raise IndexError()