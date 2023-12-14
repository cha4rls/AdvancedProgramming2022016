# Read numbers from file and store them in a list
with open("numbers.txt", "r") as file:
    numbers_list = [int(line.strip()) for line in file]

# Output the values in integer format
for number in numbers_list:
    print(number)
