def is_triangle(side1, side2, side3):
    #If statement to check that the sides follow the triangle inequality
    if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
        return True
    else:
        return False

#Asks for user input for the lengths of the sides
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

#Verifies if the given lengths form a triangle
if is_triangle(side1, side2, side3):
    print("The given sides form a triangle.")

#Else, it doesn't form a triangle
else:
    print("The given sides do not form a triangle.")