import string
import enum
from math import pi
import time
import random
import constants
import os
import random

###################
# Niveau Debutant #
###################

print("Exercice 1")
# Exercice 1
# Notion abordees : les variables
# On commence simple avec ce premier exercice, qui consiste à declarer differents types de variables.

# La variable 'prenom' qui doit contenir la chaine de caractere Pierre.
# La variable 'age' qui doit contenir 20.
# La variable 'majeur' qui doit contenir un boolean vrai.
# La variable 'compte_en_banque' qui doit contenir le nombre à virgule 20135,384.
# La variable 'amis' qui doit contenir une liste contenant trois chaines de caracteres: Marie, Julien, Adrien.
# La variable 'parents' qui doit contenir un tuple contenant deux chaines de caracteres: Marc et Caroline
##
# prenom = "Pierre"
# age = 20
# majeur = True
# compte_en_banque = 20135.384
# amis = ["Marie", "Julien", "Adrien"]
# parents = ("Marc", "Caroline")
# print(prenom)
# print(age)
# print(majeur)
# print(compte_en_banque)
# print(amis)
# print(parents)
"""
        EXPLICATION

   Dans cet exercice, il suffisait de déclarer les différents types de variable demandés.

       POINTS IMPORTANTS À RETENIR

   - Une chaîne de caractère doit être entourée de deux guillemets. Les guillemets peuvent être simples (') ou doubles ("). Vous ne pouvez pas commencer avec des guillemets simples et finir avec des guillemets doubles et vice-versa.

   - Un booléen commence par une majuscule et peut contenir deux valeurs, True ou False.

   Si vous essayez de créer un booléen en écrivant true ou false vous obtiendrez une erreur de syntaxe.

   - Pour définir un nombre décimal, on utilise le point (.) et non pas la virgule.

   La virgule sert à séparer les éléments les uns des autres.

   Si vous essayez de créer un nombre à virgule avec une virgule au lieu d'un point, vous vous retrouverez avec un tuple contenant les deux nombres de chaque côté de la virgule.

   Voyez plutôt :

       nombre = 123,456
       >>> (123, 456)
       nombre = 123.456
       >>> 123.456

   - Pour définir une liste, on utilise les crochets : [ ]
   - Pour définir un tuple, on utilise les parenthèses : ( )
   """

print("\nExercice 2")
# Exercice 2
# Notion abordees: les variables
# Une erreur s'est glissee dans la declaration de la variable 'site_web', à vous de la trouver et de la corriger pour que le script affiche
# le nom du site web.

# site_web = 'Udemy'
# print(site_web)
##
# site_web = "Udemy"
# print(site_web)
"""
    SOLUTION

    site_web = "Udemy"
    print(site_web)

    EXPLICATION

Quand vous déclarez une variable de type chaîne de caractères, vous devez utiliser le même type de guillemet en ouverture et fermeture. Il existe deux types de guillemets, les simples et les doubles. Vous pouvez utiliser les deux sans problèmes tant que vous ne les mélangez pas.

    POINTS IMPORTANTS À RETENIR

    Pour définir une chaîne de caractère, il faut utiliser le même type de guillemet en ouverture et fermeture.
"""

print("\nExercice 3")
# # Exercice 3
# # Notions abordees: les variables
# # Dans cet exercice, nous allons afficher un nombre à l'interieur d'une chaine de caractere.
# # Pythom ne permet pas de concatener une chaine de caracteres avec un nombre, il va donc falloir convertir le nombre en chaine de
# # caractere.
# nombre = 15
# print("Le nombre est " + str(nombre))
"""
    SOLUTION

    nombre = 15
    print("Le nombre est " + str(nombre))

    EXPLICATION

Là encore un exercice très simple pour ceux qui sont habitués à Python.

Dans Python, on ne peut pas concaténer des variables de différents types. Ainsi, si on essaie d'additionner une chaîne de caractères avec un nombre, on se retrouve avec une erreur :

    >>> nombre = 15
    >>> print("Le nombre est " + nombre)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: must be str, not int

L'erreur ci-dessus nous indique que le type de la variable 'nombre', pour être concaténé avec la chaîne de caractère 'Le nombre est ', doit être de type 'str' (chaîne de caractère) et non pas 'int' (nombre entier).

Pour remédier à ce problème, on convertit donc notre nombre 15, par la chaîne de caractère '15', grâce à la fonction str.

    POINTS IMPORTANTS À RETENIR

- Pour convertir un nombre en chaîne de caractère, on utilise la fonction str.

- Pour convertir une chaîne de caractère en nombre, on utilise la fonction int.
Attention : si vous essayez de convertir une chaîne de caractère qui ne contient pas un nombre en 'integer' avec la fonction int, vous aurez une erreur :

    >>> int("Udemy")
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: invalid literal for int() with base 10: 'Udemy'

Pour vérifier si une chaîne de caractère ne contient que des chiffres, vous pouvez utiliser la méthode isdigit :

    >>> "Udemy".isdigit()
    False
    >>> "2018".isdigit()
    True
    >>> 
"""

print("\nExercice 4")
# Exercice 4
# Notions abordees: les variables
# Pour reussir l'exercice, vous devez printer la valeur que contient la variable 'a'.
##
# a = 3
# b = 6
# a = b
# b = 7
# # trouver la valeur de a
# print(6)

"""
    SOLUTION

    a = 3
    b = 6
    a = b
    b = 7
     
    print(6)

    EXPLICATION

Ici, on déclare deux variables, a et b, qui contiennent des valeurs différentes.

On déclare de nouveau la variable a à la troisième ligne et on lui assigne la valeur de b (donc 6).

Ensuite on modifie la valeur de la variable b, mais cela ne modifie en rien la valeur de la variable a.
Les deux variables sont distinctes et on peut modifier les valeurs contenues dans l'une et dans l'autre sans affecter l'autre variable.
"""

print("\nExercice 5")
# # Exercice 5
# # Notions abordees: La fonction print.
# # Dans cette exercice, nous allons utiliser les nouvelles fonctionnalites de python 3, afin de printer les 3 variables a, b et c, separees par un symbole d'addition(+)
# a = 2
# b = 6
# c = 3
# print(a, b, c, sep=" + ")

"""
    SOLUTION

    a = 2
    b = 6
    c = 3
    print(a, b, c, sep=" + ")

    EXPLICATION

Depuis la version 3 de Python, la fonction print accepte un paramètre 'sep' qui permet de séparer les éléments que l'on print par une chaîne de caractère.

Ici, nous séparons donc les trois variables que nous affichons avec la fonction print, par la chaîne de caractère " + ", ce qui permet d'afficher le résultat suivant : 2 + 6 + 3 
"""

print("\nExercice 6")
# Exercice 6
# Notions abordees: les variables
# Le but de cet exercice est de trouver et reparer l'erreur presente dans le code.
# Vous devez modifier le code dans la console afin de ne plus avoir d'errers lors de l'execution du script.
# Vous ne devez pas toucher à la fonction print, juste a declaration des variables
# list = range(3)
# list2 = range(5)
# print(list(list2))
list1 = range(3)
list2 = range(5)
print(list(list2))

"""
    SOLUTION

    list1 = range(3)
    list2 = range(5)
    print(list(list2))

    EXPLICATION

Le problème qui survient dans le script de départ vient du fait que nous assignons 'range(3)' dans une variable qui est déjà utilisée par Python pour convertir un objet en liste (la fonction list).

Ainsi, quand nous essayons de convertir la liste 'list2', avec la fonction list, nous avons une erreur :

    >>> list = range(3)
    >>> list2 = range(5)
    >>> list(list2)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'range' object is not callable

En écrasant le mot réservé 'list' par 'range(3)', nous écrasons la fonction list et quand nous voulons l'utiliser plus loin dans notre script, Python essaie de convertir notre liste 'list2' avec l'objet 'range' contenu à l'intérieur de la variable 'list' au lieu d'utiliser la fonction list.

    POINTS IMPORTANTS À RETENIR

- Il faut faire très attention à ne pas écraser des noms réservés par Python.

- Voici une liste non-exhaustive des noms réservés par Python :

    False               def                 if                  raise
    None                del                 import              return
    True                elif                in                  try
    and                 else                is                  while
    as                  except              lambda              with
    assert              finally             nonlocal            yield
    break               for                 not                 
    class               from                or                  
    continue            global              pass 

À cette liste vous pouvez ajouter toutes les fonctions de base de Python, comme la fonction str, la fonction int, la fonction dict, la fonction print, la fonction list etc...
"""

print("\nExercice 7")
# Exercice 7
# Notions abordees: Les variables
# Dans cette exercice, vous allez devoir verifier que la variable 'prenom' est bien une chaine de caracteres.
# La variable prenom est definie au debut du script par une chaine de caractere.
# Votre script doit donc printer une premiere fois la phrase "La varaible est une chaine de caracteres".
# La variable prenom est ensuite redefinie est assignee au nombre 0.
# Vous devez donc tester de nouveau votre condition mais cette fois-ci, votre script ne doit pas printer la phrase.
# prenom = "Pierre"
# INSERER VOTRE CONDITION ICI.
# Votre condition doit verifier si la variable est bien une chaine
# de caractere. Ici c'est le cas,
# votre condition doit donc etre vraie et printer la phrase "La variable
# est une chaine de caracteres".
# prenom = 0
# INSERER VOTRE CONDITION DE NOUVEAU
# Cette fois-ci, la variable n'est pas egale à une chaine de caractere.
# Votre condition doit donc etre fausse et la phrase ne doit pas s'afficher.
##
# prenom = "Pierre"

# if (isinstance(prenom, str)):
#     print("La variable est une chaîne de caractères")
# elif (isinstance(prenom, int)):
#     pass

