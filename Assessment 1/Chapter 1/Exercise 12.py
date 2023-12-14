import math

#A function to calculate for the area of square
def area_of_square():
    side_length = float(input("Enter the side length of the square: "))
    area = side_length ** 2
    print(f"------The area of the square is: {area}------")

#A function to calculate for the area of circle
def area_of_circle():
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * radius ** 2
    print(f"------The area of the circle is: {area:.2f}------")

#A function to calculate for the area of triangle
def area_of_triangle():
    base = float(input("Enter the base length of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print(f"------The area of the triangle is: {area}------")

#A display the menu
while True:
    print("\nMenu:")
    print("1: Calculate the area of a square")
    print("2: Calculate the area of a circle")
    print("3: Calculate the area of a triangle")
    print("4: Exit")

    #Gets the choice of the user
    choice = input("Enter your choice (1, 2, 3, or 4 to exit): ")

    #Performs the chosen operation or exits the program
    if choice == "1":
        area_of_square()
    elif choice == "2":
        area_of_circle()
    elif choice == "3":
        area_of_triangle()
    elif choice == "4":
        print("------Goodbye!------")
        break
    else:
        print("------Invalid! Please choose between 1, 2, 3, or 4------")