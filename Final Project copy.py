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
meal_db["1"] = Meal("Dosa", ["lunch", "dinner"], ["dosa mix", "masala"])

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
        



def main():
    a = meal_db[str(random.randint(0, len(meal_db)-1))]
    a.info()
    add_meal()

    
main()