# prenom = 0
# if (isinstance(prenom, str)):
#     print("La variable est une chaîne de caractères")
# elif (isinstance(prenom, int)):
#     pass
"""
    SOLUTION

    prenom = "Pierre"
     
    if type(prenom) == str:
        print("La variable est une chaîne de caractères")
     
    prenom = 0
     
    if isinstance(prenom, str):
        print("La variable est une chaîne de caractères")

    EXPLICATION

Pour vérifier si une variable est d'un certain type, on peut utiliser la fonction type ou la fonction isinstance.

On vérifie une première fois si la variable "prenom" est de type "str", c'est le cas, la phrase "La variable est une chaîne de caractères" s'affiche donc bien à l'écran.

On redéfinie ensuite la variable "prenom" pour lui assigner le nombre 0.

On vérifie ensuite une deuxième fois avec la fonction isinstance, que la variable "prenom" est bien une instance de la classe "str". Cette fois-ci, la variable "prenom" étant égale à un nombre entier (int), la phrase ne s'affiche pas.

Dans un exemple simple comme celui-ci, le résultat est similaire. Il est cependant préférable d'utiliser la fonction isinstance, car elle fonctionnera également si vous vérifier le type d'une variable qui hérite d'une classe qui est du type que vous cherchez.

    >>> default_dict = {}
     
    >>> type(default_dict)  # Notre dictionnaire est bien de type 'dict'
    <type 'dict'>
     
    >>> class CustomDict(dict):  # On créé une classe custom, qui hérite de la classe 'dict'
    ...     pass
     
    >>> custom_dict = CustomDict()
     
    >>> type(custom_dict)
    <class '__main__.CustomDict'>
     
    # Avec la fonction type(), notre dictionnaire custom n'est pas reconnu comme étant de type 'dict'
    >>> type(custom_dict) == dict
    False                     
     
    # La fonction isinstance en revanche comprend que notre dictionnaire custom hérite de la classe 'dict'
    >>> isinstance(custom_dict, dict)
    True                      

    POINTS IMPORTANTS À RETENIR

- Pour vérifier le type d'une variable, on peut utiliser la fonction type ou la fonction isinstance. On préfèrera la fonction isinstance qui gère l'héritage.
"""

# print("\nExercice 8")


# Exercice 8
# Notions abordees: Les chaines de caractere.
# Dans cet exercice, vous devez remplacer le mot 'Bonjour' dans la variable 'phrase' par le mot 'Bonsoir' à l'aide d'une fonction Python.
# Vous devez donc modifier la variable 'phrase'!
# phrase = "Bonjour tout le monde."
# nouvelle_phrase =
# print(nouvelle_phrase)
##
# phrase = "Bonjour tout le monde."
# nouvelle_phrase = phrase.replace("Bonjour", "Bonsoir")
# print(nouvelle_phrase)
"""

    SOLUTION 

    phrase = "Bonjour tout le monde."
    nouvelle_phrase = phrase.replace("Bonjour", "Bonsoir")
    print(nouvelle_phrase)

    EXPLICATION

Pour remplacer un mot par un autre en Python on utilise la fonction replace.

Le premier argument est le mot à chercher et le second contient ce par quoi on veut le remplacer.

La fonction replace va remplacer toutes les instances de la chaîne de caractère qu'elle trouve dans la phrase. Si vous avez 3 fois le mot "Bonjour", les trois occurrences du mot seront remplacées.

    POINTS IMPORTANTS À RETENIR

Pour remplacer un mot par un autre on utilise la fonction replace.
"""

print("\nExercice 9")
# Exercice 9
# Notions abordees: Les chaines de caracteres.
# Le but de cet exercice est de remettre en ordre alphabetique les prenoms presents dans la chaine de caractere.
# Vous devez donc printer à la fin de l'exercice, la chaine de caractere suivante:
# "Anne, Julien, Lucien, Marie, Pierre"
# chaine = "Pierre, Julien, Anne, Marie, Lucien"
##
# chaine = "Pierre, Julien, Anne, Marie, Lucien".split(", ")
# chaine.sort()
# chaine = ", ".join(chaine)
# print(chaine)
"""

    SOLUTION

    chaine = "Pierre, Julien, Anne, Marie, Lucien"
     
    chaine_liste = chaine.split(", ")
    chaine_liste.sort()
    chaine_en_ordre = ", ".join(chaine_liste)
    print(chaine_en_ordre)

    EXPLICATION

Tout d'abord, il faut séparer les différents prénoms de la chaîne de caractère pour les mettre dans une liste.

En effet, on ne peut pas trier une chaîne de caractère, il va donc falloir passer par une liste.

Pour séparer les différents prénoms, on utilise la fonction split, qui permet de séparer la chaîne de caractère en plusieurs éléments, en opérant la séparation sur la virgule. Vous noterez qu'on a ajouté un espace après la virgule pour ne pas récupérer l'espace dans les prénoms de notre liste.

À ce stade-ci, nous avons donc la liste suivante :

['Pierre', 'Julien', 'Anne', 'Marie', 'Lucien'] 

Il faut maintenant ordonner cette liste, ce que nous faisons à la ligne suivante avec la fonction sort.

chaine_liste.sort() 

Il ne reste plus qu'à joindre de nouveaux les prénoms de la liste avec le caractère que nous avons utilisé précédemment pour réaliser la séparation (une virgule suivie d'un espace). Pour cela, nous utilisons la méthode join.

chaine_en_ordre = ", ".join(chaine_liste) 

    POINTS IMPORTANTS À RETENIR

    On ne peut pas trier une chaîne de caractère.
    Pour séparer une chaîne de caractère en plusieurs éléments, on utilise la fonction split.
    Pour trier une liste, on utilise la fonction sort.
    Pour joindre différents éléments d'une liste par une chaîne de caractère, on utilise la méthode join.
"""

print("\nExercice 10")
# Exercice 10
# Notions abordees: Les operateurs mathematiques.
# Dans cet exercice, nous allons calculer le volume d'une sphere ayant pour rayon 10 centimetres.
# La formule pour calculer le volume d'une sphere est:
# (4pi/3)*rayon au cube
# rayon representant la valeur du rayon (defini dans le code par la variable 'rayon').
# Pour reussir l'exercice, vous devez uniquelment afficher le volume de la sphere, si vous rajoutez du texte en plus l'exercice ne sera pas
# valide (donc il suffit de laisser print(volume) à la fin et de calculer le volume à la ligne d'avant)
##
# rayon = 10.0
# volume = (4*pi)/3 * rayon**3
# print(volume)
"""
SOLUTION

    import math
    rayon = 10.0
    volume = (4.0 * math.pi / 3.0) * (rayon ** 3)
    print(volume)

EXPLICATION

Peu de difficulté dans cet exercice, le seul point sur lequel il fallait porter attention était l'import du module math, qui permet d'obtenir une valeur précise de pi, sans avoir besoin d'entrer le nombre à la main.

Le reste est assez simple, le symbole * permet de multiplier, tandis que le symbole ** permet de calculer le rayon puissance 3. Le symbole pour la division est la barre oblique (/). Pour obtenir le bon résultat, il fallait faire attention également aux parenthèses dans votre calcul.

POINTS IMPORTANTS À RETENIR

    Pour obtenir la valeur de pi, on importe le module math.

    Pour multiplier, on utilise *, pour mettre le rayon à la puissance 3 on utilise ** et pour diviser on utilise /
"""

print("\nExercice 11")
# Exercice 11
# Notions abordees: structures conditionnelles.
# Dans cet exercice, nous allons utiliser une structure conditionnelle pour verifier si a est plus grand ou non que 10.
# Dans ce cas-ci, a est egal à 12, votre script devra donc afficer 'a est plus grand que 10'
# Aller plus loin: Vous pouvez egalement rajouter une condition pour tester si la variable a contient bien un nombre.
# a = 12
##
# a = 12
# if a > 10:
#     print("a est plus grand que 10")
# elif a <= 10:
#     print("a est inferieur ou egal a 10")
"""
    SOLUTION

    a = 12
    if a > 10:
        print("a est plus grand que 10")
    elif a < 10:
        print("a est plus petit que 10")

    EXPLICATION

Exercice très simple pour ceux d'entres-vous qui sont habitués à Python.

Il s'agissait ici de faire une structure conditionnelle de base afin de vérifier si le nombre a était plus grand ou plus petit que 10.

La première condition if a > 10  sera exécutée si a est plus grand que 10.

La seconde condition, exécutée avec le elif a < 10 sera exécutée si a est plus petit que 10.

    POINTS IMPORTANTS À RETENIR

    Pour tester plusieurs conditions, on utilise la structure conditionnelle if, elif.
"""

print("\nExercice 12")
# Exerice 12
# Notions abordees: Les listes.
# Dans cet exercice, on contiue avec des operations assez simples utilisant les bases du langage Python.
# Le but ici est de crrer une liste de nombres allant de 5 à 15 en utilisant une fonction de base de Python.
# Pour valider l'exercice, vous devez afficher cette liste, en utilisant la fonction print.
##
# list1 = []
# for i in range(5, 16):
#     list1.append(i)
# print(list(list1))

"""
    SOLUTION

    liste_de_nombres = range(5, 16)
    print(list(liste_de_nombres))

    EXPLICATION

Pour créer facilement et rapidement des listes de nombres, on utilise la fonction range.

On peut l'utiliser en passant un seul nombre en argument, auquel cas la fonction range va créer une liste allant de 0 jusqu'au nombre indiqué - 1 :

    >>> list(range(10))
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

Vous voyez dans l'exemple ci-dessus, que la liste s'arrête à 9.

On peut également passer deux arguments, pour indiquer à la fonction à partir de quel nombre commencer, comme dans cet exercice :

    >>> list(range(5, 16))
    [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

Là encore, vous remarquerez que la liste s'arrête à 15. Si nous voulons inclure le nombre 15 dans la liste, il faut donc passer en deuxième argument le nombre 16.

Attention ! Depuis Python 3, la fonction range ne retourne pas une liste mais un objet de type 'range'.

Ainsi, si vous voulez afficher cet objet en tant que liste, il vous faudra utiliser la fonction list pour convertir l'objet range en liste.

    POINTS IMPORTANTS À RETENIR

    La fonction range permet de générer une liste de nombres rapidement.
    Depuis Python 3, il faut utiliser la fonction list pour convertir le résultat de la fonction range en liste.
"""

