def count_bs(bees):
    print(bees.count("b"))


def every(list):
    for i in list:
        if bool(i) == True:
            flag = True
        else:
            return False
    return flag


def month(num):
    data = {
        "winter": [1,2,3],
        "spring": [4,5,6],
        "summer": [7,8,9],
        "autumn": [10,11,12]
    }
    for i,v in data.items():
        for j in v:
            if j == num:
                print(i)

class Circle:
    def __init__(self,rad):
        self.rad = rad
    def get_area(self):
        return 3.14 * self.rad
    def get_perimeter(self):
        return 2 * 3.14 * self.rad


class Beverage:
    ingredients = []
    s = 0
    p = 0
    ing = " "
    cost = {
        "Strawberries" : 1.50,
        "Banana" : 0.50,
        "Mango" : 2.50,
        "Blueberries" : 1.00,
        "Raspberries" : 1.00,
        "Apple" : 1.75,
        "Pineapple" : 3.50
    }
    def __init__(self,ingredient):
        self.ingredient = ingredient
    def get_ingredients(self):
        self.ingredients = self.ingredient
        return self.ingredients
    def get_cost(self):
        for i in self.ingredient:
            for c in self.cost:
                if i == c:
                    self.s += self.cost[c]
        return self.s
    def get_pice(self):
        for i in self.ingredient:
            for c in self.cost:
                if i == c:
                    self.p = 2.5 * self.cost[c]
        return self.p
    def get_name(self):
        self.ing = ' '.join(self.get_ingredients())
        if len(self.ing.split()) == 1:
            print(self.ing.replace('berries','berry') + " Smoothie")
        else:
            print(self.ing.replace('berries','berry') + " Fusion")

s1 = Beverage(['Banana'])
print(s1.get_ingredients())
print(s1.get_cost())
print(s1.get_pice())
s1.get_name()




