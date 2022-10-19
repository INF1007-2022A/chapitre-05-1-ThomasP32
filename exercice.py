#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List

#Écrire un programme qui lit un nombre et affiche sa valeur absolue, sans utiliser de fonction avancée
def convert_to_absolute(number: float) -> float:
    absolu = number * -1
    return absolu 

#Écrire un petit script qui génère tous ces noms à partir des deux chaînes suivantes : prefixes = 'JKLMNOPQ' et suffixe = 'ack'
def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    new_list = []
    for lettre in prefixes:
        new_list.append(lettre + suffixe)
    
    return new_list

#Calculer la somme des 100 premiers nombres entiers premiers excluant le nombre 1
def prime_integer_summation() -> int:
   
        
    return 0

#Calculer la factorielle d’un nombre entier, sans utiliser de fonction avancée
def factorial(number: int) -> int:
    factorielle = 1
    for i in range(2, number+1):
        factorielle *= i
    return factorielle

#Utiliser l’instruction 'continue' pour modifier une boucle for d’affichage de tous les entiers de 1 à 10 compris, 
#sauf lorsque la variable de boucle vaut 5
def use_continue() -> None:
    for nbr_entier in range(1, 11):
        if nbr_entier == 5:
            continue
        print (nbr_entier)

def verify_ages(groups: List[List[int]]) -> List[bool]:
    acceptable = []
    for group in groups:
        if 25 in group:
            acceptable.append(True) 
            continue
        elif len(group) > 10 or len(group) <= 3:
            acceptable.append(False)
            continue
        elif max(group) > 70 and 50 in group or min(group) < 18:
            acceptable.append(False)
            continue

    return acceptable

        
    

    

    #critere dage
    return []


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
