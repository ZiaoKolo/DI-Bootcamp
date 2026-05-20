#Defi 1
#entrée de l'utilisateur
mot_utilisateur = input("Entrez un mot : ")
dictionnaire = {}
#boucle pour parcourir chaque caractère du mot et enregistrer les indices dans le dictionnaire
for i, chaine in enumerate(mot_utilisateur):
    if chaine in dictionnaire:
        dictionnaire[chaine].append(i)
    else:
        dictionnaire[chaine] = [i]
print(f"“{mot_utilisateur}”, the output should be: {dictionnaire}")

#Defi 2

items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$300"

basket =[]

for article, prix in items_purchase.items():
    #nettoyage des données pour convertir les prix en entiers
    prix_apres_nettoyage = prix.replace("$", "").replace(",", "")
    prix_entier = int(prix_apres_nettoyage)
    porteffeille_entier = int(wallet.replace("$", ""))
    #vérification si le prix de l'article est inférieur ou égal au montant dans le portefeuille
    if prix_entier <= porteffeille_entier:
        basket.append(article)
        wallet = f"${porteffeille_entier - prix_entier}"
#affichage du résultat
if len(basket) == 0:
    print("Nothing")
else:    
    print(sorted(basket))
    

