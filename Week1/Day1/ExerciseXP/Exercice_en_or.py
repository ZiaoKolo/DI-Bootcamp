"""#Exercice 1
mois = input("Entrez un mois : ")

mois_int = int(mois)

if mois_int >=3 and mois_int <=5:
    print("C'est le printemps")
elif mois_int >=6 and mois_int <=8:
    print("C'est l'été")
elif mois_int >=9 and mois_int <=11:
    print("C'est l'automne")
else:
    print("C'est l'hiver")
    

#Exercice 2

for i in range(21):
    print(i)

for i in range(21):
    if i % 2 == 0:
        print(i)
    
#Exercice 3

while True:
    nom = input("Quel est votre nom ? ")
    if nom.lower() == "ziao":
        print("Woahou le nom est correcte")
        break
    print("Nom incorrect, veuillez réessayer.")
"""

#Exercice 4

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

name = input("Entrez un nom : ")

if name in names:
    print(f"{name} est dans la liste avec index{names.index(name)}")
else:
    print(f"{name} n'est pas dans la liste")
    
#Exercice 5
a = int(input("Entrez un nimbre :"))
b = int(input("Entrez un nimbre :"))
c = int(input("Entrez un nimbre :"))

if a > b and a > c:
    print(f"{a} est le plus grand")
    if b > c:
        print(f"{b} est le deuxième plus grand")
        print(f"{c} est le plus petit")
    else:
        print(f"{c} est le deuxième plus grand")
        print(f"{b} est le plus petit")
elif b > a and b > c:
    print(f"{b} est le plus grand")
    if a > c:
        print(f"{a} est le deuxième plus grand")
        print(f"{c} est le plus petit")
    else:
        print(f"{c} est le deuxième plus grand")
        print(f"{a} est le plus petit")
else:
    print(f"{c} est le plus grand")
    if a > b:
        print(f"{a} est le deuxième plus grand")
        print(f"{b} est le plus petit")
    else:
        print(f"{b} est le deuxième plus grand")
        print(f"{a} est le plus petit")
        
#Exercice 6
import random
nombre = int(input("Entrez un nombre entre 1 et 9 : "))
nombre_aleatoire = random.randint(1, 9)
if nombre == nombre_aleatoire:
    print("vous avez trouvez le nombre")
else:
    print(f"vous n'avez pas trouvez le nombre. Le nombre était {nombre_aleatoire}")
