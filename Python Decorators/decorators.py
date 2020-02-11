""" Decorator """
""" Before jumping in decoratore we need to look at functions that can return functions """

# The idea here is to get a function to return a function


def hello(name='Julien'):
    print('The hello() function has been executed!')

    def greet():
        return '\t This is the greet() func inside hello!'

    def welcome():
        return '\t This is welcome() func inside hello!'

    print("I am going to return a function!!")

    if name == 'Julien':
        return greet
    else:
        return welcome


my_new_func = hello()
print(my_new_func())


# here is another example of a function returning function
def cool():

    def super_cool():
        return 'I am very cool!'

    return super_cool


some_func = cool()
print(some_func())


# Passing a function as an argument
def hello2():
    return 'Hi Julien!'


def other(some_def_func):
    print('Other code runs here!')
    print(some_def_func())


other(hello2)

# As conclusion: We can returns functions and we can pass functions as an argument !!!

""" Let's have a look to how decorator works, here we are coding the decorator"""


def new_decorator(original_func):

    def wrap_func():
        print('Some extra code, before the original function')
        original_func()
        print('Some extra code, after the original function!')

    return wrap_func


""" Now let's see how to use decorators in python as they are already defined no need to code them """


@new_decorator
def func_needs_decorator():
    print("I want to be decorated!!")


func_needs_decorator()
