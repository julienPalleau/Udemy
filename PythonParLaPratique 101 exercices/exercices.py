from math import pi
import random
# Exercice 1
# Notion abordees : les variables
# On commence simple avec ce premier exercice, qui consiste à declarer differents types de variables.

# La variable 'prenom' qui doit contenir la chaine de caractere Pierre.
# La variable 'age' qui doit contenir 20.
# La variable 'majeur' qui doit contenir un boolean vrai.
# La variable 'compte_en_banque' qui doit contenir le nombre à virgule 20135,384.
# La variable 'amis' qui doit contenir une liste contenant trois chaines de caracteres: Marie, Julien, Adrien.
# La variable 'parents' qui doit contenir un tuple contenant deux chaines de caracteres: Marc et Caroline
prenom = "Pierre"
age = 20
majeur = True
compte_en_banque = 20135.384
amis = ["Marie", "Julien", "Adrien"]
parents = ("Marc", "Caroline")
print(prenom)
print(age)
print(majeur)
print(compte_en_banque)
print(amis)
print(parents)

# Exercice 2
# Notion abordees: les variables
# Une erreur s'est glissee dans la declaration de la variable 'site_web', à vous de la trouver et de la corriger pour que le script affiche
# le nom du site web.

#site_web = 'Udemy'
# print(site_web)

site_web = "Udemy"
print(site_web)

# Exercice 3
# Notions abordees: les variables
# Dans cet exercice, nous allons afficher un nombre à l'interieur d'une chaine de caractere.
# Pythom ne permet pas de concatener une chaine de caracteres avec un nombre, il va donc falloir convertir le nombre en chaine de
# caractere.
nombre = 15
print("Le nombre est " + str(nombre))

# Exercice 4
# Notions abordees: les variables
# Pour reussir l'exercice, vous devez printer la valeur que contient la variable 'a'.
a = 3
b = 6
a = b
b = 7
# trouver la valeur de a
print(6)

# Exercice 5
# Notions abordees: La fonction print.
# Dans cette exercice, nous allons utiliser les nouvelles fonctionnalites de python 3, afin de printer les 3 variables a, b et c, separees par un symbole d'addition(+)
a = 2
b = 6
c = 3
print(a, b, c, sep=" + ")

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

prenom = "Pierre"

if (isinstance(prenom, str)):
    print("La variable est une chaîne de caractères")
elif (isinstance(prenom, int)):
    pass

prenom = 0
if (isinstance(prenom, str)):
    print("La variable est une chaîne de caractères")
elif (isinstance(prenom, int)):
    pass

# Exercice 8
# Notions abordees: Les chaines de caractere.
# Dans cet exercice, vous devez remplacer le mot 'Bonjour' dans la variable 'phrase' par le mot 'Bonsoir' à l'aide d'une fonction Python.
# Vous devez donc modifier la variable 'phrase'!
# phrase = "Bonjour tout le monde."
# nouvelle_phrase =
# print(nouvelle_phrase)

phrase = "Bonjour tout le monde."
nouvelle_phrase = phrase.replace("Bonjour", "Bonsoir")
print(nouvelle_phrase)

# Exercice 9
# Notions abordees: Les chaines de caracteres.
# Le but de cet exercice est de remettre en ordre alphabetique les prenoms presents dans la chaine de caractere.
# Vous devez donc printer à la fin de l'exercice, la chaine de caractere suivante:
# "Anne, Julien, Lucien, Marie, Pierre"
# chaine = "Pierre, Julien, Anne, Marie, Lucien"
chaine = "Pierre, Julien, Anne, Marie, Lucien".split(", ")
chaine.sort()
chaine = ", ".join(chaine)
print(chaine)

# Exercice 10
# Notions abordees: Les operateurs mathematiques.
# Dans cet exercice, nous allons calculer le volume d'une sphere ayant pour rayon 10 centimetres.
# La formule pour calculer le volume d'une sphere est:
# (4pi/3)*rayon au cube
# rayon representant la valeur du rayon (defini dans le code par la variable 'rayon').
# Pour reussir l'exercice, vous devez uniquelment afficher le volume de la sphere, si vous rajoutez du texte en plus l'exercice ne sera pas
# valide (donc il suffit de laisser print(volume) à la fin et de calculer le volume à la ligne d'avant)
rayon = 10.0
volume = (4*pi)/3 * rayon**3
print(volume)

