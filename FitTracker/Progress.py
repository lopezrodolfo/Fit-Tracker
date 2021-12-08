import Day #should also import Account with day

class Progress:
    def __init__(self):
        self.days = []

    def getDays(self):
        return self.days

    #never need to set day
    
    def addDay(self, day): #where day is Day object
        self.days.append(day)
        
    


    