import random

print("##############################################################################")
print("\t\t\tWELCOME TO GAME HUB")
print("\t\t\tTODAY'S GAME IS GUESS THE NUMBER")
print("\t\t\tHOPE UR LUCK FAVORS U TODAY :)")
print("##############################################################################")

print("\n\n")
name = input("Enter your name: ")

real_number = random.randint(1, 100)
for i in range(1,9):
    guessed_number = int(input("Guess the number: "))
    if guessed_number>100 or guessed_number<1:
        print("The entered integer is not upto the given range.....")
        print("The range is (-15, 254), try again :)")
    else:
        if guessed_number < real_number:
            print("The guessed number is smaller than the original number  :(")
        elif guessed_number > real_number:
            print("The guessed number is larger than the original number   :(")
        else:
            print("Wow!! U guessed it right! Congratulations    :)")
            print(f"U guessed it right in your {i} attempt")
            break
print("WE ARE DONE FOR TODAY PAL")
print(f"{name} see you next time bye!!!")
