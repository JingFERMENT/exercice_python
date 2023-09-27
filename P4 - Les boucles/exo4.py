# ["Python", "Javascript", "Java", "PHP", "C++", "Cobol"] 
# Réaliser un algorithme qui affiche cette liste 

# listes  
languages = ["Python", "Javascript", "Java", "PHP", "C++", "Cobol"] 

### BOUCLE FOR 
print ("Boucle FOR : ")
for language in languages:
    print(language)

### BOUCLE WHILE
language = 0
# nombre d'éléments dans le tableau
length_of_languages = len(languages)

print ("Boucle WHILE : ")
while language < length_of_languages :
    print(languages[language])
    language += 1 # incrémentation # boucle de sortie
    # language = language + 1
