
"""
# Nutrient types

 MACRONUTRIENTS
 - carbohydrates
 - fat
 - protein

 MICRONUTRIENTS
 - minerals
 - vitamins

 # Condition
 raw, uncooked, cooked
"""

class NutritionFacts:
    def __init__(self, food, nutrient_type, condition, brand, production_country, ):
        self.food = food
        self.nutrient = nutrient_type
        self.condition = condition
        self.brand = brand
        self.origin = production_country

        self.nutrition_facts = [
            "kcal", 
            "fat", 
            "saturated_fat", 
            "carbohydrates", 
            "sugars", 
            "proteins", 
            "salt", 
            "vitamins and other"
            ]
        self.food_label = {}
        


    def add_food_label(self):
        print("Add nutrition facts as grams per 100g")
        for i, fact in enumerate(self.nutrition_facts):
            self.food_lable[fact] = input(f"{self.nutrition_facts[i]}: ")


    def edit_food_label(self):
        """To edit nutrition information on product food label"""
        pass


    def print_nutrition_table(self):
        """Prints a formatted table of nutrition facts in the terminal"""
        pass


    def compare_to_other_product(self, product):
        """Shows comparative percentages of nutrition / content"""
        # Fetches a product to compare to from register (json file).
        pass





rice = NutritionFacts("rice", "carbohydrate", "uncoocked", "ICA", "Italy")
rice.add_food_label()
print(rice.food_label)

