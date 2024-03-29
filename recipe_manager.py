import os
from pathlib import Path
import time, string

def create_recipe_folder(*args):
    pass

def choose_menu_option(recipes_folder ):
    """
        Display the Menu for the recipe Manager and Let the user choose a Menu option
    """
    clear_screen()
    print("=" * 100)
    print("\t\t\t\t\tWELCOME TO THE RECIPE MANAGER\n")
    print("=" * 100)
    print("\n")
    print(f"The recipes are in: {recipes_folder}\n")
    total_recipes = [recipe for recipe in recipes_folder.glob('**/*.txt')]
    print(f"You currently have {len(total_recipes)} Recipes\n")

    menu_choice = 'x'
    while not menu_choice.isnumeric() or int(menu_choice) not in range(1,7):
        print(f"\n{'=' * 10}Menu{'=' * 10}")
        print("[1] - Read Recipe\n")
        print("[2] - Create recipe\n")
        print("[3] - Create category\n")
        print("[4] - Delete Recipe\n")
        print("[5] - Delete Category\n")
        print("[6] - End Program\n")
        print("=" * 27)
        menu_choice = input("Please choose a Menu Option between 1-6:  ")
    return int(menu_choice)

def show_categories(recipes_folder):
    categories = [category for category in recipes_folder.iterdir() if category.is_dir()]
    print(f"\nThese are our current categories :\n")
    for i, c in enumerate(categories):
        print(f"{i+1}. {c.name}")
    return categories

def choose_category(category_list):
    """
        Choose a category from the list of categories
    """
    category_choice = 'x'
    while not category_choice.isnumeric() or int(category_choice) not in range(1, len(category_list) + 1):
        category_choice = input("\nChoose a category: ")
    return category_list[int(category_choice) - 1]

def show_recipes(category_path):
    recipes_path = Path(category_path)
    recipes = [recipe for recipe in recipes_path.iterdir() if recipe.is_file()]
    print(f"\nThese are our current recipes in the {category_path.name} category :\n")
    for i, r in enumerate(recipes):
        print(f"{i+1}. {r.name}")
    return recipes

def choose_recipe(recipe_list):
    """
        Choose a category from the list of categories
    """
    recipe_choice = 'x'
    while not recipe_choice.isnumeric() or int(recipe_choice) not in range(1, len(recipe_list) + 1):
        recipe_choice = input("\nChoose a recipe: ")
    return recipe_list[int(recipe_choice) - 1]


def read_recipe(recipe):
    """
        Read a recipe content from a specific category
    """
    print(Path.read_text(recipe))

def create_recipe(category_path):
    """
        Create a recipe content in a specific category
    """
    print(f"Write the name of your new {category_path.name} recipe: \n")
    recipe_name = input()
    recipe_path = Path(category_path, recipe_name + '.txt')
    if recipe_path.is_file():
        print(f"Sorry, recipe {recipe_name} already exist")
    else:
        recipe_content = input("Write your new recipe: \n")
        with recipe_path.open(mode='w') as file:
            file.write(recipe_content)
        #Path.write_text(recipe_path, recipe_content)
        print(f"Your recipe {recipe_name}.txt has been created")

def create_category(recipes_folder):
    """
        Create a Recipe Category in the Recipes' Folder
    """

    category_name = input("Write the name of the new category: ")
    category_path = Path(recipes_folder, category_name)
    if not category_path.exists():
        category_path.mkdir(parents=True)
        print(f"Your new category {category_name} has been created")
    else:
        print(f"Category '{category_path}' already exits")

def delete_recipe(recipe):
    """
        Delete a Recipe file from a Category 
    """
    Path(recipe).unlink()
    print(f"The recipe {recipe.name} has been deleted")

def delete_category(category):
    """
        Delete a Category of Recipe from the Recipes' Folder
    """
    Path(category).rmdir()
    print(f"The {category.name} has been deleted")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def return_to_menu():
    return_choice = 'x'
    while return_choice.lower() != 'b':
        return_choice = input("\nPress 'b' to return to the menu: ")


def main():
    base = Path.home()
    recipes_folder = Path(base, 'Recipes')
    
    manage_recipe = True
    while manage_recipe:
        menu_option = choose_menu_option(recipes_folder)
        match menu_option:
            case 1:
                category_list = show_categories(recipes_folder)
                category = choose_category(category_list)
                recipe_list = show_recipes(category)
                if len(recipe_list) < 1:
                    print(f"There is no recipes in the {category.name} category")
                else:
                    recipe = choose_recipe(recipe_list)
                    read_recipe(recipe)
                return_to_menu()
            case 2 :
                category_list = show_categories(recipes_folder)
                category = choose_category(category_list)
                create_recipe(category)
                return_to_menu()
            case 3: 
                create_category(recipes_folder)
                return_to_menu()
            case 4:
                category_list = show_categories(recipes_folder)
                category = choose_category(category_list)
                recipe_list = show_recipes(category)
                if len(recipe_list) < 1:
                    print(f"There is no recipes in the {category.name} category")
                else:
                    recipe = choose_recipe(recipe_list)
                    delete_recipe(recipe)
                return_to_menu()
            case 5:
                category_list = show_categories(recipes_folder)
                category = choose_category(category_list)
                delete_category(category)
                return_to_menu()
            case 6:
                    manage_recipe = False

if __name__ == '__main__':
    main()