# Écrire un algorithme qui demande à l'utilisateur son âge puis son genre.
# En fonction des réponses de celui-ci, afficher une phrase telle que :
# "Bonjour Madame. Vous êtes majeure."
# PS : On se limitera pour cet exercice à Homme et Femme

input_age = int(input("Quel est votre âge ?"))
input_gender = input("Vous êtes ?")


def my_result (input_age, input_gender):
    if input_gender == "Femme" and input_age >= 18:
        print("Bonjour Madame.Vous êtes majeure.")
    elif input_gender == "Homme" and input_age >= 18:
        print ("Bonjour Monsieur.Vous êtes majeure.")
    else:
        print("Bonjour.Vous êtes mineur.")

my_result(input_age, input_gender)