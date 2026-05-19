#entrer un nombre et vérifier si c'est un nombre pair ou impair
entrer_utilisatteur = input("Veuillez entrer un nombre : ")
#convertir le nombre en entier
nombre_int = int(entrer_utilisatteur)
#verifier si le nombre est pair ou impair
if nombre_int % 2 == 0:
    print("Le nombre est pair")
else:    
    print("Le nombre est impair")