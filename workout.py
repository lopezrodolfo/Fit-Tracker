from abc import ABC, abstractmethod


class Workout(ABC):
    """Stores Workout created by current user"""

    def __init__(self, name, calories_per_hour, hours):
        self.setName(name)
        self.setCaloriesPerHour(calories_per_hour)
        self.setHours(hours)

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getCaloriesPerHour(self):
        return self.calories_per_hour

    def setCaloriesPerHour(self, calories_per_hour):
        self.calories_per_hour = calories_per_hour

    def getHours(self):
        return self.hours

    def setHours(self, hours):
        self.hours = hours

    @abstractmethod
    def calcCaloriesBurned(self) -> None:
        pass


class Cardio(Workout):
    def __init__(self, name, calories_per_hour, hours):
        super().__init__(name, calories_per_hour, hours)

    def calcCaloriesBurned(self):
        self.calories_burned = float(self.hours) * float(self.calories_per_hour)
        return self.calories_burned


class Weighted(Workout):
    def __init__(self, name, calories_per_hour, hours):
        super().__init__(name, calories_per_hour, hours)

    def calcCaloriesBurned(self):
        self.calories_burned = float(self.hours) * float(self.calories_per_hour)
        return self.calories_burned
