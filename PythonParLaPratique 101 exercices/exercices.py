from math import pi
import time
import random
import constants
import os
import random

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

print("\nExercice 2")
# Exercice 2
# Notion abordees: les variables
# Une erreur s'est glissee dans la declaration de la variable 'site_web', à vous de la trouver et de la corriger pour que le script affiche
# le nom du site web.

# site_web = 'Udemy'
# print(site_web)

site_web = "Udemy"
print(site_web)

print("\nExercice 3")
# Exercice 3
# Notions abordees: les variables
# Dans cet exercice, nous allons afficher un nombre à l'interieur d'une chaine de caractere.
# Pythom ne permet pas de concatener une chaine de caracteres avec un nombre, il va donc falloir convertir le nombre en chaine de
# caractere.
nombre = 15
print("Le nombre est " + str(nombre))

print("\nExercice 4")
# Exercice 4
# Notions abordees: les variables
# Pour reussir l'exercice, vous devez printer la valeur que contient la variable 'a'.
a = 3
b = 6
a = b
b = 7
# trouver la valeur de a
print(6)

print("\nExercice 5")
# Exercice 5
# Notions abordees: La fonction print.
# Dans cette exercice, nous allons utiliser les nouvelles fonctionnalites de python 3, afin de printer les 3 variables a, b et c, separees par un symbole d'addition(+)
a = 2
b = 6
c = 3
print(a, b, c, sep=" + ")

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

print("\nExercice 8")
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

print("\nExercice 9")
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

print("\nExercice 10")
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

print("\nExercice 11")
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

print("\nExercice 12")
# Exerice 12
# Notions abordees: Les listes.
# Dans cet exercice, on contiue avec des operations assez simples utilisant les bases du langage Python.
# Le but ici est de crrer une liste de nombres allant de 5 à 15 en utilisant une fonction de base de Python.
# Pour valider l'exercice, vous devez afficher cette liste, en utilisant la fonction print.
list1 = []
for i in range(5, 16):
    list1.append(i)
print(list(list1))

print("\nExercice 13")
# Exercice 13
# Notions abordees: les listes.
# Dans cet exercice, on continue avec la fonction range, cette fois-ci pour creer une liste de nombres pairs allant de 1 à 100.
# Votre script doit afficher la liste, pensez donc à faire un print à la fin, si vous faites juste declarer la liste,
# l'exercice ne sera pas valide
list1 = []
for i in range(2, 101, 2):
    list1.append(i)
print(list(list1))

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
# 6
for i in range(1, 7):
    j = random.choice(range(1, 7))
    print(j)

print("\nExercice 15")
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

print("\nExercice 16")
# Exercice 16
# Notions abordees: les listes.
# On retourne aux bases de Python dans cet exercice dans lequel vous devez tout simplement recuperer le premier element de la liste.
# Dans cet exemple, vous devez printer la chiane de caractere 'Pierre'
# ma_liste = ["Pierre", "Paul", "Marie"]
ma_liste = ["Pierre", "Paul", "Marie"]
print(ma_liste[0])

print("\nExercice 17")
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

print("\nExercice 18")
# Exercice 18
# Notions abordees: les listes.
# On continue avec les listes. Cetter fois-ci, l'objectif de l'exercice est de recuperer un element sur deux dans la liste.
# Votre scritp doit donc printer la liste suivante: [1, 3, 5, 7, 9]
ma_liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(ma_liste[0:11:2])

print("\nExercice 19")
# Exercice 19
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

print("\nExercice 20")
# Exercice 20
# Dans cet exercice, vous allez devoir recuperer les elements communs aux deux listes.
# Dans ce cas-ci, votre liste commune devra contenir les nombres 5, 7, 10
# Vous pouvez utiliser les sets pour cet exercice
# Pour aller plus loin essayez de faire cet exercice sans utiliser les sets
liste_01 = [1, 5, 6, 7, 9, 10, 11]
liste_02 = [2, 3, 5, 7, 8, 10, 12]
print(list(set(liste_01).intersection(set(liste_02))))

