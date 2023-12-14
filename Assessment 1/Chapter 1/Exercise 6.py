#For loop counts the range from 1 to 100
for num in range(1, 101):

    #If number is divisible by 3 and 5
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")

    #If number is divisible by 3 only
    elif num % 3 == 0:
        print("Fizz")

    #If number is divisible by 5 only
    elif num % 5 == 0:
        print("Buzz")

    #Otherwise, print the number only
    else:
        print(num)