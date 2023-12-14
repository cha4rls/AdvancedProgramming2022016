#List with 10 values
int_list = [3, 9, 18, 20, 8, 22, 17, 15, 7, 30]

print("List:")
#Prints list with for loop
for number in int_list:
    print(number, end=" ")

#Prints number with highest and lowest value
print(f"\nThe highest number in the list is {max(int_list)}!")
print(f"The lowest number in the list is {min(int_list)}!")

#Sorts the list from lowest to highest
int_list.sort()
print(f"\nList of numbers in ascending order: {int_list}")

#Sorts the list from highest to lowest
int_list.sort(reverse=True)
print(f"\nList of numbers in descending order: {int_list}")

#Adds two elements in the list
int_list.append(39)
int_list.append(820)

#Prints the list with appended elements
print("\nNew list: ")
for number in int_list:
    print(number, end=" ")