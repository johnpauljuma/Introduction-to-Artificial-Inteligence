import random
import time
class environment(object):
    def __init__(self):
        self.location = ["A","B"] #locations
        self.locationcondition = {"A": 0,"B": 0}
        self.locationcondition["A"] = random.randint(0,1)
        self.locationcondition["B"] = random.randint(0,1)
        self.vacuumlocation = random.choice(self.location)
        self.mode = ["T","L"]
        self.cleaningmethod = {"A":"T","B":"T"}
        self.cleaningmethod["A"] = random.choice (self.mode)
        self.cleaningmethod["B"] = random.choice (self.mode)
class agent(environment):
    def __init__(self,environment):
        print("Environment condition", environment.locationcondition, "Vacuum location",environment.vacuumlocation, "cleaning method"
        ,environment.cleaningmethod)
        count = 0
        while count<2:
            if environment.locationcondition[environment.vacuumlocation] == 1:
                if environment.cleaningmethod[environment.vacuumlocation] == "T":
                    environment.cleaningmethod[environment.vacuumlocation] = "L"
                else:
                    environment.cleaningmethod[environment.vacuumlocation] = "T"
                environment.locationcondition[environment.vacuumlocation] = 0
                print(environment.vacuumlocation, "Has been cleaned")
            else:
                print(environment.vacuumlocation, "Is clean")
            newindex = environment.location.index(environment.vacuumlocation)+1
            if newindex == 2:
                newindex = 0
            environment.vacuumlocation = environment.location[newindex]
            count += 1
        print("new conditions",environment.locationcondition)
        print("updated history",environment.cleaningmethod)
#The goal can be achieved follows
x=0
while x<24:
    e1 = environment()
    a1 = agent(e1)
    x+=1
    #Add a 1 hr delay in the loop
    time.sleep(1)