import random

def my_func1():
    print ("this is my_func1")

def my_func2():
    print ("this is my_func2")

def my_func3():
    #return "123"
    return False

def my_func4():
    num = random.randint(0, 10)
    if num % 2 == 0:
        return True
    else:
        raise Exception("NOT an even number")