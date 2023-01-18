import random
import shelve
from datetime import datetime
now = datetime.now()

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
        user_info = input("1. remove ingredient\n2. add ingredient\n")
        if user_info == "1":
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
        if user_info == "2":
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
        if tag in self.ingredients or tag in self.category:
            return True
        return False

meal_db = shelve.open("meals")
meal_db["0"] = Meal("Channa", ["lunch", "dinner"], ["chole", "turmeric", "zeera"])
meal_db["1"] = Meal("Dosa", ["lunch", "dinner", "breakfast"], ["dosa mix", "masala"])
meal_db["2"] = Meal("Gol guppa", ["lunch", "breakfast"], ["masala","aloo"])
meal_db["3"] = Meal("Pooha", ["breakfast", "lunch"], ["turmeric", "rice"])
meal_db["4"] = Meal("Pasta", ["lunch, dinner"], ["pasta", "tomatos"])
meal_db["5"] = Meal("Dumplings", ["dinner"], ["dumpling skin", "veggies"])

def ingre_add():
        ingre_input = input("ingredients \n(seperate ingredients using a comma)\n")
        try:
            ingre_list = ingre_input.split(', ')
            return ingre_list
        except:
            print("seperate using a space and a comma")
            ingre_add()
     
def categ_add():
    categ_input = input("categories \n(seperate categories using a comma)\n")
    try:
        categ_list = categ_input.split(', ')
        return categ_list
    except:
        print("seperate using a space and a comma")
        categ_add()

def add_meal():
    name = input("meal name:\n")
    ingredients = ingre_add()
    categories = categ_add()
    meal_db[str(len(meal_db))] = Meal(name, ingredients, categories)
        
def meal_generation(day_nums):
    temp_db = meal_db
    i = 0
    meal_list = {}
    if day_nums <= len(meal_db):
        while i in range(day_nums):
            key = str(random.choice(list(temp_db)))
            gen_meal = temp_db[key]
            del temp_db[key]
            meal_list[i+1] = gen_meal
            i += 1
        return meal_list
    else:
        print("Not enough meals in the database")
        return {}

def filter_generation(day_nums, tags):
    ml_vals = search(tags)
    i = 0
    meal_list = {}
    if day_nums <= len(ml_vals):
        while i in range(day_nums):
            key = str(random.choice(list(ml_vals)))
            gen_meal = meal_db[key]
            del ml_vals[key]
            meal_list[key] = gen_meal
            i += 1
    else:
        print("\nnot enough meals with those tags\n")
    print(meal_list)
    return meal_list

def switch_meals_reg(day_switched, meal_plan):
    temp = meal_db
    temp_list = [(k,v) for k, v in temp.items()]

    if day_switched in meal_plan:
        for x in meal_plan:
            for y in range(len(temp_list)):
                if meal_plan[x] in temp_list[y]:
                    del temp[temp_list[y][0]]
                    break     
        meal_plan[day_switched] = random.choice(list(temp.values()))

    else: 
        print("not in day range")
    meal_view(meal_plan)

def switch_meals_filter(day_switched, meal_plan, tags):
    filtered_db = search(tags)
    temp_list = [(k,v) for k, v in filtered_db.items()]

    if day_switched in meal_plan:
        for x in meal_plan:
            for y in range(len(temp_list)):
                if meal_plan[x] in temp_list[y]:
                    del filtered_db[temp_list[y][0]]
                    break     
        meal_plan[day_switched] = random.choice(list(filtered_db.values()))
    else: 
        print("not in day range")
    meal_view(meal_plan)

def search(tags):
    tags = tags.split(", ")
    meals = {}
    for x in meal_db:
        if set(tags) <= set(meal_db[x].ingredients+meal_db[x].category):
            meals[x] = meal_db[str(x)]
    return meals

def meal_view(meal_content):
    meal_ingred_lists = []
    meal_str = ""
    i = 1
    def new_line(string):
        print()
        string = string + "\n"
        return string

    def spacing(string):
        for w in range(len(meal_content)):
            print(''.center(15), end="|")
            string = string + ''.center(15) + "|"
        print()
        string = string + "\n"
        return string
   
    def double_space(string):
        string = new_line(string)
        string = spacing(string)
        return string

    if len(meal_content) >= 1:
        for v in meal_content:
            day_count = "day " + str(i)
            print(day_count.center(15), end="|")
            meal_str = meal_str + day_count.center(15) + "|"
            meal_ingred_lists.append(meal_content[v].ingredients)
            i += 1
        meal_str = double_space(meal_str)

        for x in meal_content:
            str_x = str(x)
            content = meal_content[x]
            print(content.name.center(15), end="|")
            meal_str = meal_str + content.name.center(15)+ "|"

        meal_str = double_space(meal_str)
        meal_str = spacing(meal_str)
        for z in range(len(meal_content)):
            print('ingredients:'.center(15), end="|")
            meal_str = meal_str + 'ingredients:'.center(15) + "|"
        
        meal_str = double_space(meal_str)

        a = max(len(b) for b in meal_ingred_lists)
        i = 0
        while i < a:
            for c in meal_content:
                try:
                    print(meal_content[c].ingredients[i].center(15), end="|")
                    meal_str = meal_str + meal_content[c].ingredients[i].center(15) + "|"
                except:
                    print("".center(15), end="|")
                    meal_str = meal_str + "".center(15) + "|"
            meal_str = new_line(meal_str)
            i += 1
        meal_str = meal_str + "\n"
        meal_str = new_line(meal_str)
        meal_str = new_line(meal_str)

        return meal_str
    else:
        return ""

def main():
    time = now.strftime("%d-%m-%y~%H-%M-%S.txt")
    x = meal_generation(3)
    contents = meal_view(x)
    with open(time, "x") as f:
        f.write(contents)
    switch_meals_filter(3, x, "lunch")
    
main()