num_1 = int(input("Please enter your first number: ")) #Gets first number
num_2 = int(input("Please enter your second number: ")) #Gets second number

if num_1 == 0 or num_2 == 0:
    sum = num_1 + num_2 #Calculates the sum of the two numbers
    diff = num_1 - num_2 #Calculates the difference of the two numbers
    prod = num_1 * num_2 #Calculates the product of the two numbers

    print("\n") #Adds a blank line for space
    print(f"The sum of {num_1} and {num_2} is {sum}") #Prints the two inputs of user and the sum
    print(f"The difference of {num_1} and {num_2} is {diff}") #Prints the two inputs of user and the difference
    print(f"The product of {num_1} and {num_2} is {prod}") #Prints the two inputs of user and the product
    print(f"The quotient of {num_1} and {num_2} is 0")
    print(f"The remainder of {num_1} and {num_2} is 0") #Prints the two inputs of user and the remainder

else: 
    sum = num_1 + num_2 #Calculates the sum of the two numbers
    diff = num_1 - num_2 #Calculates the difference of the two numbers
    prod = num_1 * num_2 #Calculates the product of the two numbers
    quot = num_1 / num_2 #Calculates the quotient of the two numbers
    rem = num_1 % num_2 #Calculates the remainder of the two numbers

    print("\n") #Adds a blank line for space
    print(f"The sum of {num_1} and {num_2} is {sum}") #Prints the two inputs of user and the sum
    print(f"The difference of {num_1} and {num_2} is {diff}") #Prints the two inputs of user and the difference
    print(f"The product of {num_1} and {num_2} is {prod}") #Prints the two inputs of user and the product
    print(f"The quotient of {num_1} and {num_2} is {quot}") #Prints the two inputs of user and the quotient
    print(f"The remainder of {num_1} and {num_2} is {rem}") #Prints the two inputs of user and the remainder