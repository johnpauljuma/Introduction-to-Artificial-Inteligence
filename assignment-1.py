import random

class MarsEnvironment:
    def __init__(self, locations=4):
        self.locations = locations
        self.rocks = [False] * locations

    def randomize_environment(self):
        self.rocks = [random.choice([True, False]) for _ in range(self.locations)]

    def has_rock(self, location):
        return self.rocks[location]

class RoverAgent:
    def __init__(self):
        self.sampled_locations = []

    def explore_and_sample(self, environment):
        for location in range(environment.locations):
            if location not in self.sampled_locations:
                if environment.has_rock(location):
                    self.sampled_locations.append(location)
                    print(f"Sampled rock at location {location}.")
                else:
                    print(f"No rock at location {location}.")

class RoverPerformance:
    def __init__(self):
        self.samples_taken = 0

    def update_performance(self, samples):
        self.samples_taken = samples

    def display_performance(self):
        print(f"Total samples taken: {self.samples_taken}")

def main():
    environment = MarsEnvironment()
    rover = RoverAgent()
    performance = RoverPerformance()

    # First exploration
    print("First Exploration:")
    environment.randomize_environment()
    rover.explore_and_sample(environment)

    # Second exploration
    print("\nSecond Exploration:")
    environment.randomize_environment()
    rover.explore_and_sample(environment)

    # Update and display performance
    performance.update_performance(len(rover.sampled_locations))
    performance.display_performance()

    print(f"Final sampled locations: {rover.sampled_locations}")

if __name__ == "__main__":
    main()
