from abc import ABC, abstractmethod

class MealConsumed(ABC):
    def __init__(self, name):
        self.setName(name)

    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name

    @abstractmethod
    def calcCalories(self) -> None:
        pass

class Food(MealConsumed):
    def __init__(self, name):
        super().__init__(name)

    def calcCalories(self):
        self.calories = 100

class Drink(MealConsumed):
    def __init__(self, name):
        super().__init__(name)

    def calcCalories(self):
        self.calories = 50