# le meme exercice avec deux boucles à la place du set()
print("")
liste_01 = [1, 5, 6, 7, 9, 10, 11]
liste_02 = [2, 3, 5, 7, 8, 10, 12]
ma_liste = []
i, j = 0, 0
for j in liste_01:
    result = 0
    for i in liste_02:
        if (i == j):
            ma_liste.append(i)
print(ma_liste)

print("\nExercice 21")
# Exercice 21
# Dans cet article, l'objectif est de trier une liste qui contient des tuples:
# liste = [("Harry Potter", 5), ("Wall-E", 3), ("Blade Runner", 4)]
# Comme vous pouvez le voir, la liste contient des tuples qui ont comme premier element le nom d'un film, et comme deuxieme element
# leur note sur 5.
# Le but de l'exercice est de trier ces tuples en fonction de la note qui leur a ete attribuee.
# Votre script doit donc retourner la liste suivante:
# [('Wall-E, 3), ('Blade Runner', 4), ('Harry Potter', 5)]
liste = [("Harry Potter", 5), ("Wall-E", 3), ("Blade Runner", 4)]
liste = sorted(liste, key=lambda colonnes: colonnes[1])
print(liste)

print("\nExercice 22")
# Exercice 22
# Dans cet exercice, nous allons recuperer la valeur de la cle 'prenom', contenue dans le dictionnaire 'employe'.
# Votre script doit donc retourner la chaine de caractere 'Pierre'.
# Aller plus loin : contstruisez votre script de sorte à ce qu'il ne produise aucune erreur si les cles du dictionnaire
# venaient à etre modifiees.
employes = {"01": {"identite": {"prenom": "Pierre", "nom": "Dupont"}}}
# si la clef n'est pas trouve le script plante, imaginons que l'on cherche la clef 1 au lieu de 01
print(employes['01']["identite"]["prenom"])
# on retourne rien si la clef n'est pas trouve
print(employes.get("01", {}).get("identite", {}).get("prenom", "valeur inconnue"))

print("\n Exercice 23")
# Exerice 23
# Notions abordees: les dictionnaires.
# On continue avec les dictionnaires ! Dans cet exercice, vous devez aaditionner toutes les valeurs
# du dictionnaire ensemble. Votre script doit donc retourner le nombre 8700.
# Allez plus loin: Esseayer de faire tenir votre scipt en une seule ligne
employes = {"Pierre": 2500, "Marie": 5000, "Julien": 1200}
values = 0
for value in employes.values():
    result += value
print(result)

print("Exercice 23 bis")
# autre solution:
employes = {"Pierre": 2500, "Marie": 5000, "Julien": 1200}
print(sum(employes.values()))

print("\n Exercice 24")
# Notions abordees: Les modules.
# Nous passons maintenant avec un exercice simple sur les modules.
# Le script actuel ne fonctionne pas et vous retournera une erreur. A vous de trouver où se situe l'erreur afin que le script fonctionne.
# Votre script doit au final retourner un nombre aleatoire compris entre 0 et 5.
nombre_aleatoire = random.randint(0, 5)
print(nombre_aleatoire)

print("\n Exercice 25")
# Notions abordees: syntaxe.
# On continue avec les erreurs et la syntaxe. Le script suivant ne fonctionne pas, à vous de trouver pourquoi et le corriger.
# Votre script doit retourner la liste [2, 6, 12, 20, 42, 56, 90]
liste = [1, 1, 4, 3, 3, 2, 6, 7, 7, 9, 2]

resultat = [i*(i+1 % (i*5)) for i in sorted(list(set(liste)))]
print(resultat)

print("\n Exercice 26")
# Notions abordees: Les modules, les variables.
# Dans cette exercice, nous allons importer une variable d'un autre module dans notre script principal.
# Dans le fichier constants.py se trouve une variable 'nom' qui contient le mot 'Udemy'.
# Le but de l'exercice est d'importer cette variable dans le fichier exercice.py pour l'afficher grace à la fonction print.
print(constants.nom)


