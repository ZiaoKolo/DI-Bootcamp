class Farm :
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    def add_animal(self, **kwargs):
        for animal_type, count in kwargs.items():
            if animal_type in self.animals:
                self.animals[animal_type] += count
            else:
                self.animals[animal_type] = count

    def get_info(self):
        Info= f"le nom de la ferme est {self.name} "
        for animal, count in self.animals.items():
            Info += f"{animal}: {count}\n"
        Info += "EIEI-0!"
        return Info
    
    def get_animal_types(self):
        return sorted(self.animals.keys())
    
    def get_short_info(self):
        animal_types = self.get_animal_types()
        if not animal_types:
            return f"{self.name} farm has no animals."
        elif len(animal_types) == 1:
            return f"{self.name} farm has {animal_types[0]}."
        else:
            animals_str = ", ".join(animal_types[:-1]) + f" and {animal_types[-1]}"
            return f"{self.name} farm has {animals_str}."

macdonald = Farm("McDonald")
macdonald.add_animal(cow=5, sheep=2, goat=12)
print(macdonald.get_short_info())
