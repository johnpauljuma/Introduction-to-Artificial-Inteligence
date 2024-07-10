import random

class RoverPerformance:
    def __init__(self):
        self.total_samples = 0
        self.successful_samples = 0

    def record_sample(self, location, success):
        self.total_samples += 1
        if success:
            self.successful_samples += 1

    def evaluate_performance(self):
        return f"Successful samples: {self.successful_samples} out of {self.total_samples}"

class MarsEnvironment:
    def __init__(self, locations):
        self.locations = locations

    def randomize_environment(self):
        for location in self.locations:
            self.locations[location] = bool(random.getrandbits(1))

    def is_rock_present(self, location):
        return self.locations.get(location, False)

class RoverAgent:
    def __init__(self, environment, performance):
        self.environment = environment
        self.performance = performance
        self.visited_locations = set()
        self.current_location = None

    def explore(self):
        while len(self.visited_locations) < len(self.environment.locations):
            self.current_location = random.choice(list(self.environment.locations.keys()))
            if self.current_location not in self.visited_locations:
                self.sample(self.current_location)
                self.visited_locations.add(self.current_location)

    def sample(self, location):
        rock_present = self.environment.is_rock_present(location)
        self.performance.record_sample(location, rock_present)
        print(f"Sampled {location}: {'Rock present' if rock_present else 'No rock'}")

# Example usage
locations = {'Location1': False, 'Location2': False, 'Location3': False, 'Location4': False}
environment = MarsEnvironment(locations)
performance = RoverPerformance()
rover = RoverAgent(environment, performance)

for _ in range(2):  # Two exploration ventures
    environment.randomize_environment()
    rover.explore()

print(performance.evaluate_performance())
