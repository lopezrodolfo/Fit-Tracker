from abc import ABC, abstractmethod


class Meal(ABC):
    """Stores Meal created by current user"""

    def __init__(self, name, unit, calories_per_unit, amount):
        self.setName(name)
        self.setUnit(unit)
        self.setCaloriesPerUnit(calories_per_unit)
        self.setAmount(amount)

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getUnit(self):
        return self.unit

    def setUnit(self, unit):
        self.unit = unit

    def getCaloriesPerUnit(self):
        return self.calories_per_unit

    def setCaloriesPerUnit(self, calories_per_unit):
        self.calories_per_unit = calories_per_unit

    def getamount(self):
        return self.amount

    def setAmount(self, amount):
        self.amount = amount

    @abstractmethod
    def calcCaloriesConsumed(self) -> None:
        pass


class Food(Meal):
    def __init__(self, name, unit, calories_per_unit, amount):
        super().__init__(name, unit, calories_per_unit, amount)

    def calcCaloriesConsumed(self):
        self.calories_consumed = float(self.amount) * float(self.calories_per_unit)
        return self.calories_consumed


class Drink(Meal):
    def __init__(self, name, unit, calories_per_unit, amount):
        super().__init__(name, unit, calories_per_unit, amount)

    def calcCaloriesConsumed(self):
        self.calories_consumed = float(self.amount) * float(self.calories_per_unit)
        return self.calories_consumed
