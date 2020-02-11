result = 0


def main():
    n = int(input("Entrez un entier > 0 :"))
    print("Fibonnaci de", n, "est", fibo(n))

# Return the fibonnaci number for the specified number


def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)


main()
