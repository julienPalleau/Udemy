class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages


b = Book('Python rocks', 'Jose', 200)
print(b)  # you just get get the book object adress in memory, if you wish the variables values you need to use __str__ or string representation

""" Attributes """


class Book1():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):  # str is a special method and means string representation and is used to print what is in the object
        return f"{self.title} by {self.author}"

    def __len__(self):  # lengh is another special method
        return self.pages

    def __del__(self):  # del is another special method used to destroy an object and free up memory
        print("A book object has been deleted")


b = Book1('Python rocks', 'Jose', 200)
print(b)
print(len(b))
del b
