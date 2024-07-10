import random
class RoverPerformance:
    def __init__(self):
        self.score = 0
    def update_score(self, success):
        if success:
            self.score += 1
    def display(self, sampled_locations):
        print(f"Locations Sampled {sampled_locations}")
        performance = (self.score / 4) * 100
        print(f"Rovers performance {performance:.1f} %")
        return performance
class MarsEnvironment:
    def __init__(self):
        self.locations = ['A', 'B', 'C', 'D']
        self.randomize_conditions()
    def randomize_conditions(self):
        self.location_condition = {loc: random.randint(0, 1) for loc in self.locations}
    def has_rocks(self, location):
        return self.location_condition[location] == 1
class RoverAgent:
    def __init__(self, environment, performance):
        self.environment = environment
        self.performance = performance
        self.sampled_locations = {loc: 0 for loc in self.environment.locations}
        self.sampling_history = []
    def sample(self, location, venture):
        if venture == 1 and self.sampling_history[0][location] == 1 and self.environment.has_rocks(location):
            return f"{location} Location has been sampled before."
        elif not self.environment.has_rocks(location):
            return f"{location} has no Rocks."
        else:
            if self.sampled_locations[location] == 0:
                self.sampled_locations[location] = 1
            self.performance.update_score(True)
            return f"{location} Rocks Sampled."
    def explore(self, venture_count):
        for venture in range(venture_count):
            start_location = random.choice(self.environment.locations)
            print(f"------ Exploration venture {venture} ------")
            print(self.environment.location_condition)
            print(f"Rover is in location {start_location}")
            venture_sampling = {loc: 0 for loc in self.environment.locations}
            locations_order = self.environment.locations[:]
            locations_order = locations_order[locations_order.index(start_location):] + locations_order[:locations_order.index(start_location)]
            for location in locations_order:
                result = self.sample(location, venture)
                print(result)
            if "Rocks Sampled" in result:
                venture_sampling[location] = 1
                self.sampling_history.append(venture_sampling)
                self.environment.randomize_conditions()
                print()
        # sampled_locations to reflect all locations sampled across ventures
        for venture_sampling in self.sampling_history:
            for loc, sampled in venture_sampling.items():
                if sampled:
                    self.sampled_locations[loc] = 1
            return self.sampled_locations
# Initialize performance and environment
performance = RoverPerformance()
environment = MarsEnvironment()
# Create the rover agent
rover = RoverAgent(environment, performance)
# Simulate two exploration ventures
sampled_locations = rover.explore(2)
# Display performance
performance.display(sampled_locations)