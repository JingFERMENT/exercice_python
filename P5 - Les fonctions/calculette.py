# qui doit retourner l’addition ou la soustraction de plusieurs chiffres. 
# Vous devrez passer en paramètre le type d’opération ainsi que les chiffres sur lesquels effectuer l’opération. Le nombre de ces chiffres sera indéfini

# Créer une fonction "my_calcul"
# * sous fous de tableau
def my_calcul (operation_type, *numbers):
    # mettre une condition pour l'addition
    if operation_type == '+' :
            # total = sum(input_numbers)
            # return total
        sum_result = 0
        for number in numbers:
            sum_result = sum_result + number        
        return sum_result

    if operation_type == '-':
        # le chiffre départ est le 1er chiffre du tableau
        substraction = numbers[0]
        # pour avoir chaque chiffre afin d'utiliser dans la soustraction 
        # numbers[1:] chercher la valeur de l'index de 1 à la fin de l'index
        for i in numbers[1:]:
        # for i in range (1,len(numbers)):
            substraction = substraction - i
            # substraction = substraction - numbers[i]
        return substraction
        
print(my_calcul("-", 200, 2, 2, 2, 1))
