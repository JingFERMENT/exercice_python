#Ecrire deux algorithmes qui demandent un nombre de départ, puis affiche les dix nombres suivants. 
#L’un des algorithmes doit utiliser une boucle for, l’autre une boucle while. 
#Par exemple, si l'utilisateur entre le nombre 17, le programme affichera les nombres 18 à 27.


### BOUCLE FOR
nb = int(input("Entrez un chiffre entier: "))

print ("Boucle for :")
for i in range (nb+1, nb+11):
    print(i)

### BOUCLE WHILE
print ("Boucle while :")
new_nb = nb + 1

while new_nb < nb+11:
    print(new_nb)
    new_nb = new_nb + 1