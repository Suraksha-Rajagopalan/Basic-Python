print("                WELCOME TO THE PYCALULATOR")
print("\n\n")
print("                The operations you can perform are:")
print("1 for addition")
print("2 for subtraction")
print("3 for multiplication")
print("4 for division")
print("5 for floor division")
print("6 for modulus")
print("7 for power")
print("8 for rounding off")
print("9 for exit\n\n")
choice = int(input("Enter your choice: "))
while True:
    if choice in [1,2,3,4,5,6]:
        a = int(input("Enter your first number: "))
        b = int(input("Enter your second number: "))
        if choice==1:
            print(f"The sum of two numbers is {a+b}")
        elif choice==2:
            print(f"The difference between the two numbers is {a-b}")
        elif choice==3:
            print(f"The product of the two numbers is {a*b}")
        elif choice==4:
            print(f"The division of the two numbers is {a/b}")
        elif choice==5:
            print(f"The floor division of the two numbers is {a//b}")
        else:
            print(f"The modulus of the two numbers is {a%b}")
    elif choice==7:
        base = int(input("Enter the base of the number: "))
        power = int(input("Enter the power required: "))
        print(f"The result of {base}^{power} is {base**power}")
    elif choice==8:
        num = float(input("The rounding off number is: "))
        digits = int(input("The number of digits the rounding off must take place is: "))
        print(f"The rounded number is {round(num, digits)}")
    elif choice==9:
        print("Happy CAL DAY!!!   :)")
        break;
    else:
        print("Enter a valid choice :(")
    choice = int(input("Enter your choice: "))