print("\nExercice 13")
# Exercice 13
# Notions abordees: les listes.
# Dans cet exercice, on continue avec la fonction range, cette fois-ci pour creer une liste de nombres pairs allant de 1 à 100.
# Votre script doit afficher la liste, pensez donc à faire un print à la fin, si vous faites juste declarer la liste,
# l'exercice ne sera pas valide
##
# list1 = []
# for i in range(2, 101, 2):
#     list1.append(i)
# print(list(list1))
"""
    SOLUTION

    liste_nombre_pairs = range(2, 101, 2)
    print(list(liste_nombre_pairs))

    EXPLICATION

Dans cet exercice, on pousse un peu plus loin encore la fonction range, en fournissant un troisième argument, qui va indiquer à la fonction range l'écart que l'on veut entre chaque nombre.

Dans cet exemple-ci, on indique un écart de 2, ce qui aura comme effet de ne pas inclure les nombres impairs dans notre liste (puisque l'on commence à 2).

Un dernier point auquel il fallait faire attention là encore : pour intégrer le nombre 100 dans la liste, il fallait indiquer 101 comme deuxième argument, car la fonction range s'arrête à n - 1.

    POINTS IMPORTANTS À RETENIR

    On peut spécifier un écart à la fonction range en passant un nombre en troisième argument.
"""


print("\nExercice 14")
# Exercice 14
# Notions abordees: Les modules, la boucle for.
# Le but de cet exercice est de generer 6 lancer de des aleatoires, allant de 1 à 6.
# Votre script devra donc par exemple retour les lancer suivants:
# 1
# 2
# 3
# 4
# 5
#
##
# for i in range(1, 7):
#     j = random.choice(range(1, 7))
#     print(j)

"""
    SOLUTION

    import random
     
    for _ in range(6):
        nombre = random.choice(range(1, 7))
        print(nombre)

    EXPLICATION

Pour générer des nombres aléatoires, on utilise le module random qui dispose de plusieurs fonctions nous permettant de générer des nombres aléatoires.

Celle que nous utilisons dans le cadre de cette exercice est la fonction 'choice'. Cette fonction nous permet de choisir un élément aléatoire parmi une liste de plusieurs éléments.

Pour générer un nombre aléatoire de 1 à 6, nous utilisons donc la ligne de code suivante :

nombre = random.choice(range(1, 7)) 

Si vous ne voulez pas passer par une liste, vous pouvez également utiliser la fonction randint, comme ceci :

nombre = random.randint(1, 6) 

La deuxième indication de l'exercice était de générer 6 lancer de dés.

Pour cela, on utilise une boucle for et encore une fois la fonction range, pour répéter l'opération 6 fois :

    for _ in range(6):
        # Opération à répéter

Vous remarquerez que nous utilisons un nom de variable assez spécifique (un tiret du bas). En effet, ce nom de variable est une convention en Python lorsque l'on génère une variable que l'on ne compte pas utiliser. Ici, on veut juste répéter une opération un certain nombre de fois, mais nous ne faisons aucun usage de cette variable, nous utilisons donc un tiret du bas pour signifier à quelqu'un qui pourrait lire notre script que cette variable n'est pas utilisée à l'intérieur de la boucle.

    POINTS IMPORTANTS À RETENIR

    Pour récupérer un élément aléatoire dans une liste, on utilise la fonction choice du module random.
"""

print("\nExercice 15")
# Exercice 15
# Notions abordees: Les chaines de caractere.
# Dans cet exercice, nous cherchons à compter le nombre d'occurrence d'une lettre dans une chaine de caractere.
# Ici, nous cherchons le nombre de fois que la lettre "o" apparait dans la phrase "Bonjour tout le monde".
# Votre script devra donc retourner dans ce cas-ci le nombre 4 !
##
# phrase = "Bonjour tout le monde"
# lettre_a_chercher = "o"
# compteur = 0
# for lettre in phrase:
#     if lettre == lettre_a_chercher:
#         compteur += 1
# print(compteur)

# # Here is a more pythonic solution
# lettre_a_chercher = "o"
# phrase = "Bonjour tout le monde"
# print(phrase.lower().count(lettre_a_chercher))

"""
    SOLUTION

    lettre_a_chercher = "o"
    phrase = "Bonjour tout le monde"
    print(phrase.lower().count(lettre_a_chercher))

    EXPLICATION

Pour compter le nombre d'occurrences d'une lettre dans une chaîne de caractère, on utilise la fonction count.

Afin d'éviter toute confusion quant aux majuscules et minuscules, nous prenons le soin de convertir auparavant notre chaîne de caractère en minuscule avec la fonction lower.

    POINTS IMPORTANTS À RETENIR

    Pour compter le nombre d'occurrences d'une lettre dans une chaîne de caractère, on utilise la fonction count.
    Pour convertir une chaîne de caractère en minuscule, on utilise la fonction lower.
"""

print("\nExercice 16")
# Exercice 16
# Notions abordees: les listes.
# On retourne aux bases de Python dans cet exercice dans lequel vous devez tout simplement recuperer le premier element de la liste.
# Dans cet exemple, vous devez printer la chiane de caractere 'Pierre'
# ma_liste = ["Pierre", "Paul", "Marie"]
##
# ma_liste = ["Pierre", "Paul", "Marie"]
# print(ma_liste[0])
"""
    SOLUTION

    ma_liste = ["Pierre", "Paul", "Marie"]
    print(ma_liste[0])

    EXPLICATION

Exercice très simple pour les gens habitués à utiliser Python.

Pour récupérer un élément dans une liste basé sur sa position dans la liste, on utilise les crochets : []

Il suffit ensuite d'indiquer à l'intérieur des crochets l'indice de l'élément qu'on veut récupérer.

Ici, pour récupérer le premier élément de la liste, on utilise donc la syntaxe suivante :

ma_liste[0] 

Le seul point sur lequel il fallait être attentif est le fait qu'en programmation on commence toujours à compter à partir de 0.

Ainsi, pour récupérer le premier élément de la liste, on utilise l'indice 0 et non 1.

    POINTS IMPORTANTS À RETENIR

    Pour récupérer le premier élément de la liste, on utilise les crochets et l'indice 0.
"""

print("\nExercice 17")
# Exercice 17
# Notions abordees: les listes.
# On monte d'un cran dans cet exercice, dans lequel vous devez recuperer plusieurs elements de la liste.
# Pour reussir cet exercice, vous devez printer le premier element ('Pierre'), le dernier element('Marie'), les deux premieres elements ('[Pierre','Paul]')
# et les deux derniers elements (['Paul','Marie])
##
# ma_liste = ["Pierre", "Paul", "Marie"]
# print(ma_liste[0])
# print(ma_liste[-1])
# print(ma_liste[0:2])
# print(ma_liste[1:])

"""
    SOLUTION

    ma_liste = ["Pierre", "Paul", "Marie"]
     
    print(ma_liste[0])
    print(ma_liste[-1])
    print(ma_liste[:2])
    print(ma_liste[-2:])

    EXPLICATION

Pour récupérer le premier élément, nous l'avons-vu précédemment, on utilise les crochets et l'indice 0.

Pour récupérer le dernier élément, peu importe la taille de la liste, on utilise l'indice -1 !

Pour récupérer les deux premiers éléments de la liste, on utilise une syntaxe un peu spéciale, qui se nomme 'slicing'.

En effet, plutôt que de spécifier un seul indice entre les crochets, on peut spécifier un indice de départ et un indice de fin.

Ainsi, pour récupérer les deux premiers éléments, on peut utiliser la syntaxe suivante :

ma_liste[0:2] 

Et puisque nous commençons depuis le début de la liste, on n'a même pas besoin d'indiquer le 0 et Python comprendra qu'on veut commencer depuis le début de la liste, jusqu'au deuxième élément inclus :

ma_liste[:2] 

Pour récupérer les deux derniers éléments, peu importe la taille de la liste, on utilise là encore un indice négatif et toujours le même principe de 'slicing' :

ma_liste[-2:] 

Encore une fois, pas besoin d'indiquer un indice après les deux points, on peut tout simplement laisser le deuxième indice vide, et le slice ira jusqu'à la fin de la liste.

    POINTS IMPORTANTS À RETENIR

    Pour récupérer plusieurs éléments à l'intérieur d'une liste, on utilise le slicing : ma_liste[début:fin]
    Pour récupérer des éléments en partant de la fin, on peut utiliser des indices négatifs.
"""

print("\nExercice 18")
# # Exercice 18
# # Notions abordees: les listes.
# # On continue avec les listes. Cetter fois-ci, l'objectif de l'exercice est de recuperer un element sur deux dans la liste.
# # Votre scritp doit donc printer la liste suivante: [1, 3, 5, 7, 9]
# #
# ma_liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(ma_liste[0:11:2])
"""
    SOLUTION

    ma_liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(ma_liste[::2])

    EXPLICATION

Encore une fois, nous utilisons ici le 'slicing' pour récupérer uniquement un élément sur deux dans notre liste.

Nous pouvons indiquer en effet un troisième nombre entre les crochets et ce nombre indique le pas avec lequel nous voulons récupérer les éléments de notre liste.

Là encore, pas besoin d'indiquer d'indice spécifique pour les deux premiers nombres : en n'indiquant aucun indice, le slicing commencera automatiquement au début de la liste, ira jusqu'à la fin, en prenant seulement un élément sur deux :

    ma_liste[::2]

La syntaxe complète du slicing est donc la suivante :

ma_liste[indice_de_depart:indice_de_fin:pas] 

Si on veut récupérer les éléments de 4 à 25 avec un pas de 3 on fera donc :

    >>> ma_liste = range(100)
    >>> ma_liste[4:26:3]
    [4, 7, 10, 13, 16, 19, 22, 25]

    POINTS IMPORTANTS À RETENIR

    Pour récupérer un élément sur deux, on utilise le slicing et on indique un pas de 2 à l'intérieur des crochets.
"""

