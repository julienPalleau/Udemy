import random


""" Problem1 """


def gensquares(N):
    for x in range(N):
        yield(x**2)


for y in gensquares(10):
    print(y)


""" Problem2 """

print("\n")
i = 0


def rand_num(low, high, n):
    for i in range(n):
        yield random.randint(low, high)


for num in rand_num(1, 10, 12):
    print(num)


""" Problem3 """

print("\n")
s = 'hello'
iter_s = iter(s)
print(next(iter_s))
print(next(iter_s))

""" Problem4 """
""" If the output has the potential of taking up a large amount of memory and
you only intend to iterate through it, you want to use a generator. 
