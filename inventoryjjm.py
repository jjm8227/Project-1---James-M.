import csv

# Load food items into the 'food_items' list from the CSV file
food_items = []
with open('items_food.csv') as food_file:
    food_reader = csv.reader(food_file)
    for item in food_reader:
        food_items.append(item[0])

# Load beverage items into the 'beverages_items' list from the CSV file
beverages_items = []
with open('items_beverages.csv') as beverages_file:
    beverages_reader = csv.reader(beverages_file)
    for item in beverages_reader:
        beverages_items.append(item[0])

class InventoryManager:  # Ensure this is the correct class name
    def __init__(self):
        print("Inventory Management System Initialized")

    # Method to add new item to a category
    def add_new_item(self, item, category):
        if category == 'Beverages' and item not in beverages_items:
            beverages_items.append(item)
        elif category == 'Foods' and item not in food_items:
            food_items.append(item)
        else:
            print("Item is already in the selected category.")

    # Method to remove an item from a category
    def remove_existing_item(self, item, category):
        if category == 'Beverages' and item in beverages_items:
            beverages_items.remove(item)
        elif category == 'Foods' and item in food_items:
            food_items.remove(item)
        else:
            print("Item not found in the selected category.")

    # Method to display all items in categories
    def display_items(self):
        print(f"Food Items: {food_items}")
        print(f"Beverage Items: {beverages_items}")

    # Method to update category (for advanced uses, not frequently needed)
    def update_category(self, category):
        catagory = []
        return catagory

class MenuItem(InventoryManager):  # This is inheriting from Inventory
    __item_name = ""
    __item_category = None
    __item_expiry_date = None

    def __init__(self):
        pass

    def set_item_name(self, name):
        self.__item_name = name
        return self.__item_name

    def set_item_category(self, category):
        self.__item_category = category

    def set_item_expiry(self, expiry_date):
        self.__item_expiry_date = expiry_date
        return self.__item_expiry_date

    def show_item_details(self):
        print(f"Item Name: {self.__item_name}")
        print(f"Category: {self.__item_category}")
        print(f"Expiry Date: {self.__item_expiry_date}")

menu_item = MenuItem()

class Report(InventoryManager):  # This is inheriting from Inventory
    def __init__(self):
        pass

    # Method to check the number of items in a category
    def check_item_count(self, category):
        if category == 'Foods':
            count = len(food_items)
        elif category == 'Beverages':
            count = len(beverages_items)
        print(f"There are {count} items in the '{category}' category.")
        print("You may add or remove items as needed.")

    # Method to list all recipes from the recipes file
    def list_recipes(self):
        recipes = []
        try:
            with open('recipes.csv') as recipes_file:
                recipes_reader = csv.reader(recipes_file)
                for recipe in recipes_reader:
                    recipes.append(recipe[0])
            print(f"Available Recipes: {recipes}")
        except FileNotFoundError:
            print("Recipes file not found!")

    # Method to create a new recipe using available items
    def add_new_recipe(self, recipe_name, items_list):
        print(f"Creating a new recipe: {recipe_name}")
        print(f"The ingredients for your new recipe are: {items_list}")
