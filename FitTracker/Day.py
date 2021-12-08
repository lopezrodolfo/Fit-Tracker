import Meal
import Workout
import Account
import datetime

class Day:
    def __init__(self):
        self.setDate()
        self.meals = []
        self.workouts = []

    def getDate(self):
        return self.date
    
    def setDate(self):
        cur_date = datetime.datetime.now()
        self.date = cur_date.strftime("%x")

    def getMeals(self):
        return self.meals

    def addMeal(self, meal): #where meal is a Meal object
        self.meals.append(meal)
    
    def getWorkouts(self):
        return self.workouts

    def addWorkout(self, workout): #where workout is a Workout object
        self.workouts.append(workout)

    def calcCaloriesConsumed(self):
        self.calories_consumed = 0
        for meal in self.meals:
            if type(meal) == type(Food) or type(meal) == type(Drink):
                meal.calories

    def calcCaloriesBurned(self):
        self.calories_burned = 0
        for workout in self.workouts:
            if type(workout) == type(Cardio) or type(workout) == type(Weighted):
                self.calories_burned += workout.calories_burned
    
    def calcNetCalories(self):
        self.net_calories = self.calories_consumed - self.calories_burned

    def calcDeviation(self):
        self.deviation = self.net_calories - Account.calorie_budget
        

# d = Day(1,2)
# print(d.date)