print("\n Exercice 27")
# Afficher le chemin du script python en cours
fichier_courant = __file__
dossier_parent = os.path.dirname(fichier_courant)
dossier_image = os.path.join(dossier_parent, "images")
print(dossier_image)

print("\n Exercice 28")
# Notions abordees: le module OS.
# Le but de cet exercice est de recuperer l'extension d'un fichier à l'aide du module OS.
# Dans cas-ci, vous devez recuperer l'extension du fichier python.exe
# Votre script doit retourner l'extension sans le point. Vous devez donc recuperer 'exe'.
fichier = "C:/Python36/python.exe"

_, ext = os.path.splitext('C:/Python36/python.exe')
print(ext)

print("\n Exercice29")
# Exercice 29
# Acceder à une variable d'environnement PATH et HOME
print(os.environ.get('PATH'))
print("")
print(os.environ.get)  # retourne toutes les variables d'environnement

print("\n Exercice30")
# Exercice 30
# Calculer le temps d'execution d'un script
start_time = time.time()
_ = [i*2 for i in range(9999999)]
print("Temps d'execution: %s secondes ---" % (time.time()-start_time))

print("\n Exercice31")
# Exercice 31
# Notions abordees: les structures conditionnelles, les nombres.
a = 0
if a is not None:
    print("la valeur de a est %i:" % a)

print("\n Exercice32")
# Exercice 32
# Notions abordees: Les chaines de caracteres.
# Le but de cet exercice est d'afficher dans le print le nom et le prenom contenu dans les variables respectives.
# Vous devez pour ceci utiliser la fonction format afin.
# Votre script doit donc afficher au final: "Bonjour je m'appelle Pierre Dupont"
# https://vbaforexcel.wordpress.com/2015/05/19/affichage-fonction-print/
prenom = "Pierre"
nom = "Dupont"
print("Bonjour je m'appelle Mr " + nom + " " + prenom)
print("Bonjour je m'appelle Mr {0} {1}" .format(nom, prenom))
print("Bonjour je m'appelle Mr %s, %s" % (nom, prenom))

print("\n Exercice33")
# Exercice 33
# Notions abordees: Les chaines de caractere.
# Dans cet exercice, vous allez devoir inverser l'ordre des lettres d'un mot.
# Dans cet exemple-ci, le mot est 'Udemy' votre script doit donc retourner la chaine de caractere 'Ymedu'
# Pour valider l'exercice, il faut que la premiere lettre de votre chaine de caractere resultat soit
# en majuscule("Ymedu" et non 'ymedU')
# Aller plus loin: Faites tenir votre script en une seule ligne
mot = "Udemy"
print(mot[::-1].capitalize())

# autre possibilite:
mot = "Udemy"
resultat = []
for lettre in reversed(mot):
    resultat.append(lettre)
resultat_formate = "".join(resultat)
print(resultat_formate.capitalize())

print("\n Exercice34")
# Exercice 34
# Notions abordees: le module random.
# Dans cet exercice, nous allons melanger les lettres d'un mot grace au module random.
# Le mot resultant devra commencer par une majuscule. Dans cet exercice nous allons melanger le mot 'Bonjour'.
# Votre script devra melanger les lettres de ce mot pour donner par exemple: 'Ojoubr'.
a = list("bonjour")
random.shuffle(a)
print(("".join(a)).capitalize())

print("\n Exercice35")
# Exercice 35
# Notions abordees: la fonction format.
# Dans cet exercice, nous voulons tronquer le nombre de decimales contenues apres la virgule dans la variable 'nombre', par le nombre
# contenu dans la variable 'decimales'.
# votre script doit donc afficher: 'Nombre tronque:2938.489'
nombre = 2938.48872
decimale = 3
print("Nombre tronqué: {nombres:.{decimales}f}".format(
    nombres=nombre, decimales=decimale))

print("test de la valeur toto: {toto}".format(toto=decimale))
