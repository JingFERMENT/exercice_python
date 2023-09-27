# indiquer le nombre de photocopie
nb_copy = int(input("Indiquer le nombre de photocopie dont vous avez besoin:"))

# quand le nombre n'est pas bon
if nb_copy <= 0:
    print("Le nombre de photocopie n'est pas bon.")

# quand le nombre est bon
else:
    # pour les 10 premiers photocopies
    if nb_copy <= 10 and nb_copy > 0:
        price = nb_copy * 0.1   
    # pour les 20 premiers photocopies
    elif nb_copy <= 30 and nb_copy > 10:
        price = 10 * 0.1 + (nb_copy - 10) * 0.09
    # pour plus de 30 photocopies
    elif nb_copy > 30 :
        price = (nb_copy - 30) * 0.08 + 20 * 0.09 + 10 * 0.1 

print(f"la facture pour {nb_copy} photocopies est de {price}€.")
