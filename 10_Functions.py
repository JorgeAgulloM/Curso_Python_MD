### Functions ###

def my_function():
    print("My first function")


# call function
my_function()
print(my_function())                        # = none


def say_hello(name: str):
    print("Hello {}, Welcome to Python".format(name))


print(say_hello("Yorch"))                   # = Hello Yorch, Welcome to Python


# with default parameters
def say_hello_adn_language(name: str, laguage="Python"):
    print("Hello {}, Welcome to {}".format(name, laguage))


say_hello_adn_language("Yorch")                 # = Hello Yorch, Welcome to Python
say_hello_adn_language("Yorch", "Kotlin")       # = Hello Yorch, Welcome to Kotlin


# add parameters without type
def sum_values(a, b):
    return a + b
    # it is not necessary to declare the types of the parameters,
    # it would only be something indicative, because the function
    # will swallow any value that we pass to it, it will happen that
    # if we do not pass the parameters of suitable type it can that the
    # operation that contains the function does not work.


print(sum_values(5, 10))                    # = 15
print(sum_values("Hello!", "Python"))       # = Hello!Python
print(sum_values(2.5, 5))                   # = 7.5
# print(sum_values(2.5, "Hello!"))          # error
my_result = sum_values(30, 20)
print(my_result)                            # = 50


# Infinite parameters
def infinite_params(*things):
    print(things)                           # = ('Hello', 5, 'Jorge', 'Py')
    print(type(things))                     # = class tuple
    for text in things:
        print(text)                         # = Hello
                                            #   5
                                            #   Jorge
                                            #   Py


infinite_params("Hello", 5, "Jorge", "Py")