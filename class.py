# Base class
class Superhero:
    def __init__(self, name, power_level):
        self.name = name
        self._power_level = power_level  # Protected attribute (encapsulation)

    def show_power(self):
        print(f"{self.name} has a power level of {self._power_level}.")

    def use_power(self):
        print(f"{self.name} uses a mysterious power!")

# Subclass
class Flyer(Superhero):
    def use_power(self):
        print(f"{self.name} soars into the sky with lightning speed! 🕊️")

# Subclass
class Invisibility(Superhero):
    def use_power(self):
        print(f"{self.name} vanishes into thin air... 🫥")

# Create objects
hero1 = Flyer("Skylord", 95)
hero2 = Invisibility("Shadowstrike", 87)

# Demonstrate functionality
hero1.show_power()
hero1.use_power()

hero2.show_power()
hero2.use_power()
