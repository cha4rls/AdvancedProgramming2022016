def calculate_product(input_list):
    product = 1
    for value in input_list:
        product *= value
    return product

numbers = [3, 9, 21, 20, 18]

#Calls the function and store the result
result = calculate_product(numbers)

#Displays the result
print(f"The product of the numbers {numbers} is: {result}")