print("\nExercice 19")
# Exercice 19
# Notions abordeeL les listes.
# Un autre petit exercice assez simple avec les listes, qui utilise une fonction qui n'est pas forcement connue de tous.
# Le but de cette exercice est d'ajouter plusieurs elements dans une liste en une seule fois !
# Mais attention, vous devez ajouter plusieurs elements dans la liste original, et non pas imbriquer une liste dans une autre.
# La liste de depart contient les elements 1, 2 et 3.
# La liste finale doit contenir les elements 1, 2, 3, 4, 5 et 6. Vous devez donc ajouter les elements 4, 5 et 6 à la liste originale.
# #
# ma_liste = [1, 2, 3]
# ma_liste = [1, 2, 3] + [4, 5, 6]
# print(ma_liste)
# # In a more pythonic way
# ma_liste = [1, 2, 3]
# ma_liste.extend([4, 5, 6])
# print(ma_liste)
"""
    SOLUTION

    ma_liste = [1, 2, 3]
    ma_liste.extend([4, 5, 6])
    print(ma_liste)

    EXPLICATION

Pour ajouter plusieurs éléments dans une liste en une seule fois, on utilise la fonction extend.

En effet, si vous utilisez la fonction append, vous allez ajouter une liste à l'intérieur de votre liste.

Pour ajouter plusieurs éléments d'un coup sans créer une sous-liste, il faut donc utiliser la fonction extend, qui va ajouter à la fin de votre liste les différents éléments que vous lui passez.

Il peut y avoir de la confusion dans le fait que vous devez passer une liste à la fonction extend.

Ainsi vous ne pouvez pas faire :

ma_liste.extend(4, 5, 6) 

Il faut à la place faire :

ma_liste.extend([4, 5, 6]) 

Bien que l'on passe une liste en argument de la fonction extend, cette fonction va bien ajouter les éléments à l'intérieur de votre liste sans créer de sous-liste.

    POINTS IMPORTANTS À RETENIR

    Pour ajouter plusieurs éléments dans une liste en une seule fois, on utilise la fonction extend.
"""

print("\nExercice 20")
# Exercice 20
# Dans cet exercice, vous allez devoir recuperer les elements communs aux deux listes.
# Dans ce cas-ci, votre liste commune devra contenir les nombres 5, 7, 10
# Vous pouvez utiliser les sets pour cet exercice
# Pour aller plus loin essayez de faire cet exercice sans utiliser les sets
# #
# liste_01 = [1, 5, 6, 7, 9, 10, 11]
# liste_02 = [2, 3, 5, 7, 8, 10, 12]
# print(list(set(liste_01).intersection(set(liste_02))))

# # le meme exercice avec deux boucles à la place du set()
# print("")
# liste_01 = [1, 5, 6, 7, 9, 10, 11]
# liste_02 = [2, 3, 5, 7, 8, 10, 12]
# ma_liste = []
# i, j = 0, 0
# for j in liste_01:
#     result = 0
#     for i in liste_02:
#         if (i == j):
#             ma_liste.append(i)
# print(ma_liste)

"""
    SOLUTION

    liste_01 = [1, 5, 6, 7, 9, 10, 11]
    liste_02 = [2, 3, 5, 7, 8, 10, 12]
     
    sliste_01 = set(liste_01)
    sliste_02 = set(liste_02)
     
    intersect = sliste_01.intersection(sliste_02)
    print(list(intersect))

    EXPLICATION

Dans cet exercice, nous passons par les sets pour récupérer les éléments communs à deux liste.

Pour convertir une liste en set, rien de plus facile, on utilise la fonction set :

sliste_01 = set(liste_01) 

Une fois que nos deux listes sont converties en set, nous pouvons utiliser des méthodes pour récupérer l'intersection, la différence et plein d'autres opérations du même style :

intersect = sliste_01.intersection(sliste_02) 

Il ne nous reste plus qu'à re-convertir notre set résultant en liste avec la fonction list :

resultat = list(intersect) 

    POINTS IMPORTANTS À RETENIR

    Pour convertir une liste en set, on utilise la fonction set.

    Pour récupérer les éléments communs à deux set, on utilise la méthode intersection.
"""

print("\nExercice 21")
# # Exercice 21
# # Dans cet article, l'objectif est de trier une liste qui contient des tuples:
# # liste = [("Harry Potter", 5), ("Wall-E", 3), ("Blade Runner", 4)]
# # Comme vous pouvez le voir, la liste contient des tuples qui ont comme premier element le nom d'un film, et comme deuxieme element
# # leur note sur 5.
# # Le but de l'exercice est de trier ces tuples en fonction de la note qui leur a ete attribuee.
# # Votre script doit donc retourner la liste suivante:
# # [('Wall-E, 3), ('Blade Runner', 4), ('Harry Potter', 5)]
# #
# liste = [("Harry Potter", 5), ("Wall-E", 3), ("Blade Runner", 4)]
# liste = sorted(liste, key=lambda colonnes: colonnes[1])
# print(liste)
"""
    SOLUTION

    liste = [("Harry Potter", 5), ("Wall-E", 3), ("Blade Runner", 4)]
    liste.sort(key=lambda x: x[1])
    print(liste)

    EXPLICATION

Pas besoin d'aller chercher très loin pour résoudre cet exercice. En effet, la fonction sort accepte un argument dénommé 'key', qui va vous permettre de trier la liste selon des critères spécifiques.

Dans ce cas-ci, nous donnons comme argument au paramètre key une fonction anonyme, qui elle même nous retourne l'élément 1 de la variable qui est passée à x.

L'élément 1 du tuple correspond à la note du film, la fonction sort va donc trier les éléments de notre liste en fonction de cette élément et donc trier notre liste en fonction de la note accordée à chaque film.
"""

print("\nExercice 22")
# # Exercice 22
# # Dans cet exercice, nous allons recuperer la valeur de la cle 'prenom', contenue dans le dictionnaire 'employe'.
# # Votre script doit donc retourner la chaine de caractere 'Pierre'.
# # Aller plus loin : contstruisez votre script de sorte à ce qu'il ne produise aucune erreur si les cles du dictionnaire
# # venaient à etre modifiees.
# employes = {"01": {"identite": {"prenom": "Pierre", "nom": "Dupont"}}}
# # si la clef n'est pas trouve le script plante, imaginons que l'on cherche la clef 1 au lieu de 01
# print(employes['01']["identite"]["prenom"])
# # on retourne rien si la clef n'est pas trouve
# print(employes.get("01", {}).get("identite", {}).get("prenom", "valeur inconnue"))

"""
    SOLUTION

    employes = {"01": {"identite": {"prenom": "Pierre", "nom": "Dupont"}}}
    print(employes.get("01", {}).get("identite", {}).get("prenom", "valeur inconnue"))

    EXPLICATION

Bien que cette ligne de code semble complexe, elle ne l'est pas tant que ça, car elle répète trois fois de suite le même principe.

Pour récupérer une valeur dans un dictionnaire, on peut tout d'abord utiliser les crochets de cette façon :

employes["01"] 

L'inconvénient de cette façon de faire c'est que notre script va retourner une erreur si la clé n'existe pas.

Afin de palier à ce problème nous utilisons à la place la méthode get, qui va par défaut nous retourner None si la clé n'existe pas.

Mais encore mieux, il est possible de spécifier un élément par défaut à retourner, autre que None, si la clé n'existe pas.

C'est ce principe que nous mettons en place ici. Nous récupérons la première clé et si celle-ci n'existe pas, nous retournons un dictionnaire vide :

employes.get("01", {}) 

Ainsi, nous pouvons chaîner plusieurs get à la suite, sans risquer de faire planter le script. En effet, si nous ne retournions par de valeur par défaut et que la clé n'existe pas dans le dictionnaire, la 2e méthode 
get ne fonctionnerait pas car elle s'exécuterait sur None.

Donc si la première clé n'est pas trouvée, le get va agir sur un dictionnaire vide et ainsi de suite, évitant tout risque d'erreur.

    POINTS IMPORTANTS À RETENIR

    Pour récupérer la valeur associée à une clé dans un dictionnaire, on peut utiliser la fonction get, qui permet de spécifier une valeur par défaut à retourner si la clé n'est pas trouvée.
"""

print("\n Exercice 23")
# Exerice 23
# Notions abordees: les dictionnaires.
# On continue avec les dictionnaires ! Dans cet exercice, vous devez aaditionner toutes les valeurs
# du dictionnaire ensemble. Votre script doit donc retourner le nombre 8700.
# Allez plus loin: Esseayer de faire tenir votre scipt en une seule ligne
# #
# employes = {"Pierre": 2500, "Marie": 5000, "Julien": 1200}
# values = 0
# for value in employes.values():
#     result += value
# print(result)

# print("Exercice 23 bis")
# # autre solution:
# employes = {"Pierre": 2500, "Marie": 5000, "Julien": 1200}
# print(sum(employes.values()))
"""
    SOLUTION

    employes = {"Pierre": 2500, "Marie": 5000, "Julien": 1200}
    print(sum(employes.values()))

    EXPLICATION

Encore une fois un exercice assez simple pour qui connait bien Python.

Pour récupérer toutes les valeurs d'un dictionnaire, on peut utiliser la méthode values :

    >>> employes.values()
    dict_values([2500, 5000, 1200])

Et pour obtenir la somme de toutes ces valeurs, rien de plus simple que d'utiliser la fonction sum :

    >>> sum(employes.values())
    8700

    POINTS IMPORTANTS À RETENIR

    Pour récupérer toutes les valeurs d'un dictionnaire, on utilise la méthode values.
    Pour faire la somme de plusieurs nombres, on utilise la fonction sum.
"""

