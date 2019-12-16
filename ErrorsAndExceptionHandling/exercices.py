""" Problem 1 """

try:
    for i in ['a', 'b', 'c']:
        print(i**2)
except TypeError:
    print("erreur i n'est pas un entier!")


""" Problem 2 """

try:
    x = 5
    y = 0
    z = x/y
except ZeroDivisionError:
    print("La division par 0 est impossible !")
finally:
    print("All Done")


""" Problem 3 """


def ask():
    while True:
        try:
            n = int(input("Veuillez saisir un entier : "))
        except:
            print("Svp veuillez saisir un entier ex: 1,2,3 ... n")
        else:
            return f"Your number squared is: {n**2}"


print(ask())
