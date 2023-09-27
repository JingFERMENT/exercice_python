# Soit le tableau suivant:
# [['Steve', 'Jobs'], ['Elon', 'Musk'], ['Jeff', 'Bezos'], ['Mark', 'Zuckerberg']]
# Afficher 'Steve', puis 'Musk', et enfin 'Zuckerberg Mark'

# déclaration des variables avec un tableau
famous_name = [['Steve', 'Jobs'], ['Elon', 'Musk'], ['Jeff', 'Bezos'], ['Mark', 'Zuckerberg']]

# afficher les prénoms et les noms
print(famous_name[0][0])
print(famous_name[1][1])
# option 1
print(f"{famous_name[3][1]} {famous_name[3][0]}")
# option 2
print(famous_name[3][1] + ' ' + famous_name[3][0])