print("\n Exercice 24")
# # Notions abordees: Les modules.
# # Nous passons maintenant avec un exercice simple sur les modules.
# # Le script actuel ne fonctionne pas et vous retournera une erreur. A vous de trouver où se situe l'erreur afin que le script fonctionne.
# # Votre script doit au final retourner un nombre aleatoire compris entre 0 et 5.
# #
# nombre_aleatoire = random.randint(0, 5)
# print(nombre_aleatoire)
"""
    SOLUTION

    import random
     
    nombre_aleatoire = random.randint(0, 5)
    print(nombre_aleatoire)

    EXPLICATION

Pour utiliser une fonction contenue à l'intérieur d'un module, il est impératif de préfixer cette fonction par le nom du module.

Dans cet exercice, on import le module comme suit :

import random

Pour utiliser la fonction randint, il faut donc faire :

random.randint(0, 5)

Si nous voulons utiliser directement la fonction randint, il est possible de le faire avec une syntaxe d'import légèrement différente :

from random import randint   

De cette façon, on importe directement la fonction randint et non pas tout le module random. La fonction randint est donc directement accessible dans l'espace global de notre script :

randint(0, 5) 

    POINTS IMPORTANTS À RETENIR

    Pour utiliser une fonction à l'intérieur d'un module, il ne faut pas oublier de préfixer la fonction par le nom du module.
    Pour importer une fonction à l'intérieur d'un module directement dans l'espace global de notre script, on peut utiliser la syntaxe from module import fonction .
"""

print("\n Exercice 25")
# # Notions abordees: syntaxe.
# # On continue avec les erreurs et la syntaxe. Le script suivant ne fonctionne pas, à vous de trouver pourquoi et le corriger.
# # Votre script doit retourner la liste [2, 6, 12, 20, 42, 56, 90]
# liste = [1, 1, 4, 3, 3, 2, 6, 7, 7, 9, 2]

# resultat = [i*(i+1 % (i*5)) for i in sorted(list(set(liste)))]
# print(resultat)

"""
    SOLUTION

    liste = [1, 1, 4, 3, 3, 2, 6, 7, 7, 9, 2]
    resultat = [i*(i+1%(i*5)) for i in sorted(list(set(liste)))]
    print(resultat)

    EXPLICATION

Il est courant de faire ce genre d'erreurs dans des scripts qui contiennent beaucoup de parenthèses et crochets.

Une bonne façon de vérifier si vous n'avez pas oublié une parenthèse ou un crochet est de compter dans un sens le nombre de parenthèse / crochet ouvrant, et ensuite de compter dans l'autre sens si vous avez bien le 
même nombre de parenthèse / crochet fermant.

POINTS IMPORTANTS À RETENIR

    Une seule chose : attention à la syntaxe !
"""

print("\n Exercice 26")
# # Notions abordees: Les modules, les variables.
# # Dans cette exercice, nous allons importer une variable d'un autre module dans notre script principal.
# # Dans le fichier constants.py se trouve une variable 'nom' qui contient le mot 'Udemy'.
# # Le but de l'exercice est d'importer cette variable dans le fichier exercice.py pour l'afficher grace à la fonction print.
# #
# print(constants.nom)

"""
    SOLUTION

    import constants
    print(constants.nom)

    EXPLICATION

Rien de plus simple dans cet exercice ! Il suffisait d'importer le module constants et de faire un print de la variable 'nom' contenue à l'intérieur de ce module. Un exercice simple, mais qui nécessite de bien comprendre le fonctionnement des modules et les possibilités qu'ils offrent.

    POINTS IMPORTANTS À RETENIR

    Pour importer une variable d'un module, il suffit d'importer le module dans lequel la variable est contenue.
"""

print("\n Exercice 27")
# # Afficher le chemin du script python en cours
# #
# fichier_courant = __file__
# dossier_parent = os.path.dirname(fichier_courant)
# dossier_image = os.path.join(dossier_parent, "images")
# print(dossier_image)

print("\n Exercice 28")
# # Notions abordees: le module OS.
# # Le but de cet exercice est de recuperer l'extension d'un fichier à l'aide du module OS.
# # Dans cas-ci, vous devez recuperer l'extension du fichier python.exe
# # Votre script doit retourner l'extension sans le point. Vous devez donc recuperer 'exe'.
# #
# fichier = "C:/Python36/python.exe"

# _, ext = os.path.splitext('C:/Python36/python.exe')
# print(ext)

"""
    SOLUTION

    import os
     
    fichier = "C:/Python36/python.exe"
     
    extension = os.path.splitext(fichier)[1]
    extension = extension.strip(".")
     
    print(extension)

    EXPLICATION 

Dans cet exercice, nous utilisons le module os, qui contient déjà des fonctions qui nous permettent de gérer ce genre de situations.

Depuis le module os, nous pouvons importer le module path, qui donne accès à tout un tas de fonctions permettant de manipuler des chemins.

La fonction splitext nous permet de séparer un chemin de son extension. Cette fonction nous retourne donc un tuple, qui contient le chemin sans l'extension en premier élément, et l'extension seule en deuxième 
élément :

    >>> import os
    >>> fichier = "C:/Python36/python.exe"
    >>> extension = os.path.splitext(fichier)[1]
    '.exe'

Pour récupérer l'extension sans le point, il ne nous reste qu'à utiliser la fonction strip :

    extension = extension.strip(".")

    POINTS IMPORTANTS À RETENIR 

    Pour manipuler des chemins de dossier, on utilise le module os.path.

    Pour séparer un chemin de son extension, on utilise la fonction os.path.splitext.
"""

print("\n Exercice29")
# # Exercice 29
# # Acceder à une variable d'environnement PATH et HOME
# #
# print(os.environ.get('PATH'))
# print("")
# print(os.environ.get)  # retourne toutes les variables d'environnement

"""
    SOLUTION

    import os
     
    home_var = os.environ.get("HOME")
    print(home_var)
"""

print("\n Exercice30")
# # Exercice 30
# # Calculer le temps d'execution d'un script
# #
# start_time = time.time()
# _ = [i*2 for i in range(9999999)]
# print("Temps d'execution: %s secondes ---" % (time.time()-start_time))
"""
    SOLUTION

    from time import time
     
    a = time()
    _ = [i*2 for i in range(9999999)]
    print(f"Temps d'exécution: {time() - a}s")
"""

print("\n Exercice31")
# # Exercice 31
# # Notions abordees: les structures conditionnelles, les nombres.
# #
# a = 0
# if a is not None:
#     print("la valeur de a est %i:" % a)
"""
    SOLUTION

    a = 0
    if a is not None:
        print(a)

    EXPLICATION

Exercice qui s'attaque à une erreur assez sournoise et courante.

Dans ce cas-ci, on veut vérifier que la variable a contient bien un nombre.

Pour rapidement vérifier qu'une variable contient des données, on peut utiliser une structure conditionnelle de base.

Par exemple pour vérifier qu'une liste n'est pas vide, on peut faire :

    ma_liste = [1, 2, 3]
    if ma_liste:
        print("La liste n'est pas vide")

Au lieu de :

    ma_liste = [1, 2, 3]
    if len(ma_liste) > 0:
        print("La liste n'est pas vide")

Vous conviendrez que la première façon de faire est plus concise est lisible. Cependant, en prenant l'habitude de cette syntaxe, on peut tomber dans l'écueil qu'il fallait résoudre dans cet exercice.

En effet, imaginons qu'à la place d'une liste, nous récupérons cette fois-ci un nombre entier. Si le nombre récupéré est 0, alors la structure conditionnelle ne sera pas vérifiée, car 0 est équivalant à False.

C'est pourquoi dans ce cas-ci, nous ne pouvons pas utiliser la syntaxe simplifiée if variable, il faut donc vérifier explicitement que la variable n'est pas égale à None :

    a = 0
    if a is not None:
        print("La variable n'est pas égale à None")

    POINTS IMPORTANTS À RETENIR

    Le nombre 0 est équivalant au boolean False.

    Pour vérifier explicitement qu'une variable n'est pas égale à None, il vaut mieux utiliser la syntaxe if variable is not None.
"""

# print("\n Exercice32")


# # Exercice 32
# # Notions abordees: Les chaines de caracteres.
# # Le but de cet exercice est d'afficher dans le print le nom et le prenom contenu dans les variables respectives.
# # Vous devez pour ceci utiliser la fonction format afin.
# # Votre script doit donc afficher au final: "Bonjour je m'appelle Pierre Dupont"
# # https://vbaforexcel.wordpress.com/2015/05/19/affichage-fonction-print/
# #
# prenom = "Pierre"
# nom = "Dupont"
# print("Bonjour je m'appelle Mr " + nom + " " + prenom)
# print("Bonjour je m'appelle Mr {0} {1}" .format(nom, prenom))
# print("Bonjour je m'appelle Mr %s, %s" % (nom, prenom))

"""
    SOLUTION

    prenom = "Pierre"
    nom = "Dupont"
    print("Bonjour je m'appelle {prenom} {nom}".format(prenom=prenom, nom=nom))

    EXPLICATION

Il est possible de réussir cet exercice sans utiliser la fonction format, en concaténant des chaînes de caractère avec le symbole +.

Cependant, vous remarquerez que la méthode format est souvent plus facile à utiliser et procure un résultat plus facile à décoder.

La méthode format s'applique directement sur une chaîne de caractère et fonctionne avec les accolades. On peut indiquer des indices à l'intérieur des accolades :

    "Bonjour je m'appelle {0} {1}".format(prenom, nom)

Mais aussi utiliser directement, comme dans le cas de cet exercice, des 'tags' qui vont nous permettre de remplir les espaces occupés par les accolades avec des variables :

    "Bonjour je m'appelle {prenom} {nom}".format(prenom="Pierre", nom="Dupont")

    POINTS IMPORTANTS À RETENIR

    Pour concaténer des chaînes de caractère, on peut utiliser directement la fonction format avec les accolades pour insérer des variables à l'intérieur d'une chaîne de caractère.
"""

