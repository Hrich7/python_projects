import os
from pathlib import Path
import time, string

# Create a folder called "Recipes" in the base folder of the computer
# Welcome greeting
# The recipes are in --> Path to recipes folder
# You have [x] recipies (Check folders and subfolders)
# Display the Menu (inside a while loop)

#   [1] - Read Recipe
    # > Choose Category
    # > show Recipes
    # > choose Recipe
    # > Show the content of that recipe

#   [2] - Create recipe
    # > Choose Category
    # > Create name of recipe
    # > Create content of recipe

#   [3] - Create category
    # > Category name
    # > Create Category ==> Generate a brand new folder

#   [4] - Delete Recipe
    # > Choose Category
    # > show Recipes
    # > choose Recipe
    # > Delete recipe (delete file?)

#   [5] - Delete Category
    # > choose Category
    # > delete category ==> Delete folder with contents

#   [6] - End Program
    # > End the program


#          Menu  
#   [1] - Read Recipe
#   [2] - Create recipe
#   [3] - Create category
#   [4] - Delete Recipe
#   [5] - Delete Category
#   [6] - End Program



def create_recipe_folder(*args):
    pass

def display_menu():
    """
        Display the Menu for the recipe Manager
    """
    print(f"\n{'=' * 10}Menu{'=' * 10}")
    print("[1] - Read Recipe\n")
    print("[2] - Create recipe\n")
    print("[3] - Create category\n")
    print("[4] - Delete Recipe\n")
    print("[5] - Delete Category\n")
    print("[6] - End Program\n")
    print("=" * 27)

def choose_category(recipes_folder):
    """
        Choose a Recipe category from the list of categories in the Recipe folder
    """
    categories = [category.name for category in recipes_folder.iterdir() if category.is_dir()]
    number_of_categories = len(categories)
    while True:
        print(f"These are our current categories :\n")
        for i, c in enumerate(categories):
            print(f"{i+1}. {c}")

        category = input(f'Choose Category as a number between 1 - {number_of_categories}: ')

        if category in string.digits:
            category = int(category)
            if category <= number_of_categories:
                return categories[category - 1]
            else:
                print("\nWrong input!\n")
        else:
            print("You need to enter a number from the following to choose the category")


def read_recipe(recipes_folder,category):
    """
        Read a recipe content from a specific category
    """
    category_path = Path(recipes_folder, category)
    recipes = [recipe for recipe in category_path.iterdir() if recipe.is_file()]
    number_of_recipes = len(recipes)
    print(f"List of Current Recipes in {category}: ")
    for i, recipe in enumerate(recipes):
        print(f"\t{i+1}. {recipe.stem}")
    if number_of_recipes == 0:
        print(f"There are curently no recipes in the {category} category")
    else:
        choice_of_recipe = int(input(f"\nChoose the recipe number you want to read: (1 - {number_of_recipes}): "))
        while choice_of_recipe > number_of_recipes or choice_of_recipe <= 0:
            print("Invalid choice!\n")
            choice_of_recipe = int(input(f"\nChoose the recipe number you want to read: (1 - {number_of_recipes}): "))

        with open(recipes[choice_of_recipe - 1]) as f:
            print(f.read())

def create_recipe(recipes_folder,category):
    """
        Create a recipe content in a specific category
    """

    recipe_path = Path(recipes_folder, category)
    print(f"You want to create a recipe in the {category} category\n")
    recipe_name = input("What is your recipe name: ")
    recipe_content = input (f"What is the content of the {recipe_name} recipe: ")
    with Path(recipe_path, recipe_name +'.txt').open(mode='a') as f:
        f.write(recipe_content)

def create_category(recipes_folder):
    """
        Create a Recipe Category in the Recipes' Folder
    """

    category = input("What is the name of the category you want to create: ")
    category_path = Path(recipes_folder, category)
    if not category_path.exists():
        category_path.mkdir(parents=True)
    else:
        print(f"Category '{category_path}' already exits")

def delete_recipe(recipes_folder,category):
    """
        Delete a Recipe file from a Category 
    """

    category_path = Path(recipes_folder, category)
    print(f"You want to delete a recipe in the {category} category\n")
    recipes_in_category = [recipe for recipe in category_path.iterdir() if recipe.is_file()]
    number_of_recipes = len(recipes_in_category)
    print(f"List of Current Recipes in {category}: ")
    for i, recipe in enumerate(recipes_in_category):
        print(f"\t{i+1}. {recipe.stem}")
    if number_of_recipes == 0:
        print(f"There are curently no recipes in the {category} category")
    else:
        if number_of_recipes == 1:
            recipe_number = int(input("Choose the recipe number you want to delete: (1) "))
        else :
            recipe_number = int(input(f"Choose the recipe number you want to delete: (1 - {number_of_recipes}): "))
        print(f"Deleting the recipe for {recipes_in_category[recipe_number - 1].stem} ...")
        recipes_in_category[recipe_number - 1].unlink()

def delete_category(recipes_folder, category):
    """
        Delete a Category of Recipe from the Recipes' Folder
    """

    category_path = Path(recipes_folder, category)
    print(f"removing the {category_path.name} recipe category...")
    time.sleep(2)
    category_path.rmdir()
    

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()
    print("=" * 100)
    print("\t\t\t\t\tWELCOME TO THE RECIPE MANAGER\n")
    print("=" * 100)
    print("\n")

    base = Path.home()
    recipes_folder = Path(base, 'Recipes')
    print(f"The recipes are in: {recipes_folder}\n")
    total_recipes = [recipe for recipe in recipes_folder.glob('**/*.txt')]
    print(f"You currently have {len(total_recipes)} in the Recipes folder\n")
    time.sleep(3)
    
    manage_recipy = True
    while manage_recipy:
        clear_screen()
        print("\t\t\t\t\t\tRECIPE MANAGER\n")
        display_menu()
        menu_option = int(input("Please choose a Menu Option between 1-6:  "))
        match menu_option:
            case 1:
                category = choose_category(recipes_folder)
                read_recipe(recipes_folder,category)
                time.sleep(3)
            case 2 :
                category = choose_category(recipes_folder)
                create_recipe(recipes_folder,category)
            case 3: 
                create_category(recipes_folder)
            case 4:
                category = choose_category(recipes_folder)
                delete_recipe(recipes_folder,category)
                time.sleep(3)
            case 5:
                category = choose_category(recipes_folder)
                delete_category(recipes_folder, category)
                time.sleep(3)
            case 6:
                    manage_recipy = False
            case _:
                print("Wrong input for the menu option. Please try again")
                time.sleep(2)

if __name__ == '__main__':
    main()