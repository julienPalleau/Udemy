""" Problem 1 """
for i in ['a', 'b', 'c']:
    try:
        print(i**2)
    except TypeError:
        print("erreur i n'est pas un entier!")

""" Problem 2 """
x = 5
y = 0
try:
    z = x/y
except ZeroDivisionError:
    print("La division par 0 est impossible !")
finally:
    print("All Done")

""" Problem 3 """


def ask():
    while(True):
        try:
            result = int(input("Veuillez saisir un entier : "))
        except:
            print("Svp veuillez saisir un entier ex: 1,2,3 ... n")
        else:
            return f"Le resultat de l'entier eleve au carre est {result**2}"


print(ask())
