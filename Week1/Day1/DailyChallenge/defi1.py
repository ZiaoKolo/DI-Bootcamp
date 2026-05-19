number = int(input("Veuillez entrer un nombre : "))
lenght = int(input("Entrer la taille de la liste: "))

list = []
for i in range(lenght):
    list.append(number*(i+1))

print(f"number :{number} - lenght : {lenght} ➞   {list}")