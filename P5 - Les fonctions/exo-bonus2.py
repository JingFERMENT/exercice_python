# Écrire un algorithme qui permettra de faire le modulo de 2 nombres, puis de multiplier le résultat par 60.
# Le calcul du modulo devra se faire dans une fonction ModuloNumbers qui sera à appeler dans l'algorithme
# principal

def my_calcul (nb1, nb2):
    ModuloNumbers = nb1 % nb2
    return ModuloNumbers

def principal (nb):
    total = nb * 60 
    return total

print(principal(my_calcul(25,3)))
