#from collections.abc import async_generator
from collections import deque
from random import vonmisesvariate

class myBird:
    def __int__(self):
        print("MyBird class contructor")

    def whatType(self):
        print("I ama a Bird")

    def canSwim(self):
        print("I can Swim")

class myDog:
    def __int__(self):
        print("mydog class contructor")

    def canBArk(self):
        print("i can bark")

class myPinguim(myBird, myDog):
    def __int__(self):
        super().__int__()
        print("myPenguin call contructor")

    def whoisThis(self):
        print("i am penguin")

    def canRun(self):
        print("i can run faster")

#herencia
pg1 = myPinguim()
pg1.canSwim()
pg1.canRun()
pg1.canBArk()
#oop

def my_generator():
    n=1
    print("first")
    yield n
    n+=1
    print("second")
    yield n
    n+=1
    print("third")
    yield n

def reverse_string(my_string):
    length = len(my_string)
    for i in range(length-1,-1,-1):
        yield my_string[i]

a= my_generator()
next(a)
next(a)
next(a)
'''
for item in my_generator():
    print(item)

for char in reverse_string("WORLD"):
    print(char)
'''
#decorators
def make_deco(func):
    def inner_function():
        print("i got decorated ")
        func()
    return inner_function()

@make_deco
def simple_func():
    print("i am simple function")

#simple_func()
#decor = make_deco(simple_func)
#decor()