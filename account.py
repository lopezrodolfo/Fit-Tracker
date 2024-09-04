class Account:
    """Stores account info for current user"""

    def __init__(self, username, full_name, gender, height, weight, age):
        self.calories_consumed = 0.0
        self.calories_burned = 0.0
        self.setUsername(username)
        self.setFullName(full_name)
        self.setGender(gender)
        self.setHeight(height)
        self.setWeight(weight)
        self.setAge(age)
        self.calcCalorieBudget()
        self.calcNetCalories()
        self.calcDeviation()

    def __str__(self):
        """Daily Totals (can be saved to user's progress file"""
        return f"Calorie Budget: {self.calorie_budget:.2f} Calories Consumed: {self.calories_consumed:.2f} Calories Burned: {self.calories_burned:.2f} Net Calories: {self.net_calories:.2f} Progress: {self.displayProgress()}"

    def incCaloriesConsumed(self, calories_consumed):
        self.calories_consumed += calories_consumed
        self.net_calories += calories_consumed
        self.calcDeviation()

    def incCaloriesBurned(self, calories_burned):
        self.calories_burned += calories_burned
        self.net_calories -= calories_burned
        self.calcDeviation()

    def getUsername(self):
        return self.username

    def setUsername(self, username):
        self.username = username

    def getFullName(self):
        return self.full_name

    def setFullName(self, full_name):
        self.full_name = full_name

    def getGender(self):
        return self.gender

    def setGender(self, gender):
        self.gender = gender

    def getHeight(self):
        return self.height

    def setHeight(self, height):
        self.height = height

    def getWeight(self):
        return self.weight

    def setWeight(self, weight):
        self.weight = weight

    def getAge(self):
        return self.age

    def setAge(self, age):
        self.age = age

    def calcCalorieBudget(self):
        if self.gender.lower() == "male" or self.gender.lower() == "m":
            self.calorie_budget = (
                66.47
                + (6.24 * float(self.weight))
                + (12.7 * float(self.height))
                - (6.755 * int(self.age))
            )
        elif self.gender.lower() == "female" or self.gender.lower() == "f":
            self.calorie_budget = (
                655.1 * (4.35 * float(self.weight))
                + (4.7 * float(self.height))
                - (4.7 * int(self.age))
            )
        else:
            self.calorie_budget = 2000.0

    def calcNetCalories(self):
        self.net_calories = float(self.calories_consumed) - float(self.calories_burned)

    def calcDeviation(self):
        self.deviation = float(self.calorie_budget) - float(self.net_calories)

    def displayProgress(self):
        if self.deviation < 0:
            return f"Over budget by {abs(self.deviation):.2f}"
        elif self.deviation > 0:
            return f"Under budget by {self.deviation:.2f}"
        else:
            return "Perfectly on budget"
