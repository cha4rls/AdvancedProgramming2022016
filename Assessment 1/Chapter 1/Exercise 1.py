print("Good day, user!") #Introduction
name = str(input("Please input your name:\n")) #Gets name of the user
age = int(input("Please enter your age:\n")) #Gets age of the user

name_length = len(name) #Counts the length of the variable
proper_name = name.title() #Capitalizes the first letter of the words
print(f"It's nice to meet you, {proper_name}!") #Prints the variable proper_name
print(f"The length of your name is {name_length}.") #Prints the counted length of the variable

age_next = age + 1 #Adds one to the given age
print(f"You will turn {age_next} next year.") #Prints the variable age_next