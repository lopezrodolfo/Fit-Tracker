import MealConsumed

class Meal:
    def __init__(self, name):
        self.setName(name)
        self.food_consumed = []
        self.drinks_consumed = []

    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name

    def getFoodConsumed(self):
        return self.food_consumed

    def addFoodConsumed(self, food_consumed): #where food_consumed is Food object
        self.food_consumed.append(food_consumed)

    def getDrinksConsumed(self):
        return self.drinks_consumed
    
    def addDrinkConsumed(self, drink_consumed): #where drink_consumed is Drink object
        self.drinks_consumed.append(drink_consumed)

class Breakfast(Meal):
    def __init__(self, name):
        super().__init__(name)

class Lunch(Meal):
    def __init__(self, name):
        super().__init__(name)

class Dinner(Meal):
    def __init__(self, name):
        super().__init__(name)

class Snack(Meal):
    def __init__(self, name):
        super().__init__(name)