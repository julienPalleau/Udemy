import math


def count_primes():
    mylist = [2, 3, 5, 7]
    nombre = int(input("Entrer un nombre: "))
    i = 3

    while i < nombre:
        if (i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0):
            mylist.append(i)
        i = i + 1

    print(mylist)


count_primes()
