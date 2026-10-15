"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.


class Aircraft:
    # Class variable shared by all aircraft objects
    aircraft_category = "General Aviation"

    def __init__(self, make, model, registration):
        # Instance variables unique to each aircraft
        self.make = make
        self.model = model
        self.registration = registration

    def display_info(self):
        return (
            f"Make: {self.make}, Model: {self.model}, "
            f"Registration: {self.registration}, "
            f"Category: {self.aircraft_category}"
        )


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class TrainingAircraft(Aircraft):
    # New class variable for training aircraft
    aircraft_purpose = "Flight Training"

    def __init__(self, make, model, registration, max_passengers,
                 flight_hours):
        # Inherit the parent class's instance variables
        super().__init__(make, model, registration)

        # New instance variables for training aircraft
        self.max_passengers = max_passengers
        self.flight_hours = flight_hours

    # Override the parent class method
    def display_info(self):
        return (
            f"Training Aircraft - Make: {self.make}, "
            f"Model: {self.model}, Registration: {self.registration}, "
            f"Category: {self.aircraft_category}, "
            f"Purpose: {self.aircraft_purpose}, "
            f"Max Passengers: {self.max_passengers}, "
            f"Flight Hours: {self.flight_hours}"
        )

    # New method specific to training aircraft
    def log_flight(self, hours):
        self.flight_hours += hours
        return f"{hours} flight hours logged. Total: {self.flight_hours}"


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    # Create two training aircraft objects
    aircraft1 = TrainingAircraft("Cessna", "172", "N123AB", 3, 120)
    aircraft2 = TrainingAircraft("Piper", "PA-28", "N456CD", 3, 95)

    # Access a class variable through the class itself
    print("Class variable:", TrainingAircraft.aircraft_purpose)

    # Access the same class variable through an object
    print("Aircraft 1 purpose:", aircraft1.aircraft_purpose)

    # Add a new attribute to only one object
    aircraft1.last_inspection = "October 2026"

    # Display each object's instance namespace
    print("\nAircraft 1 instance namespace:")
    print(aircraft1.__dict__)

    print("\nAircraft 2 instance namespace:")
    print(aircraft2.__dict__)

    # Display information about the class namespace
    print("\nTrainingAircraft class namespace:")
    print(TrainingAircraft.__dict__)


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    # Create a flight training record containing nested mutable data
    original = {
        "aircraft": "Cessna 172",
        "pilot": "Student Pilot",
        "flight_log": {
            "total_hours": 120,
            "completed_lessons": ["Takeoffs", "Landings"]
        }
    }

    # A shallow copy creates a new outer dictionary but shares
    # nested mutable objects with the original.
    shallow_copy = copy(original)

    # A deep copy creates a new outer dictionary and recursively
    # copies nested objects, keeping their data independent.
    deep_copy = deepcopy(original)

    # Modify the original object's nested data
    original["flight_log"]["total_hours"] = 125
    original["flight_log"]["completed_lessons"].append(
        "Instrument Approaches"
    )

    # Display all three dictionaries to compare their contents
    print("Original flight record:")
    print(original)

    print("\nShallow copy of flight record:")
    print(shallow_copy)

    print("\nDeep copy of flight record:")
    print(deep_copy)


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    # Create and test a parent class object
    aircraft = Aircraft("Cessna", "150", "N789EF")
    print("\nParent class aircraft:")
    print(aircraft.display_info())

    # Create and test a child class object
    training_aircraft = TrainingAircraft(
        "Cessna", "172", "N123AB", 3, 120
    )

    print("\nChild class training aircraft:")
    print(training_aircraft.display_info())

    # Demonstrate an inherited method override and a new child method
    print("\nDemonstrating inheritance:")
    print(training_aircraft.display_info())
    print(training_aircraft.log_flight(2))

    # Demonstrate namespaces and copying
    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()