print("\n Exercice33")
# # Exercice 33
# # Notions abordees: Les chaines de caractere.
# # Dans cet exercice, vous allez devoir inverser l'ordre des lettres d'un mot.
# # Dans cet exemple-ci, le mot est 'Udemy' votre script doit donc retourner la chaine de caractere 'Ymedu'
# # Pour valider l'exercice, il faut que la premiere lettre de votre chaine de caractere resultat soit
# # en majuscule("Ymedu" et non 'ymedU')
# # Aller plus loin: Faites tenir votre script en une seule ligne
# #
# mot = "Udemy"
# print(mot[::-1].capitalize())

# # autre possibilite:
# mot = "Udemy"
# resultat = []
# for lettre in reversed(mot):
#     resultat.append(lettre)
# resultat_formate = "".join(resultat)
# print(resultat_formate.capitalize())
"""
    SOLUTION

    mot = "Udemy"
     
    resultat = []
     
    for lettre in reversed(mot):
        resultat.append(lettre)
     
    resultat_formate = "".join(resultat)
    print(resultat_formate.capitalize())

    EXPLICATION

Tout d'abord, commençons par dire qu'il est possible de réaliser cet exercice en une seule ligne, avec les slices :

    >>> mot = "Udemy"
    >>> print("Udemy"[::-1].capitalize())
    "Ymedu"

Mais pour faire durer un peu le plaisir, je vous montre une façon de faire un peu moins directe et qui vous permettra d'utiliser un peu plus de fonctions natives de Python.

Tout d'abord, pour inverser l'ordre des lettres, nous utilisons la fonction reversed :

    >>> mot = "Udemy"
    >>> print(reversed(mot))
    <reversed object at 0x10386b278>

Cette fonction nous retourne un object 'reversed', qui est en fait un itérateur. Nous pouvons donc passer à travers cet itérateur avec une boucle for et ajouter chaque lettre dans une liste :

    for lettre in reversed(mot):
        resultat.append(lettre)

Nous nous retrouvons ainsi avec une liste contenant chaque lettre dans l'ordre inverse.

Pour terminer, nous pouvons utiliser la fonction join pour joindre les éléments de la liste ensemble et la fonction capitalize pour mettre une majuscule au début du mot :

    resultat_formate = "".join(resultat)
    print(resultat_formate.capitalize())

    POINTS IMPORTANTS À RETENIR

    Pour inverser une chaîne de caractère, on peut utiliser le slicing [::-1] ou la fonction reversed.
    Pour joindre les éléments d'une liste ensemble, on utilise la fonction join.
    Pour mettre une majuscule sur la première lettre d'un mot, on utilise la fonction capitalize.
"""

print("\n Exercice34")
# # Exercice 34
# # Notions abordees: le module random.
# # Dans cet exercice, nous allons melanger les lettres d'un mot grace au module random.
# # Le mot resultant devra commencer par une majuscule. Dans cet exercice nous allons melanger le mot 'Bonjour'.
# # Votre script devra melanger les lettres de ce mot pour donner par exemple: 'Ojoubr'.
# #
# a = list("bonjour")
# random.shuffle(a)
# print(("".join(a)).capitalize())

"""
    SOLUTION

    import random
     
    mot = "Bonjour"
    mot = list(mot)
     
    random.shuffle(mot)
     
    mot_random = "".join(mot).capitalize()
    print(mot_random)

    EXPLICATION

Pour facilement mélanger les lettres d'un mot, nous allons utiliser le module random et la fonction shuffle.

La fonction shuffle fonctionne sur des listes et permet de mélanger les éléments de la liste qui lui est passée.

Nous allons donc commencer par convertir notre mot en liste avec la fonction list :

    mot = list(mot)

Nous utilisons ensuite la fonction shuffle du module random pour mélanger la liste :

    random.shuffle(mot)

Il ne reste plus qu'à rassembler tous les éléments de la liste avec la fonction join et de remettre la majuscule à la bonne place avec la fonction capitalize :

    mot_random = "".join(mot).capitalize()

    POINTS IMPORTANTS À RETENIR

    Pour mélanger les éléments d'une liste, on utilise la fonction shuffle du module random.
    Pour convertir une chaîne de caractères en liste, on utilise la fonction list.
"""

print("\n Exercice35")
# # Exercice 35
# # Notions abordees: la fonction format.
# # Dans cet exercice, nous voulons tronquer le nombre de decimales contenues apres la virgule dans la variable 'nombre', par le nombre
# # contenu dans la variable 'decimales'.
# # votre script doit donc afficher: 'Nombre tronque:2938.489'
# #
# nombre = 2938.48872
# decimale = 3
# print("Nombre tronqué: {nombres:.{decimales}f}".format(
#     nombres=nombre, decimales=decimale))

# print("test de la valeur toto: {toto}".format(toto=decimale))
"""
    SOLUTION

    nombre = 2938.48872
    decimales = 3
     
    print("Nombre tronqué: {nombre:.{decimales}f}".format(nombre=nombre, decimales=decimales))

    EXPLICATION

Dans cet exercice, nous continuons d'explorer cette fabuleuse fonction format qui cache de nombreuses fonctionnalités assez avancées.

En effet, il est possible d'utiliser la syntaxe suivante pour tronquer le nombre de décimales après la virgule d'un nombre :

{nombre:.3f} 

'nombre' correspond au nom du tag que l'on utilise comme nom de paramètre dans la fonction format.

Nous avons ensuite deux points, un point, un nombre qui détermine le nombre de décimales après la virgule que l'on souhaite conserver (ici 3) et pour finir la lettre f.

Je l'avoue, ce n'est pas la syntaxe la plus facile à retenir, mais c'est vraiment très efficace pour pouvoir rapidement afficher un nombre tronqué dans une chaîne de caractère.

    SOLUTION ALTERNATIVE

Vous pouvez également utiliser la fonction round afin de tronquer le nombre de décimales :

    nombre = 2938.48872
    decimales = 3
     
    solution = round(nombre, decimales)
     
    print("Nombre tronqué: {}".format(solution))

Il vous faudra cependant tout de même utiliser la méthode format afin d'insérer le nombre tronqué à l'intérieur de la chaîne de caractères.

    POINTS IMPORTANTS À RETENIR

    On peut tronquer directement un nombre pour n'afficher qu'une certaine parties des décimales après la virgule grâce à la fonction format et la syntaxe {nombre:.3f}.
"""

print("\n Exercice36")
# # Exercice 36
# # Notions abordees: structures conditionnelles.
# #
# a = 20
# print("Vous etes majeur !") if a >= 18 else print("Vous etes minieur")
"""
    SOLUTION

    a = 20
    majeur = print("Vous êtes majeur !") if a >= 18 else print("Vous êtes mineur")

    EXPLICATION

Pour résoudre cet exercice, il fallait utiliser ce qu'on appelle un opérateur ternaire.

De cette façon, nous pouvons réaliser une condition if, else sur une seule ligne.

Il est important de noter qu'il n'est possible d'inclure des print dans un opérateur ternaire que depuis la version 3 de Python.

À noter aussi, il n'est pas possible d'inclure un elif dans un opérateur ternaire.
Nous n'avons donc que deux choix possibles avec le if et le else, en suivant la syntaxe suivante :

variable = expression if condition else expression 

    POINTS IMPORTANTS À RETENIR

    Pour réaliser une structure conditionnelle sur une seule ligne, on utilise un opérateur ternaire.
"""

print("\n Exercice37")
# # Exercice 37
# # Age du chien
# #
# age = int(input("Entrer l'age du chien: "))
# result = 0
# if (age < 0):
#     print("Vous devez entrer un age positif!")
# elif (age <= 2):
#     result = age * 10.5
#     print("l'age du chien est {0} ans a l'echelle humaine".format(result))
# else:
#     result = 21 + (age - 2) * 4
#     print("l'age du chien est %d ans a l'echelle humaine" % result)

"""
    age = int(input("Entrez l'âge du chien: "))
     
    if age < 0:
        print("Vous devez entrer un âge positif!")
        exit()
    elif age <= 2:
        d_age = age * 10.5
    else:
        d_age = 21 + (age - 2) * 4
     
    print("L'âge du chien en âge humain est", d_age)
"""

print("\n Exercice38")
# # Exercice 38
# # Notions abordees: Fonctions de base.
# # Dans cet exercice, nous allons trier trois nombres sans avoir recours à l'utilisation de structures conditionnelles
# # ni à la fonction sort(). A l'aide des fonctions de base de Python, vous allez devoir trouver un moyen de trier les
# # variables 'a', 'b', 'c' du plus petit au plus grand.
# # Dans le cas de cet exercice, avec a = 4, b = 6 et c = 2, votre script doit printer:'les nombres dans l'ordre sont 2, 4 et 6'.
# #
# a = 4
# b = 6
# c = 2
# a1 = min(a, b, c)
# a3 = max(a, b, c)
# a2 = (a + b + c) - a1 - a3
# print("Les nombres dans l'ordre sont {}, {} et {}".format(a1, a2, a3))
"""
    SOLUTION

    a = 4
    b = 6
    c = 2
     
    a1 = min(a, b, c)
    a3 = max(a, b, c)
    a2 = (a + b + c) - a1 - a3
     
    print("Les nombres dans l'ordre sont {}, {} et {}".format(a1, a2, a3))

    EXPLICATION

Dans cet exercice, il fallait penser un peu plus à la solution car il était interdit d'utiliser les structures conditionnelles.

Pour résoudre ce problème, nous commençons par trouver le nombre le plus petit et le nombre le plus grand entre les trois variables a, b et c grâce aux fonctions min et max.

Cela nous donne donc la variable a1 et la variable a3 :

    a1 = min(a, b, c)
    a3 = max(a, b, c)

Puisque nous ne pouvons pas savoir d'avance quelles variables parmi a, b et c vont correspondre à la valeur la plus petite et la valeur la plus grande, il nous faut faire un peu d'arithmétique pour trouver la valeur du milieu.

Pour se faire, nous additionnons les trois valeurs ensemble (a, b et c) puis nous soustrayons les deux variables précédemment trouvées avec la fonction min et max :

    a2 = (a + b + c) - a1 - a3

    POINTS IMPORTANTS À RETENIR

    Pour trouver la valeur maximale ou minimale entre plusieurs variables, on utilise les fonctions min et max.
"""

