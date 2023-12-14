#Variable to count the loop
loop = 0

#While loop
while True:
    #Asks the user if they want to continue
    choice = input("Do you want to continue? (Y/N): ")

    #Adds 1 to the counter if it continues
    loop += 1

    #If statement if the user doesn't want to continue
    if choice.upper() != 'Y':
        break  #Break for loop

#Prints the number of times the loop was done
print(f"The loop was done {loop} times.")