import csv

food_category = []
with open('items_food.csv') as csv_food:
    csv_reader_food = csv.reader(csv_food)
    for line in csv_reader_food:
        food_category.append(line[0])

beverages_category = []
with open('items_beverages.csv') as csv_beverages:
    csv_reader_beverages = csv.reader(csv_beverages)
    for line in csv_reader_beverages:
        beverages_category.append(line[0])

class Inventory:
    def __init__(self):
        print("Welcome to the Inventory System!")
    
    def add_item(self, item, category):
        if category == 'Beverages' and item not in beverages_category:
            beverages_category.append(item)
        elif category == 'Foods' and item not in food_category:
            food_category.append(item)
        else:
            print(f"Item '{item}' already exists in the {category} category.")
    
    def remove_item(self, item, category):
        if category == 'Beverages' and item in beverages_category:
            beverages_category.remove(item)
        elif category == 'Foods' and item in food_category:
            food_category.remove(item)
        else:
            print(f"Item '{item}' not found in the {category} category.")
    
    def list_items(self):
        print(f"\n--- Inventory List ---")
        print(f"Foods: {food_category}")
        print(f"Beverages: {beverages_category}")
    
    def update_inventory(self, category):
        if category == 'Foods':
            return food_category
        elif category == 'Beverages':
            return beverages_category

class Item:
    def __init__(self, name="", category=None, expiration_date=None):
        self.__name = name
        self.__category = category
        self.__expiration_date = expiration_date
    
    def set_name(self, name):
        self.__name = name
        return self.__name

    def set_category(self, category):
        self.__category = category
        return self.__category

    def set_expiry(self, date):
        self.__expiration_date = date
        return self.__expiration_date

    def get_details(self):
        print(f"Item: {self.__name}")
        print(f"Category: {self.__category}")
        print(f"Expiration Date: {self.__expiration_date}")

class Report(Inventory):
    def __init__(self):
        super().__init__()

    def items_in(self, category):
        if category == 'Foods':
            length_of_items = len(food_category)
        elif category == 'Beverages':
            length_of_items = len(beverages_category)
        else:
            print(f"Category '{category}' is invalid!")
            return
        print(f"There are currently {length_of_items} items in the '{category}' category.\n")
        print("You can add or remove more to your own liking.")

    def recipes(self):
        list_of_recipes = []
        try:
            with open('recipes.csv') as csv_recipes:
                csv_reader_recipes = csv.reader(csv_recipes)
                for line in csv_reader_recipes:
                    list_of_recipes.append(line[0])
            print(f"\n--- Recipes in Inventory ---")
            print(list_of_recipes)
        except FileNotFoundError:
            print("Recipes file not found. Please make sure the 'recipes.csv' file exists.")

    def create_new_recipe(self, name, items):

        print(f"\nCreating a new recipe '{name}'!")
        print(f"This recipe includes the following items from the inventory: {items}")
        with open('recipes.csv', mode='a', newline='') as csv_recipes:
            csv_writer = csv.writer(csv_recipes)
            csv_writer.writerow([name, *items])
        print(f"Recipe '{name}' has been added!")

inventory_system = Inventory()

inventory_system.add_item('Apple', 'Foods')
inventory_system.add_item('Coke', 'Beverages')
inventory_system.remove_item('Coke', 'Beverages')

inventory_system.list_items()

item1 = Item("Milk", "Beverages", "2025-03-10")
item1.get_details()

report = Report()
report.items_in('Foods')

report.create_new_recipe("Fruit Salad", ["Apple", "Banana", "Orange"])

report.recipes()

