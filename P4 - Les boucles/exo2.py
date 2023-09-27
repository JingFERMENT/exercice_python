# Réaliser un algorithme qui demande à l’utilisateur un nombre compris entre 10 et 20. 
# Si le nombre est inférieur à 10, le terminal doit afficher « Plus grand ! », si le nombre excède 20, le terminal doit afficher « Plus petit ! ».

# déclaration d'un variable pour entrer un chiffre
# "input" est une fonction qui permet de récupérer une fonction
asked_nb = int(input("Entrez une valeur entre 10 et 20:"))

while (asked_nb < 10 or asked_nb > 20):
    # dans la cas où le nombre est inférieur à 10
    if (asked_nb < 10):
        print ("Plus grand!")    
    # comme c'était indiqué dans la condition "while", donc "else" signfie que dans la cas où le nombre est supérieur à 20   
    else:
        print("Plus petit!")
    asked_nb = int(input("Entrez une autre valeur entre 10 et 20:"))
