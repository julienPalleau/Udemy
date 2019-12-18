""" The all idea of this chapter is about memory used when you iterate
for instance if you run a loop over 1 000 000 you'll get one million
result stored in memory. If you use yield() function you iterate over
1 million 1 at the time as per you need so you only take one memory block
that store 1 number """

""" Use of yield """
print("\n")


def create_cubes(n):
    for x in range(n):
        yield(x**3)


for x in create_cubes(10):
    print(x)


""" Exemple with fibonacci sequence """
print("\n")


def gen_fibon(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a+b


for number in gen_fibon(10):
    print(number)


""" next function """
print("\n")


def simple_gen():
    for x in range(3):
        yield x


for number in simple_gen():
    print(number)

g = simple_gen()
print(g)
print(next(g))
print(next(g))

""" iter function """
print("\n")
s = 'hello'
for letter in s:
    print(letter)
# next(s) it doesn't work, because string object does support iteration
# because we went through a for loop on it but we cannot directly iterate over it
# just like we did for generator using the next() function.

# here it is possible as s_iter is an iter object
print("\n")
s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
