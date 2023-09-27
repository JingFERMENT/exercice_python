# # Réaliser un algorithme qui demande à l’utilisateur un chiffre compris entre 1 et 3. 
# # Si la saisie n’est pas un chiffre compris entre 1 et 3, votre algorithme devra redemander une nouvelle saisie.
# # on connait le nombre d'iteration => for, sinon "while"

# # déclarer la variable puis initialiser
asked_nb_user = 0

# #tant que le chiffre n'est pas compris entre 1 et 3
while (asked_nb_user > 3 or asked_nb_user < 1):
     asked_nb_user = int(input("Entrez un chiffre entre 1 et 3 :"))
