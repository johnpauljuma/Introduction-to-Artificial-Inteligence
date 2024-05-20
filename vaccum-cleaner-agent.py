import random

#Design the Environment
class environment(object):
    def __init__(self):
        #instantiate locations and conditions
        # 0 indicates Clean and 1 indicates dirty
        self.location = ["A","B"] #Locations
        self.locationcondition = {"A": 0, "B": 0} #Status of enviroment
        #Randomise conditions
        self.locationcondition["A"] = random.randint(0,1)
        self.locationcondition["B"] = random.randint(0,1)
        #Place vacuum cleaner at a random location
        self.vacuumlocation = random.choice(self.location)
#Design the vacuum cleaner agent
class agent(environment):
    def __init__(self, environment):
        print("Environment condition", environment.locationcondition,
        "vacuum location", environment.vacuumlocation)
        count = 0
        #Set the number of iterations to two to avoid infinite loops
        while count < 2:
            if environment.locationcondition[environment.vacuumlocation] ==1:# suck and mark clean
                environment.locationcondition[environment.vacuumlocation] = 0
                print(environment.vacuumlocation, "Has been cleaned")
            else:
                print(environment.vacuumlocation, "Is cleaned")
            newindex = environment.location.index(environment.vacuumlocation)+1
            if newindex == 2:
                newindex = 0
            environment.vacuumlocation = environment.location[newindex]
            count += 1
        #Done with cleaning
        print(environment.locationcondition)
#Create an environment
e1 = environment()
#Send the vacuum agent
a1 = agent(e1)