#Exercice 1

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
#concatenation de la liste keys et de la liste values
concatenation_k_v = zip(keys, values)
#convertir la concatenation en dictionnaire
dictionnaire = dict(concatenation_k_v)
print(dictionnaire)


#Exercice 2
#dictionnaire de la famille avec les ages
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
somme =0
#calculer le prix des billets pour chaque membre de la famille et faire la somme totale
for nom, valeur in family.items():
    if valeur < 3:
        print(f"le billlet est gratuit pour {nom}")
        somme += 0
    elif 3 <= valeur < 12:
        print(f"le billlet est de 10$ pour {nom}")
        somme += 10
    else:
        print(f"le billlet est de 15$ pour {nom}")
        somme += 15

print(f"le prix total est des billets est {somme}")

#Exercice 3
#dictionnaire de la marque Zara
brand ={
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": ["blue"],
        "Spain": ["red"],
        "US": ["pink", "green"]
    }
}
#ajouter un élément au dictionnaire
brand["number_stores"] = 2
#afficher le type de vêtements que les clients de Zara peuvent acheter
print(f"Les types de vêtements que les clients de Zara peuvent acheter sont: {brand['type_of_clothes']}.")
#ajouter un élément au dictionnaire
brand["country_creation"] = "Spain"

for element, valeur in brand.items():
    if element == "international_competitors":
        valeur.append("Desigual")

del brand["creation_date"]

print(brand["international_competitors"][-1])

print(brand["major_color"]["US"])

print(len(brand.keys()))
for cle in brand.keys():
    print(cle)
    
#autre dictionnaire de la marque Zara
more_on_zara ={
    "creation_date": 1970,
    "number_stores": 10005
}
#concatenation de brand et de more_on_zara
concatenation = zip(brand.items(),more_on_zara.items())
concatenation_dict = dict(concatenation)
print(concatenation_dict)

#Exercice 4
#definition de la fonction
def describe_city(city, country="unknown"):
    print(f"{city} is in {country}.")
#appel de la fonction    
describe_city("Reykjavik", "Iceland")
describe_city("Paris")


#Exercice 5
from calendar import month
import random

#Créez une fonction qui accepte un nombre compris entre 1 et 100 comme paramètre.
def generer_nombre_aleatoire(nombre):
    nombre_aleatoire =random.randint(1, 100)
    if nombre == nombre_aleatoire:
        print("Success! (if the numbers match)")
    else:
        print(f"Fail! Your number: {nombre}, Random number: {nombre_aleatoire} (if they don't match)")
        
        
generer_nombre_aleatoire(50)

#Exercice 6

#definition de la fonction
def make_shirt(size="large", text="I love Python"):
    print(f"The size of the shirt is {size} and the text is {text}.")
#appel de la fonction    
make_shirt("large", "I love Python")
make_shirt("medium", "I love Python")
make_shirt("small", "Custom message")

#Exercice 7
import random

#definition de la fonction
def get_random_temp(mois):
    if mois in [12, 1, 2]:
        return random.uniform(-10, 0)
    elif mois in [3, 4, 5]:
        return random.uniform(0, 16)
    elif mois in [6, 7, 8]:
        return random.uniform(16, 23)
    elif mois in [9, 10, 11]:
        return random.uniform(23, 32)
#appel de la fonction dans la fonction main
def main():
    mois = int(input("Entrer un mois en entier (1-12): "))
    temperature = get_random_temp(mois)
    print(f"The temperature right now is {temperature} degrees Celsius.")
    if temperature < 0:
        print("Brrr, that’s freezing! Wear some extra layers today")
    elif 0 <= temperature < 16:
        print("Quite chilly! Don’t forget your coat")
    elif 16 <= temperature < 23:
        print("Nice weather.")
    elif 24 <= temperature < 32:
        print("It's a bit hot, remember to stay hydrated.")
    else:
        print("It's really hot! Stay cool.")

main()


#Exercice 8
#liste des ingrédients de la pizza et le prix de la pizza
liste_ingredients=[]
prix_de_pizza = 10.0
#demander à l'utilisateur d'entrer des ingrédients pour sa pizza jusqu'à ce qu'il entre "quit"
while True:
    ingredient = input("entrer un ingredient pour votre pizza: ")
    liste_ingredients.append(ingredient)
    prix_de_pizza += 2.5
    print(f"Adding {ingredient} to your pizza.")
    if ingredient == "quit":
        break
liste_finale =liste_ingredients[:-1]  # Exclure "quit" de la liste finale
print(f"les ingredients de votre pizza sont: {liste_finale}. Le prix de votre pizza est {prix_de_pizza}$.")



