class Dog:
    def __init__(self, name, age, weight):
        # ... code to initialize attributes 
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        # ... code to return bark message ...
        return f"{self.name} goes woof!"

    def run_speed(self):
        # ... code to return run speed ...
        return self.weight / self.age

    def fight(self, other_dog):
        # ... code to determine and return winner ...
        if self.run_speed() * self.weight > other_dog.run_speed() * other_dog.weight:
            return f"{self.name} wins the fight!"
        elif self.run_speed() * self.weight < other_dog.run_speed() * other_dog.weight:
            return f"{other_dog.name} wins the fight!"
        else:
            return "It's a tie!"

# Step 2: Create dog instances
#... your code here
dog1 = Dog("Nick", 5, 20)
dog2 = Dog("Escanor", 3, 15)
dog3 = Dog("Bobby", 4, 18)
# Step 3: Test dog methods
print(dog1.bark())
print(dog2.run_speed())
print(dog1.fight(dog2))
