def categories():
    print("Choices: ")
    print("'a' Normal math")
    print("'b' Misc.")

def misc_categories():
    print("Choices: ")
    print("'a' month calculator")

def choices():
    print("Choices:")
    print("'a' subtract")
    print("'b' divide")
    print("'c' multiply")
    print("'d' odd or even number")
    print("'e' perimeters")
    print("'f' addition")
    print("'g' averages")
    print("")
    print("Categories:")
    print("'1' for misc.")


categories()
category = str(input("Choose: "))
if category == "a":

    choices()
    choice = str(input("Choose: "))

#subtraction
    if choice == "a":
        a = int(input("1: "))
        b = int(input("2: "))
        c = a - b
        print(c)

#division
    elif choice == "b":
        a = int(input("1: "))
        b = int(input("2: "))
        c = a / b
        print(c)

#multiplication
    elif choice == "c":
        a = int(input("1: "))
        b = int(input("2: "))
        c = a * b
        print(c)

#odd or even number
    elif choice == "d":
        a = int(input("Number: "))
        if a % 2 == 0:
            print("The number",a,"is an even number")
        else:
            print("The number",a,"is an odd number")

#Perimeter
    elif choice == "e":
    
    #Choose perimeter shape
        print("Choices (for shapes):")
        print("'a' for squares")
        print("'b' for triangles")

        d = str(input("Shape: "))

    #square calculation
        if d == "a":
            a = int(input("Height: "))
            b = int(input("Width: "))
            d = (a * 2) + (b * 2)

    #triangle calculation
        elif d == "b":
            a = int(input("Length of first wall: "))
            b = int(input("Length of second wall: "))
            c = int(input("Length of third wall: "))
            d = a + b + c
    
    #answer
        print("Perimeter:",d)

#addition
    elif choice == "f":
        a = int(input("1: "))
        b = int(input("2: "))
        c = a + b
        print(c)

#averages
    elif choice == "g":

    #required
        amt = 0
        sum = 0.0
        num = 1

    #keep in mind
        print("Enter 0 to stop cycle")

    #the real math
        while num != 0:
            num = float(input("Enter number: "))
            if num != 0:
                amt = amt + 1
                sum = sum + num 
            if num == 0:
                print("Average:", sum / amt)
    
#misc
if category == "b":

    misc_categories()
    choices = str(input("Choose: "))
    if choices == "a":

            months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                    "November", "December"]
            month = int(input("Number of month: "))
            if 1 < month <= 12:
                print("The month is",months[month-1])
    else:
        quit()