# Exercice 11
# Notions abordees: structures conditionnelles.
# Dans cet exercice, nous allons utiliser une structure conditionnelle pour verifier si a est plus grand ou non que 10.
# Dans ce cas-ci, a est egal à 12, votre script devra donc afficer 'a est plus grand que 10'
# Aller plus loin: Vous pouvez egalement rajouter une condition pour tester si la variable a contient bien un nombre.
# a = 12
a = 12
if a > 10:
    print("a est plus grand que 10")
elif a <= 10:
    print("a est inferieur ou egal a 10")


# Exerice 12
# Notions abordees: Les listes.
# Dans cet exercice, on contiue avec des operations assez simples utilisant les bases du langage Python.
# Le but ici est de crrer une liste de nombres allant de 5 à 15 en utilisant une fonction de base de Python.
# Pour valider l'exercice, vous devez afficher cette liste, en utilisant la fonction print.
list1 = []
for i in range(5, 16):
    list1.append(i)
print(list(list1))

# Exercice 13
# Notions abordees: les listes.
# Dans cet exercice, on continue avec la fonction range, cette fois-ci pour creer une liste de nombres pairs allant de 1 à 100.
# Votre script doit afficher la liste, pensez donc à faire un print à la fin, si vous faites juste declarer la liste,
# l'exercice ne sera pas valide
list1 = []
for i in range(2, 101, 2):
    list1.append(i)
print(list(list1))

# Exercice 14
# Notions abordees: Les modules, la boucle for.
# Le but de cet exercice est de generer 6 lancer de des aleatoires, allant de 1 à 6.
# Votre script devra donc par exemple retour les lancer suivants:
# 1
# 2
# 3
# 4
# 5
# 6
for i in range(1, 7):
    j = random.choice(range(1, 7))
    print(j)

print("")

# Exercice 15
# Notions abordees: Les chaines de caractere.
# Dans cet exercice, nous cherchons à compter le nombre d'occurrence d'une lettre dans une chaine de caractere.
# Ici, nous cherchons le nombre de fois que la lettre "o" apparait dans la phrase "Bonjour tout le monde".
# Votre script devra donc retourner dans ce cas-ci le nombre 4 !
phrase = "Bonjour tout le monde"
lettre_a_chercher = "o"
compteur = 0
for lettre in phrase:
    if lettre == lettre_a_chercher:
        compteur += 1
print(compteur)

# Here is a more pythonic solution
lettre_a_chercher = "o"
phrase = "Bonjour tout le monde"
print(phrase.lower().count(lettre_a_chercher))

# Exercice 16
# Notions abordees: les listes.
# On retourne aux bases de Python dans cet exercice dans lequel vous devez tout simplement recuperer le premier element de la liste.
# Dans cet exemple, vous devez printer la chiane de caractere 'Pierre'
# ma_liste = ["Pierre", "Paul", "Marie"]
ma_liste = ["Pierre", "Paul", "Marie"]
print(ma_liste[0])

# Exercice 17
# Notions abordees: les listes.
# On monte d'un cran dans cet exercice, dans lequel vous devez recuperer plusieurs elements de la liste.
# Pour reussir cet exercice, vous devez printer le premier element ('Pierre'), le dernier element('Marie'), les deux premieres elements ('[Pierre','Paul]')
# et les deux derniers elements (['Paul','Marie])
ma_liste = ["Pierre", "Paul", "Marie"]
print(ma_liste[0])
print(ma_liste[-1])
print(ma_liste[0:2])
print(ma_liste[1:])

# Exercice 18
# Notions abordees: les listes.
# On continue avec les listes. Cetter fois-ci, l'objectif de l'exercice est de recuperer un element sur deux dans la liste.
# Votre scritp doit donc printer la liste suivante: [1, 3, 5, 7, 9]
ma_liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(ma_liste[0:11:2])

# Exericie 19
# Notions abordeeL les listes.
# Un autre petit exercice assez simple avec les listes, qui utilise une fonction qui n'est pas forcement connue de tous.
# Le but de cette exercice est d'ajouter plusieurs elements dans une liste en une seule fois !
# Mais attention, vous devez ajouter plusieurs elements dans la liste original, et non pas imbriquer une liste dans une autre.
# La liste de depart contient les elements 1, 2 et 3.
# La liste finale doit contenir les elements 1, 2, 3, 4, 5 et 6. Vous devez donc ajouter les elements 4, 5 et 6 à la liste originale.
ma_liste = [1, 2, 3]
ma_liste = [1, 2, 3] + [4, 5, 6]
print(ma_liste)
# In a more pythonic way
ma_liste = [1, 2, 3]
ma_liste.extend([4, 5, 6])
print(ma_liste)
