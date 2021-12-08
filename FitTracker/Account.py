class Account:

    def __init__(self, first_name, last_name, gender, height, weight, age):
        self.setFirstName(first_name)
        self.setLastName(last_name)
        self.setGender(gender)
        self.setHeight(height)
        self.setWeight(weight)
        self.setAge(age)
        self.calcCalorieBudget()

    def getUsername(self):
        return self.username

    def setUsername(self, username):
        self.username = username

    # def getPassword(self):
    #     return self.__password
    
    # def setPassword(self, password):
    #     self.__password = password

    def getFirstName(self):
        return self.first_name
    
    def setFirstName(self, first_name):
        self.first_name = first_name

    def getLastName(self):
        return self.last_name
    
    def setLastName(self, last_name):
        self.last_name = last_name
    
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
        if self.gender.lower() == 'male':
            self.calorie_budget = 66 * (6.2 * float(self.weight)) + (12.7 * float(self.height)) - (6.76 * int(self.age))
        elif self.gender.lower() == "female":
            self.calorie_budget = 655.1 * (4.35 * float(self.weight)) + (4.7 * float(self.height)) - (4.7 * int(self.age))
        else:
            self.calorie_budget = 2000.0
            


        

    
    
    

