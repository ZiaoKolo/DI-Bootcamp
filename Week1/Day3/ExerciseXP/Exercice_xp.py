#Exercice 1
#créer une classe Cat avec des attributs name et age
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
    
 #créer des objests de la classe Cat  
chat1 = Cat("Milou", 5)
chat2 = Cat("Masha", 3)
chat3 = Cat("Miaou", 8) 
#fonction pour trouver le chat le plus vieux parmi les trois chats
def Trouver_le_chat_le_plus_vieux(chat1, chat2, chat3):
        age_du_chat_leplus_vieux = max(chat1.age, chat2.age, chat3.age)
        if age_du_chat_leplus_vieux == chat1.age:
            return chat1
        elif age_du_chat_leplus_vieux == chat2.age:
            return chat2
        else:
            return chat3

oldest_cat = Trouver_le_chat_le_plus_vieux(chat1, chat2, chat3)

print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")


#Exercice 2
#créer une classe Dog
class Dog:
    #initialiser les attributs name et height
    def __init__(self,name,height):
        self.name = name
        self.height = height
    #créer une méthode pour faire aboyer le chien et une autre pour faire sauter le chien
    def bark(self):
        
        print(f"{self.name} goes woof!")
    #créer une méthode pour faire sauter le chien
    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")
    
#créer deux objets de la classe Dog
davids_dog = Dog("Bilou", 50)
sarahs_dog = Dog("Boby", 20)

#afficher le nom et la taille de chaque chien
print(f"{davids_dog.name} fait {davids_dog.height} cm de taille.")
print(f"{sarahs_dog.name} fait {sarahs_dog.height} cm de taille.")
#faire aboyer et sauter les deux chiens
davids_dog.bark()
davids_dog.jump()

sarahs_dog.bark()
sarahs_dog.jump()
#comparer la taille des deux chiens et afficher un message indiquant s'ils ont la même taille ou pas
comparaison = davids_dog.height == sarahs_dog.height
if comparaison:
    print(f"les chiens {davids_dog.name} et {sarahs_dog.name} ont la même taille")
else:
    print(f"les chiens {davids_dog.name} et {sarahs_dog.name} n'ont pas la meme taille")
    
#Exercice 3
#créer une classe Song
class Song:
    #initialiser l'attribut lyrics
    def __init__(self,lyrics):
        self.lyrics = lyrics
    #Créez une sing_me_a_song()méthode qui affiche chaque élément de la lyricsliste sur une nouvelle ligne
    def sing_me_a_song(self):
        for ligne in self.lyrics:
            print(ligne)
            
#créer un objet de la classe Song avec une liste de paroles
stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])

stairway.sing_me_a_song()

#Exercice 4
#créer une classe Personne
class Zoo:
    def __init__(self,zoo_name):
        self.name = zoo_name
        self.animals = []
    
    def add_animal(self, *new_animals):
        for animal in new_animals:
            if animal not in self.animals:
                self.animals.append(animal)
            else:
                print(f"{animal} est déjà dans la liste des animaux du zoo.")
    #créer une méthode get_animals() qui affiche la liste des animaux
    def get_animals(self):
        print(self.animals)
    #créer une méthode sell_animal() qui vend un animal du zoo
    def sell_animal(self,animal_a_vendre):
        if animal_a_vendre in self.animals:
            self.animals.remove(animal_a_vendre)
        else:
            print(f"{animal_a_vendre} n'est pas dans la liste des animaux du zoo.")
            
    #créer une méthode sort_animals() qui trie la liste des animaux par ordre alphabétique
    def sort_animals(self):
        liste_animal_triee = sorted(self.animals)

        groupes = {}

        for animal in liste_animal_triee:
            premiere_lettre = animal[0].upper()

            if premiere_lettre not in groupes:
                groupes[premiere_lettre] = []

            groupes[premiere_lettre].append(animal)
        return groupes
    #créer une méthode get_groups() qui affiche les groupes d'animaux triés par ordre alphabétique
    def get_groups(self):
        groupes = {}
        for animal in self.animals:
            premiere_lettre = animal[0].upper()
            if premiere_lettre not in groupes:
                groupes[premiere_lettre] = []
            groupes[premiere_lettre].append(animal)
        return groupes  
        
   
brooklyn_safari = Zoo("Brooklyn Safari")

# Step 3: Use the Zoo methods
brooklyn_safari.add_animal("Giraffe")
brooklyn_safari.add_animal("Bear")
brooklyn_safari.add_animal("Baboon")
brooklyn_safari.get_animals()
brooklyn_safari.sell_animal("Bear")
brooklyn_safari.get_animals()
brooklyn_safari.sort_animals()
brooklyn_safari.get_groups()