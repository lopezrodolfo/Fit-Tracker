import WorkoutPerformed

class Workout:
    def __init__(self, name):
        self.setName(name)
        self.cardio_performed = []
        self.weighted_performed = []

    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name
    
    def getCardioPerformed(self):
        return self.cardio_performed

    def addCardioPerformed(self, cardio_exercise): #where cardio exercise is Cardio object
        self.cardio_performed.append(cardio_exercise)

    def getWeightedPerformed(self):
        return self.weighted_performed
    
    def addWeightedPerformed(self, weighted_exercise): #where weighted exercise is Weighted object
        self.weighted_performed.append(weighted_exercise)
