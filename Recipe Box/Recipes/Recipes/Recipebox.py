import os
from pathlib import Path

def recipe_path():
    print("What type of recipe do you want?")
    print("Dessert, Meat, Pasta, Salad")
    type_recipe = input("Enter your choice: ")
    food_you_want = input("Type of food: ")
    return type_recipe, food_you_want

def open_path(a, b):
    base_dir = "F:\\Personal Files\\Recipe Box\\Recipes\\Recipes\\"
    file_path = Path(base_dir+a+"\\"+b+".txt")
    return file_path

def read_recipe(file_path):
    file = open(file_path, 'r')
    data = file.read()
    print(data)
    file.close()

def create_recipe():
    Type, food = recipe_path()
    new_path = open_path(Type, food)
    file = open(new_path, 'w')
    content = input("Enter the recipe: ")
    file.write(content)
    print("Your recipe has been recorded")
    file.close()

def create_category():
    type = input("Enter the type of category: ")
    path = open_path(type, "")
    os.makedirs(path)

def modify_recipe():
    n, m = recipe_path()
    path = open_path(n, m)
    file = open(path, 'a')
    data = input("Enter the modified recipe: ")
    file.write(data)
    print("The recipe has successfully been modified")
    file.close()

def delete_recipe():
    a, b = recipe_path()
    path = open_path(a,b)
    os.rmdir(path)
    print("Recipe deleted")

def delete_category():
    type = input("Enter the type of category: ")
    path = open_path(type, "")
    os.rmdir(path)
    print("Category deleted")

# main program
while True:
    print("Welcome to the recipe book")
    print("You can do the following to the recipe book:")
    print("1. Read a recipe")
    print("2. Create a recipe")
    print("3. Modify a recipe")
    print("4. Create a category")
    print("5. Delete a recipe")
    print("6. Delete a category")
    print("7. End the program")
    choice = int(input(("Your choice: ")))
    if choice==1:
        c, d = recipe_path()
        path = open_path(c, d)
        read_recipe(path)
    elif choice==2:
        create_recipe()
    elif choice==3:
        modify_recipe()
    elif choice==4:
        create_category()
    elif choice==5:
        delete_recipe()
    elif choice==6:
        delete_category()
    else:
        print("ending......")
        break
    os.system('cls')