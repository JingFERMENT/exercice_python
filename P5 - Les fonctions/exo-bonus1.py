# Soit un tableau contenant 10 nombres.
# Écrire un algorithme qui permettra de faire la multiplication de ces 10 nombres entre eux
# et d'affecter le résultat à une variable resultCalc

def multiplication (array):
    resultCalc = array[0]
    for i in range(1, len(array)):
        resultCalc = resultCalc * array[i]
    return resultCalc

print(multiplication([1, 2, 3, 4, 5, 1, 1, 1, 1, 1]))