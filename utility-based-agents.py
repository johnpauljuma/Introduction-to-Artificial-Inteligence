import random
import time
class performance:
    def __init__(self):
        self.score = 0


    def display(self):
        print("Score: ", self.score)
        print("Perfomance: ", (self.score/48)*100, "%")


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


class agent(environment, performance):
    def __init__(self,environment, performance):
        print("Environment condition", environment.locationcondition, "Vacuum location",environment.vacuumlocation, "cleaning method" ,environment.cleaningmethod)
        count = 0
        while count<2:
            if environment.locationcondition[environment.vacuumlocation] == 1:
                if environment.cleaningmethod[environment.vacuumlocation] == "T":
                    environment.cleaningmethod[environment.vacuumlocation] = "L"
                else:
                    environment.cleaningmethod[environment.vacuumlocation] = "T"
                environment.locationcondition[environment.vacuumlocation] = 0
                print(environment.vacuumlocation, "Has been cleaned")
                performance.score+=1
            else:
                print(environment.vacuumlocation, "Is clean")
            newindex = environment.location.index(environment.vacuumlocation)+1
            if newindex == 2:
                newindex = 0
            environment.vacuumlocation = environment.location[newindex]
            count += 1
            print("new conditions",environment.locationcondition)
            print("updated history",environment.cleaningmethod)


thescore=performance()
x=0
while x<24:
    e1 = environment()
    a1 = agent(e1, thescore)
    x+=1
    time.sleep(1)
thescore.display()