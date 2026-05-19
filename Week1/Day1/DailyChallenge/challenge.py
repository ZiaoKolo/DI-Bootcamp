#defi1
#Créer une liste de multiples d’un nombre donné, jusqu’à une certaine longueur.
number = int(input("Veuillez entrer un nombre : "))
lenght = int(input("Entrer la taille de la liste: "))
#créer la liste des multiples du nombre donné
list = []
for i in range(lenght):
    list.append(number*(i+1))

print(f"number :{number} - lenght : {lenght} ➞   {list}")

#defi2
#Supprimer les lettres consécutives d’un mot donné.
user_word = input("Entrez un mot : ")
new_word = ""
for i in range(len(user_word)):
    if i == 0 or user_word[i] != user_word[i-1]:
        new_word += user_word[i]
print(f"user's word : {user_word} ➞ {new_word}")

