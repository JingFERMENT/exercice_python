# Ecrire un algorithme qui demande un nombre à l’utilisateur puis affiche un message l’informant si la valeur est positive ou négative (le cas du zéro est mis de côté).

# Signe d’une variable
value = input(input("Entrez un nombre: "))

if value > 0:
    print("La valeur est positive")
elif value == 0:
    print("La valeur est 0.")
else:
    print("La valeur est négative.")
