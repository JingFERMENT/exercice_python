# qui doit retourner l’addition ou la soustraction de plusieurs chiffres. 
# Vous devrez passer en paramètre le type d’opération ainsi que les chiffres sur lesquels effectuer l’opération. Le nombre de ces chiffres sera indéfini

# Créer une fonction "my_calcul"
def my_calcul (operation_type, input_numbers):
    # mettre une condition pour l'addition
    if operation_type == '+' :
        # initier la valeur de l'addition
        sum = 0
        # faire une boucle dans le tableau des chiffres pour avoir chaque chiffre
        for number in input_numbers:
            # ajouter à chaque fois un chiffre lors du passage de boucle 
            sum = sum + number        
        return sum
    
    if operation_type == '-':
        # le chiffre départ est le 1er chiffre dans un tableau des chiffres, donc l'index 0 du tableau des chiffres
        substraction = input_numbers[0]
        # faire une boucle pour avoir chaque chiffre du tableau pour pouvoir utiliser dans la soustraction 
        for i in range (1,len(input_numbers)):
            # ajouter à chaque fois un chiffre lors du passage de boucle
            substraction = substraction - input_numbers[i]
        return substraction
        
   
print(my_calcul('+', [200, 2, 2, 2, 1]))
