date_anniversaire = input("Entrez votre date de naissance (format DD/MM/YYYY) : ")
date = date_anniversaire.split("/")
age = 2026 - int(date[2])
if str(age)[-1] == str(age)[-1]:
    nombre_bougies = age % 10
print(f"""
      ___{ "i" * nombre_bougies }___
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~
"""
)    

