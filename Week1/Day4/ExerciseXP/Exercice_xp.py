#Exercice 1

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Siamese(Cat):
    def __init__(self, name, age, race):
        super().__init__(name, age)
        self.race = race

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    

bengal = Bengal("Meow", 3)
chartreux = Chartreux("Ch", 5)
siamese = Siamese("Sia", 2, "Siamese")

all_cats = [bengal, chartreux, siamese]

sara_pets = Pets(all_cats)

sara_pets.walk()



#Exercice 2

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


#Exercice 3
from dog import Dog
import random
class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self): 
        super().bark()
        self.trained = True

    def play(self, *args):
        # ... code to print play message ...
        print(f"{self.name} and {', '.join(args)} all play together")

    def do_a_trick(self): 
        if self.trained:
            tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
            print(f"{self.name} {random.choice(tricks)}")

# Test PetDog methods
my_dog = PetDog("Fido", 2, 10)
my_dog.train()
my_dog.play("Buddy", "Max")
my_dog.do_a_trick()


#Exercice 4

class Person:
    def __init__(self,first_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = ""
    
    def is_18(self):
        if self.age >= 18:
            return True
        else:
            return False
        

class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []
    
    def born(self, first_name, age):
        person = Person(first_name, age)
        person.last_name = self.last_name
        self.members.append(person)
    
    def check_majority(self):
        for member in self.members:
            for member in self.members:
                
                if member.is_18():
                    print(f"You are over 18, your parents {member.first_name} {self.last_name} accept that you will go out with your friends")
                else:
                    print(f"{member.first_name} {self.last_name} is not an adult.")

    def presentation_family(self):
        print(f"Family Name: {self.last_name}")
        for member in self.members:
            print(f" - {member.first_name} {self.last_name}, Age: {member.age}")
            
family = Family("Smith")

family.born("John", 20)
family.born("Emma", 15)
family.check_majority()
family.presentation_family()