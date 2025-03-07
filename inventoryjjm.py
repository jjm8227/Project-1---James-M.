import csv

class InventorySystem:
    def __init__(self):
        self.food_items = self.load_items('items_food.csv')
        self.beverage_items = self.load_items('items_beverages.csv')
        print("Inventory System Initialized!")

    def load_items(self, filename):
        items = []
        try:
            with open(filename, newline='') as file:
                reader = csv.reader(file)
                items = [line[0] for line in reader]
        except FileNotFoundError:
            print(f"{filename} not found!")
        return items

    def add_to_inventory(self, item, category):
        if category == 'Beverages':
            if item not in self.beverage_items:
                self.beverage_items.append(item)
            else:
                print(f"Item '{item}' already exists in Beverages category.")
        elif category == 'Foods':
            if item not in self.food_items:
                self.food_items.append(item)
            else:
                print(f"Item '{item}' already exists in Foods category.")
        else:
            print("Invalid category!")

    def remove_from_inventory(self, item, category):
        if category == 'Beverages' and item in self.beverage_items:
            self.beverage_items.remove(item)
        elif category == 'Foods' and item in self.food_items:
            self.food_items.remove(item)
        else:
            print(f"Item '{item}' not found in {category} category.")

    def display_inventory(self):
        print(f"\n--- Current Inventory ---")
        print(f"Foods: {self.food_items}")
        print(f"Beverages: {self.beverage_items}")

    def get_items_by_category(self, category):
        if category == 'Foods':
            return self.food_items
        elif category == 'Beverages':
            return self.beverage_items
        else:
            print("Invalid category!")
            return []

class Product:
    def __init__(self, name="", category=None, expiry=None):
        self.name = name
        self.category = category
        self.expiry = expiry

    def update_name(self, name):
        self.name = name
        return self.name

    def update_category(self, category):
        self.category = category
        return self.category

    def update_expiry(self, date):
        self.expiry = date
        return self.expiry

    def show_product_details(self):
        print(f"Product Name: {self.name}")
        print(f"Category: {self.category}")
        print(f"Expiration Date: {self.expiry}")

class InventoryReport(InventorySystem):
    def __init__(self):
        super().__init__()

    def report_item_count(self, category):
        if category == 'Foods':
            print(f"There are {len(self.food_items)} items in the Foods category.")
        elif category == 'Beverages':
            print(f"There are {len(self.beverage_items)} items in the Beverages category.")
        else:
            print(f"Invalid category '{category}'!")

    def list_recipes(self):
        try:
            with open('recipes.csv', newline='') as file:
                recipes = [line[0] for line in csv.reader(file)]
            print(f"\n--- Recipes Available ---")
            print(recipes)
        except FileNotFoundError:
            print("Recipes file is missing. Ensure 'recipes.csv' exists.")

    def add_recipe(self, recipe_name, ingredients):
        print(f"\nAdding a new recipe: '{recipe_name}'")
        print(f"Ingredients: {ingredients}")
        with open('recipes.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([recipe_name, *ingredients])
        print(f"Recipe '{recipe_name}' added successfully!")
