#Exercice 1
print(("Hello world\n") * 4)

#Exercice 2
resultat = (99**3)*8
print(f"Le resultat est : {resultat}")

#Exercice 3
name = "Ziao"
age = 20
shoes_size = 42
#afficher les informations de l'utilisateur
info  = "Mon nom est " + name + ", j'ai " + str(age) + " ans et ma pointure est " + str(shoes_size) + ""
print(info)


#Exercice 4
computer_brand ="hp"
print("I have a " + computer_brand + " computer")

#Exercice 5
name = "Ziao"
age = 20
shoes_size = 42
#afficher les informations de l'utilisateur
info  = "Mon nom est " + name + ", j'ai " + str(age) + " ans et ma pointure est " + str(shoes_size) + ""
print(info)

#Exercice 6
a = 30
b= 20
#verifier si a est plus grand que b
if a > b:
    print("Hello World")
    
#Exercice 7
#entrer un nombre et vérifier si c'est un nombre pair ou impair
entrer_utilisatteur = input("Veuillez entrer un nombre : ")
#convertir le nombre en entier
nombre_int = int(entrer_utilisatteur)
#verifier si le nombre est pair ou impair
if nombre_int % 2 == 0:
    print("Le nombre est pair")
else:    
    print("Le nombre est impair")
    
#Exercice 8
#enter utilisateur et vérifier si c'est le bon nom
nom = input("Quel est votre nom ? ")
nom_utilisateur = "ziao"
#verifier si le nom est correcte
if nom.lower() == nom_utilisateur:
    print("Woahou le nom est correcte")
else:
    print("Nom incorrect")


#Exercice 9
#entrer taille et vérifier si la personne est assez grande pour monter à cheval
taille = input("Quelle est votre taille en cm ? ")
taille_int = int(taille)
#verifier si la personne est assez grande pour monter à cheval
if taille_int > 145:
    print("Vous êtes assez grand pour monter à cheval")
else:
    print("vous devez grandir pour monter à cheval")
