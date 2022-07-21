# print("hello, world")
#hdjkjsncjhjs
# jsidskliojkhsej
# jkshujijknjhsjd
# nxjhhsduido

# x, y, z = "orange", "banana", "cherry"

# print(x, y, z)

# x=y=z = "orange"
# print(x, y, z)

# fruits =["apple", "banana", "cherry"]
# x, y, z, = fruits
# print(x)
# print(y)
# print(z)

# x = "awesome"

# def myfunc():
#     global x
#     x = "fanstastic"
#     print("Python is " + x)

# myfunc()

# print("Python is " + x)

# import random

# print(random.randrange(1, 10))
# for x in "banana":
#     print(x)

# b= "Hello, world!"
# print(b[2:5])

# def my_function(fname):
#     print(fname + " Refsnes")

# my_function("Emil")
# my_function("Tobias")
# my_function("linus") 
class myClass:
    x = 5

class erson:
    def __init__(mysillyobject, name, age) -> None:
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("hello my name is " + abc.name)   

p1 = erson("john", 36)

class Person:
    def __init__(self, fname, lname) -> None:
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

# x = Person("john", "doe")
# x.printname()

class Student(Person):
    def __init__(self, fname, lname, year) -> None:
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

# x = Student("Mike", "Olsen", 2019)
# x.welcome()

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)

