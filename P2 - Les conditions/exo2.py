# Ecrire un algorithme qui demande deux nombres à l’utilisateur puis affiche un message l’informant si le produit des deux nombres est positif ou négatif sans faire le calcul (le cas ou les nombres sont des zéros est mis de côté).

# Signe du produit de deux valeurs
value1 = float(input("Entrez un 1er nombre:"))
value2 = float(input("Entrez un 2ème nombre:"))

if value1 == 0 or value2 == 0:
    print("La valeur est à 0")
elif (value1 > 0 and value2 > 0) or (value1 < 0 and value2 < 0):
    print("La valeur est positive.")
else:
    print("La valeur est négative.")
