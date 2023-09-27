age = int(input("Entrez votre âge:"))
# isnumberic

if age >= 8 and age <= 9:
    category = "Microbe"
elif age >= 10 and age <= 11:
    category = "Poussin"
elif age >=12 and age <= 13:
    category = "Benjamine/benjamin"
elif age >=14 and age <= 15:
    category = "Minime"
elif age >=16 and age <= 17:
    category = "Cadette/cadet"
elif age >=18 and age <= 19:
    category = "Junior"
elif age >=20 and age <= 39:
    category = "Sénior"
else:
    category = "Vétérane/vétéran"

print(f"vous êtes dans la catégorie de {category}")
# définir la variable categorie et faire un print une seule fois
