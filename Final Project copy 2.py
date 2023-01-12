import random
import shelve

class Meal:
    def __init__(self, name, category=[], ingredients=[]):
        self.name = name
        self.ingredients = ingredients
        self.category = category

    def info(self):
        print("\n\n", self.name,"\n")
        for x in self.category:
            print("-",x)
        print("-----------------------")
        print("\ningredients\n")
        for x in self.ingredients:
            print("-",x)
        print("\n")
    
    def ingre_edit(self):
        self.info()
        check = True
        a = input("1. remove ingredient\n2. add ingredient\n")
        if a == "1":
            while check:
                x = input("what ingredient do you wish to remove?\n")
                if x in self.ingredients:
                    self.ingredients.remove(x)
                    self.info()
                    x = input("remove more ingredients?\n")
                    if x not in ["y", "Y", "ye", "Ye", "yes", "Yes", "yea", "yea"]:
                        check = False
                else:
                    print("Not in ingredients")
        if a == "2":
            while check:
                x = input("what ingredient do you wish to add?\n")
                self.ingredients.append(x)
                self.info()
                x = input("add more ingredients?\n")
                if x not in ["y", "Y", "ye", "Ye", "yes", "Yes", "yea", "yea"]:
                    check = False
    
    def categ_edit(self):
        self.info()
        check = True
        a = input("1. remove category\n2. add category\n")
        if a == "1":
            while check:
                x = input("what category do you wish to remove?\n")
                if x in self.ingredients:
                    self.category.remove(x)
                    self.info()
                    x = input("remove more categories?\n")
                    if x not in ["y", "Y", "ye", "Ye", "yes", "Yes", "yea", "yea"]:
                        check = False
                else:
                    print("Not a category")
        if a == "2":
            while check:
                x = input("what category do you wish to add?\n")
                self.category.append(x)
                self.info()
                x = input("add more?\n")
                if x not in ["y", "Y", "ye", "Ye", "yes", "Yes", "yea", "yea"]:
                    check = False
    
    def tag_check(self, tag):
        if tag in self.ingredients or self.category:
            return True
        return False

meal_db = shelve.open("meals")
meal_db["0"] = Meal("Channa", ["lunch", "dinner"], ["chole", "turmeric", "zeera"])
meal_db["1"] = Meal("Dosa", ["lunch", "dinner", "breakfast"], ["dosa mix", "masala"])
meal_db["2"] = Meal("gol guppa", ["breakfast"], ["masala","aloo"])
meal_db["3"] = Meal("pohaa", ["breakfast", "lunch"], ["turmeric", "rice"])

def add_meal():
    name = input("meal name:\n")
    def ingre_add():
        ingre = input("ingredients \n(seperate ingredients using a comma)\n")
        try:
            ingre_list = ingre.split(', ')
            return ingre_list
        except:
            print("seperate using a space and a comma")
            ingre_add()
     
    def categ_add():
        categ = input("categories \n(seperate categories using a comma)\n")
        try:
            categ_list = categ.split(', ')
            return categ_list
        except:
            print("seperate using a space and a comma")
            categ_add()
    
    ingredients = ingre_add()
    categories = categ_add()
    meal_db[str(len(meal_db))] = Meal(name, ingredients, categories)
        
def meal_generation(day_nums, db):
    temp_db = db
    i = 0
    meal_list = []
    while i in range(day_nums):
        x = str(random.randint(0, len(db)-1))
        if x in temp_db:
            gen_meal = temp_db[x]
            del temp_db[x]
            meal_list.append(gen_meal)
            i += 1
        else:
            continue
    return meal_list

def search(tags, name_ret):
    tags = tags.split(", ")
    meal_keys = []
    meal_val = []
    if tags != []:
        for x in meal_db:
            if set(tags) <= set(meal_db[x].category + meal_db[x].ingredients):
                meal_keys.append(x)
    if name_ret == True:
        for y in meal_keys:
            meal_val.append(meal_db[y].name)
        return meal_val
    return meal_keys

def filter_generation(tags, day_nums):
    ml_vals = search(tags, False)
    i = 0
    meal_list = []
    if day_nums <= len(ml_vals):
        while i in range(day_nums):
            x = str(random.randint(0, len(ml_vals)-1))
            gen_meal = meal_db[ml_vals[int(x)]]
            ml_vals.pop(int(x))
            meal_list.append(gen_meal.name)
            i += 1
    else:
        return "not enough meals with those tags"
    return meal_list
    

    
def main():
    print(filter_generation("turmeric, lunch", 2))
    
main()