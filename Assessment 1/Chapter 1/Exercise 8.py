#Indicates the number of rows
rows = 5

#Nested loop to display the pattern
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()