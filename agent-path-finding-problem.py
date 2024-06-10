import random
class environment(object):
    def __init__(self):
        self.location = ["1", "2", "3", "4"]
        self.move = ['U', 'D', 'L', 'R']
        self.path = {'1R':'2', '1L':'W', '1U':'W', '1D':'3',
                    '2R':'W', '2L':'1', '2U':'W', '2D':'4',
                    '3R':'4', '3L':'W', '3U':'1', '3D':'W',
                    '4R':'W', '4L':'3', '4U':'2', '4D':'W'}
        self.journey = []
class agent(environment):
    def choice_path(self, agent_location, environment):
        i = random.choice(self.move)
        j = str(agent_location[0] + i)
        print("Suggested Path:", j)
        while environment.path[j] == "W":
            i = random.choice(self.move)
            j = str(agent_location[0] + i)
        print("Suggested Path:", j)
        print("Selected Path:", j)
        return j
    def take_journey(self, environment):
        agent_location = random.choice(environment.location)
        print("agent_location:", agent_location)
        self.journey.append(agent_location[0])
        while agent_location[0] != "4":
            to_move = self.choice_path(agent_location, environment)
            agent_location = environment.path[to_move]
            self.journey.append(agent_location[0])
        self.journey.append(4)
        print("Journey",self.journey)
        return(self.journey)
e1 = environment()
a1 = agent()
a1.take_journey(e1)