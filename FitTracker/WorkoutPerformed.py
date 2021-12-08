from abc import ABC, abstractmethod

class WorkoutPerformed(ABC):
    def __init__(self, name):
        self.setName(name)

    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name

    @abstractmethod
    def calcCaloriesBurned(self) -> None:
        pass

class Cardio(WorkoutPerformed):
    def __init__(self, name):
        super().__init__(name)

    def calcCaloriesBurned(self):
        self.calories_burned = 100

class Weighted(WorkoutPerformed):
    def __init__(self, name):
        super().__init__(name)

    def calcCaloriesBurned(self):
        self.calories_burned = 50

