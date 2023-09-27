#Créer une fonction nommée "average" qui attend 2 nombres en arguments.
nb1 = int(input("Entrez le premier nombre:"))
nb2 = int(input("Entrez le 2ème nombre:"))

def my_calcul (nb1, nb2):
   #calculer la moyenne de ces 2 nombres.
   averge =  (nb1 + nb2) / 2 
   return (f"La moyenne de {nb1} et {nb2} est {averge}")

# affichage dans le terminal
print(my_calcul(nb1,nb2))