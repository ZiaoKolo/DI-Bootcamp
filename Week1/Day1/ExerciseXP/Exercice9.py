#entrer taille et vérifier si la personne est assez grande pour monter à cheval
taille = input("Quelle est votre taille en cm ? ")
taille_int = int(taille)
#verifier si la personne est assez grande pour monter à cheval
if taille_int > 145:
    print("Vous êtes assez grand pour monter à cheval")
else:
    print("vous devez grandir pour monter à cheval")