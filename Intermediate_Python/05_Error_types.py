### Error Types ###

## SyntaxError

#print "Hello people"   #Error. SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
print("Hello people")   # = Hello people


## NameError

language = "spanish"
#print(language2)       #Error. NameError: name 'language2' is not defined
print(language)         # = Spanish


# IndexError

my_list = ["Python", "Kotlin", "Java", "JavaScript"]
print(my_list[0])       # = Python
print(my_list[-1])      # = JavaScript
#print(my_list[4])      #Error. IndexError: list index out of range


# ModuleNotFoundException

#import maths            # ModuleNotFoundError: No module named 'maths'
import math


# AttributeError

#print(math.PI)          # AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?
print(math.pi)


# KeyError

my_dict = {"name":"Jorge", "surname":"Agulló", "age":39, "heigth":1.87}
#print(my_dict["edad"])  # KeyError: 'edad'
print(my_dict)           # = {'name': 'Jorge', 'surname': 'Agulló', 'age': 39, 'heigth': 1.87}


# TypeError

#print(my_list["0"])     # TypeError: list indices must be integers or slices, not str
print(my_list[0])        # = Python


# ImportError

#from math import Pi     # ImportError: cannot import name 'Pi' from 'math' (unknown location)
from math import pi
print(pi)                # = 3.141592653589793


# ValueError

#my_int = int("10 años") # ValueError: invalid literal for int() with base 10: '10 años'
my_int = int("10")
print(my_int)            # = 10


# ZeroDivisionError

#print(4/0)              # ZeroDivisionError: division by zero
print(4/2)               # = 2