print("\n Exercice39")
# # Dans cet exercice, nous sommes en presence d'une boucle while infinie! En l'etat actuel, le script ne s'arretera jamais et la phrase 'Exercice reussi!'
# # ne s'affichera jamais.
# # Vous devez modifier la boucle while afin de sortir et d'afficher la phrase 'Exercice reussi !'
# i = 0
# while i < 10:
#     i+=1
# print("Exercice reussi!")
"""
    SOLUTION

    i = 0
     
    while i < 10:
        pass
        i += 1
     
    print("Exercice réussi !")

    EXPLICATION

Une erreur courante que font beaucoup de débutants est de créer une boucle infinie.

La boucle while, bien que très pratique, est également assez dangereuse à manipuler pour qui ne fait pas attention à la condition de sortie.

C'était le cas dans cet exercice, dans lequel la variable i n'était jamais incrémentée et donc toujours plus petite que 10.

Il fallait donc incrémenter la valeur de i pour pouvoir arriver à un moment dans le script où i soit plus grand que 10 et que la condition du while soit fausse.

Peu importe la boucle while que vous comptez faire, je vous conseille toujours de vous prévoir une porte de sortie de ce genre : incrémentez une variable à chaque itération de la boucle et sortez de la boucle une fois que la variable atteint un nombre trop élevé, afin d'éviter de faire planter votre script si votre condition initiale n'est jamais fausse.

    POINTS IMPORTANTS À RETENIR

    Pour incrémenter un nombre entier, on utilise la syntaxe variable += 1.
"""

print("\n Exercice40")
# # Exercice 40
# # On continue avec les boucles, cette fois-ci la boucle for.
# # Le but de cet exercice est de printer l'index de chaque lettre du mot 'Python'.
# # Votre script doit donc retourner:
# # 0
# # 1
# # 2
# # 3
# # 4
# # 5
# #
# mot = "Python"
# for i in range(len(mot)):
#     print(i)

"""
    SOLUTION

    mot = "Python"
    for i in range(len(mot)):
        print(i)

    EXPLICATION

La fonction range a besoin d'un nombre pour créer une liste de nombres de la longueur du nombre passé en argument.

Ici dans le script, nous passions directement la variable mot - qui est une chaîne de caractère - à la fonction range, ce qui nous retournait logiquement une erreur.

À la place, il fallait utiliser la fonction len pour calculer la longueur de la chaîne de caractère et ainsi passer ce nombre à la fonction range pour pouvoir itérer sur la liste obtenue.


    POINTS IMPORTANTS À RETENIR

    Pour calculer la longueur d'une chaîne de caractère, on utilise la fonction len.
"""

print("\n Exercice41")
# # Exercice 41
# # Dans cet exercice, la fonction 'multiplicateur_mot' retourne une erreur.
# # Trouvez cette erreur et modifiez la fonction pour qu'elle ne retourne plus d'erreur. Il y a plusieurs facons de fixer cetter erreur.
# # Votre script doit afficher 5 fois le mot 'Bonjour' à la suite (parce que dans la vie, il est important de faire des scripts bien eleves...)
# #

# def multiplicateur_mot(mot, mult=5):
#     return mot * mult


# mot_multiplie = multiplicateur_mot(mot="Bonjour")
# print(mot_multiplie)

"""
    SOLUTION

    def multiplicateur_mot(mot, mult=5):
        return mot * mult
     
    mot_multiplie = multiplicateur_mot(mot="Bonjour")
    print(mot_multiplie)

    EXPLICATION

L'ordre des paramètres par défaut dans une fonction a son importance ! En effet, si vous définissez une valeur par défaut pour un paramètre qui se trouve en première position, vous avez l'obligation de définir une valeur par défaut pour tous les paramètres qui suivent.

La façon rapide de régler l'erreur qui se trouvait dans ce script était donc soit de définir une valeur par défaut pour les deux paramètres de la fonction, soit d'inverser l'ordre des paramètres, ce que nous avons fait dans la solution proposé ci-dessus.

    POINTS IMPORTANTS À RETENIR

    L'ordre des paramètres dans une fonction a son importance ! Vous ne pouvez pas mettre un paramètre sans valeur par défaut après un paramètre qui en a une.
"""

print("\n Exercice42")
# # Exercice 42
# # On continue avec les erreurs à trouver dans les fonctions !
# # Cette fois-ci, le script ne retourne pas d'erreur mais n'affiche pas le resultat escompte.
# # La fonction addition devrait nous permettre d'additionner deux nombres ensemble. Cependant, quand on print la variable 'resultat'.
# # Python nous retourne 'None', au lieu du resultat de l'addition(ici 15).
# # Modifiez la fonction pour le print de 'resultat affiche le resultat de l'addition
# # def addition(a, b):
# #   c = a + b
# #
# # resultat = addintion(5, 10)
# # print(resultat)
# #

# def addition(a, b):
#     c = a + b
#     return c


# resultat = addition(5, 10)
# print(resultat)

"""
    SOLUTION

    def addition(a, b):
        c = a + b
        return c
     
    resultat = addition(5, 10)
    print(resultat)

    EXPLICATION

Une fonction peut, dans certains cas, ne pas retourner de résultat (par exemple, une fonction qui exécute plusieurs print à la suite, pour afficher un message de bienvenue par exemple, n'a pas besoin de retourner 
de valeur spécifique).

Cependant, ici, la fonction sert à calculer la somme de deux valeurs. Il faut donc retourner d'une façon où d'une autre le résultat de cette addition.

Pour retourner une valeur dans une fonction, on utilise le mot clé return, comme ici :

    return c

Cela nous permet de récupérer la valeur de l'addition lors de l'appel de la fonction dans une variable :

    resultat = addition(5, 10)

    POINTS IMPORTANTS À RETENIR

    Pour retourner une valeur à l'intérieur d'une fonction, on utilise le mot clé return.
"""

print("\n Exercice43")
# # Exercice 43
# # Notions abordees: boucle for, fonction range.
# # On continue avec la boucle for, cette fois-ci pour afficher la table de multiplication d'un nombre.
# # Dans ce cas-ci, votre script doit afficher la table de multiplication du nombre 7.
# # 0 * 7 = 0
# # 1 * 7 = 7
# # 2 * 7 = 14
# # 3 * 7 = 21
# # 4 * 7 = 28
# # 5 * 7 = 35
# # 6 * 7 = 42
# # 7 * 7 = 49
# # 8 * 7 = 56
# # 9 * 7 = 63
# # 10 * 7 = 70
# # Attention aux espaces entre chaque nombre et symbole !
# #
# number = 7
# for i in range(11):
#     print("{i} x {number} = {result}".format(
#         i=i, number=number, result=i * 7))

"""
    SOLUTION

    nombre = 7
     
    for i in range(11):
        print("{i} x {nombre} = {resultat}".format(i=i, nombre=nombre, resultat=i*nombre))

    EXPLICATION

Ici, nous faisons tous les calculs nécessaires directement à l'intérieur de la méthode format.

Pour commencer, nous bouclons à travers une liste contenant les nombres de 0 à 10, grâce à la fonction range :

    for i in range(11):

Nous affichons ensuite dans la chaîne de caractère formattée, le nombre courant de la boucle, contenu dans la variable i, le nombre pour lequel nous affichons la table de multiplication, contenu dans la variable 
nombre, puis la multiplication de l'un par l'autre (i * nombre).

    POINTS IMPORTANTS À RETENIR

    Il est possible de faire des opérations mathématiques directement à l'intérieur de la méthode format, afin d'insérer le résultat de ces opérations à l'intérieur d'une chaîne de caractère.
"""

print("\n Exercice44")
# # Exercice 44
# # Notions abordees: boucle for
# # Les boucles for, encore et toujours, cette fois-ci, un exercice dans lequel nous allons recuperer à la fois l'indice et l'element
# # sur lequel nous bouclons dans chaque iteration de la boucle for.
# # votre script doit donc retourner dans ce cas-ci:
# # 0 Pierre
# # 1 Paul
# # 2 Marie
# # solution 1
# #
# liste = ["Pierre", "Paul", "Marie"]
# index = 0
# for name in liste:
#     print("{index} {name}".format(index=index, name=name))
#     index += 1

# # solution 2:
# liste = ["Pierre", "Paul", "Jacques"]
# for i in range(len(liste)):
#     print("%d %s" % (i, liste[i]))

# # Correction:
# liste = ["Pierre", "Paul", "Marie"]
# for i, nom in enumerate(liste):
#     print(i, nom)

