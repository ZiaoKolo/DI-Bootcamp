#enter utilisateur et vérifier si c'est le bon nom
nom = input("Quel est votre nom ? ")
nom_utilisateur = "ziao"
#verifier si le nom est correcte
if nom.lower() == nom_utilisateur:
    print("Woahou le nom est correcte")
else:
    print("Nom incorrect")