"""
    SOLUTION

    liste = ["Pierre", "Paul", "Marie"]
    for i, nom in enumerate(liste):
        print(i, nom)

    EXPLICATION

Pour récupérer un élément dans une liste ainsi que son indice dans une boucle for, une erreur souvent faite par les débutants, est de passer par la fonction range et la fonction len, ce qui alourdit le code et le rend difficilement lisible :

    for i in range(len(liste)):
        print(i, liste[i]))

Pour récupérer dans une boucle for à la fois l'élément sur lequel on boucle ainsi que son indice, on préfère utiliser la fonction enumerate :

    for i, nom in enumerate(liste):
        print(i, nom)

    POINTS IMPORTANTS À RETENIR

    Pour récupérer un élément et son indice dans une boucle for, on utilise la fonction enumerate.
"""

print("\n Exercice45")
# # Exercice 45
# # Notions abordees: boucle for, structure conditionnelle.
# # Le but de cet exercice est de recuperer dans un seconde liste, la liste 'nombre_pairs', uniquelment les nombres
# # pairs de la premiere liste.
# # votre script doit donc printer la liste suivante:
# # [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48]
# #
# nombres = range(50)
# nombres_pairs = []
# for i in nombres:
#     if (i % 2) == 0:
#         nombres_pairs.append(i)

# print(nombres_pairs)

"""
    SOLUTION

    nombres = range(50)
    nombres_pairs = []
     
    for i in nombres:
        if i % 2 == 0:
            nombres_pairs.append(i)
     
    print(nombres_pairs)

    EXPLICATION

Pour résoudre cet exercice, il fallait faire appel à un opérateur mathématique quelque peu méconnu : l'opérateur modulo.

Cet opérateur est un peu l'alter égo de l'opérateur division, puisqu'il nous permet de récupérer le reste de la division d'un nombre par un autre.

Par exemple, 10 % 2 retournera 0, car 10 / 2 est égal à 5 et la division ne laisse aucun reste.

Par contre, 11 % 2 retournera 1, car 11 / 2 est égal à 5 et il reste 1.

Le modulo est donc un opérateur mathématique très utilisé pour vérifier si un nombre est pair ou non.
En effet, un nombre divisible par 2 et ne laissant aucun reste, est pair.

On utilise donc le modulo dans cet exercice pour tester chaque élément de la liste dans une boucle for en vérifiant si le modulo du nombre par 2 est égal ou non à 0 :

    for i in nombres:
        if i % 2 == 0:
            nombres_pairs.append(i)

    POINTS IMPORTANTS À RETENIR

    Pour vérifier si un nombre est pair, on utilise l'opérateur mathématique modulo, en vérifiant si le modulo de notre nombre par 2 est égal ou non à 0.
"""

print("\n Exercice46")
# # Exercice 46
# # Notions abordees: boucle for, structure conditionnelle, comprehension liste.
# # On continue avec le meme exercice qui consiste à recuperer seulement les nombres pairs d'une liste.
# # Cette fois-ci, nous allons effectuer le meme code que precedemment mais en une seule ligne, grace
# # aux comprehensions de liste.
# # Votre script, pour etre valide, doit donc tenir en 3 lignes: une ligne pour declarer la liste, une ligne
# # pour la trier, et une derniere ligne pour printer la liste.
# #
# nombres = range(50)
# nombre_pairs = [i for i in nombres if i % 2 == 0]
# print(nombre_pairs)

"""
    SOLUTION

    nombres = range(50)
    nombres_pairs = [i for i in nombres if i % 2 == 0]
    print(nombres_pairs)

    EXPLICATION

Dans cet exercice, nous récupérons les nombres pairs de la liste, toujours avec l'opérateur modulo, mais cette fois-ci en utilisant une compréhension de liste, ce qui permet de faire tenir le code en une seule ligne.

La syntaxe de la compréhension de liste est assez simple :

    [expression for expression in liste if condition]

La compréhension de liste nous permet donc d'exécuter une boucle for sur une seule ligne :

    [i for i in nombres]

La compréhension de liste retourne une nouvelle liste, que l'on peut stocker dans une variable :

    nouvelle_liste = [i for i in nombres]

Pour finaliser cet exercice, il ne reste plus qu'à ajouter la condition qui permet de vérifier si un nombre est pair ou non dans la compréhension de liste :

    nouvelle_liste = [i for i in nombres if i % 2 == 0]

    POINTS IMPORTANTS À RETENIR

    Pour exécuter une boucle for sur une seule ligne et ainsi trier les éléments d'une liste, on utilise une compréhension de liste.
"""


########################
# Niveau intermediaire #
########################
print("\n Exercice47")
# Exercice 47
# Notion abordees: boucle for.
# Le but de cet exercice est de calculer la somme de chaque chiffre d'un nombre.
# Dans ce cas-ci, votre script doit retourner le nombre 22(2 + 0 + 9 + 8 + 1 + 2)
# #
# nombre = 209812
# somme = 0
# for c in str(nombre):
#     somme += int(c)
# print(somme)

# # Aller plus loin : Essayez de faire tenir votre script en une seule ligne, grace aux comprehensions de liste.
# nombre = 209812
# print(sum([int(i) for i in str(nombre)]))

print("\n Exercice48")
# # Exercice 48
# # Notion abordees: comprehension liste.
# # On continue avec l'utilisation des comprehensions de liste, cette fois-ci pour remplacer une chaine de caractere dans les elements
# # d'une liste par une autre chaine de caractere.
# # Votre script doit donc afficher la liste suivante:
# # ['Pierre','Marie','Julien','Adrien','Julien']
# #
# liste = ["Pierre", "Marie", "Julie", "Adrien", "Julie"]
# nom_a_chercher = "Julie"
# nouveau_nom = "Julien"

# liste = [name.replace(nom_a_chercher, nouveau_nom) if (name == nom_a_chercher) else (name)
#          for name in liste]
# print(liste)

print("\n Exercice49")
# # Exercice 49
# # Le but de cet exercice est d'enlever les doublons de la liste.
# # Pour reussir l'exercice, vous devez utiliser une autre methode que celle qui consiste à convertir la liste en set pour enlever les
# # doublons.
# # Votre script doit donc afficher la liste suivante:
# # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# #
# nombres = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7, 8, 9, 10]
# resultat = []
# for i in nombres:
#     if i not in resultat:
#         resultat.append(i)
# print(resultat)

print("\n Exercice50")
# # Exercice 50
# # Printer un phrase autant de fois qu'un utilisateur le demande
# #
# res = 'o'
# compteur = 0
# while(res == 'o'):
#     print(f"Le compteur est maintenant à {compteur}")
#     compteur += 1
#     res = input("Voulez vous continuer ? o/n: ")

print("\n Exercice51")
# Notions abordees: les dictionnaires, boucle for.
# On s'attaque maintenant aux dictionnaires, toujours avec un peu de boucle for pour pimenter le tout.
# Dans cet exercice, vous devez boucler à travers la liste et ajouter au dictionnaire 'employes' seulement
# les elements de la liste qui sont des chaines de caractere.
# Le but de l'exercice est de trier les donnees et de construire un dictionnaire d'employes.
# Les cles du dictionnaires doivent etre 'id-xx', xx etant le numere de l'employe.
# Votre script devra donc retourner le dictionnaire suivant:
# {'id-01','Pierre','id-02','Marie','id-03','Adrien'}
#
employes = {}
liste = [10, 2329, 5, "Pierre", 203, "Marie", 867, "Adrien"]
num = 1
for element in liste:
    if (isinstance(element, str)):
        id = "id"+"-"+"0"+str(num)
        employes[id] = element
        num += 1
print(employes)

# autre solution:
employes = {}
liste = [10, 2329, 5, "Pierre", 203, "Marie", 867, "Adrien"]
i = 1
for element in liste:
    if not str(element).isdigit():
        employes["id-{:02d}".format(i)] = element
        i += 1

print(employes)

"""
    POINTS IMPORTANTS À RETENIR

    Pour vérifier si une chaîne de caractère ne contient que des nombres, on utilise la fonction isdigit.

    Pour formater un nombre pour qu'il contienne toujours 2 chiffres, on utilise la syntaxe 02d à l'intérieur d'accolades utilisées pour la fonction format.
"""

print("\n Exercice52")
# Notions abordees: les dictionnaires.
# On continue les dictionnaires: dans cet exercice, vous devez creer un dictionnaire qui contient toutes les lettres de l'alphabet.
# La cle de chaque element du dictionnaire doit contenir la position de la lettre dans l'alphabet, et la valeur doit etre egal à la
# lettre en question. L'indice de la premiere letrre doit etre 1 et non 0 !
# votre dicitionnaire doit donc etre comme ci-dessous:
# {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h'} etc...
# Aller plus loin: Essayer de faire tenir votre script en une seule ligne !
alphabet = {}
i = 1
for letter in string.ascii_lowercase:
    alphabet[i] = letter
    i += 1

print(alphabet)

# autre solution
print("\n autre solution: avec zip")
alphabet = string.ascii_lowercase
indices = range(1, len(alphabet) + 1)
liste_zip = zip(indices, alphabet)
resultat = dict(liste_zip)
print(resultat)

"""     
    POINTS IMPORTANTS À RETENIR

    Pour créer une liste de tuple à partir de deux listes, on utilise la fonction zip.

    Pour créer un dictionnaire à partir d'une liste de tuple, on peut utiliser la fonction dict.
"""

print("\n Exercice 53")
# Notons abordees: la boucle for, les fonctions.
# Un exercice toujours tres interessant à faire en Python est d'essayer de recreer les fonctions de base.
# Dans cet exercice, nous allons recreer la fonction len() qui permet de compter la longueur d'une variable.
# Dans cet exemple, nous voulons compter le nombre de lettres dans le mot 'bonjour'/
# votre script doit donc retourner le nombre 7.


def longueur(variable):
    compteur = 0
    for i in variable:
        compteur += 1
    return compteur


print(longueur("bonjour"))
"""
    POINTS IMPORTANTS À RETENIR

    Pour boucler à travers les différents éléments de plusieurs types de variables, on peut utiliser une boucle for.
    Pour incrémenter facilement un nombre entier, on peut utiliser la syntaxe +=
"""
