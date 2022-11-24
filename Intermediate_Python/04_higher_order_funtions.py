### Higher Order Funtions ###

from functools import reduce


def sum_one(vale):return vale + 1
def sum_five(vale):return vale + 5

def sum_two_values_and_add_one(first_values, second_value):
    return sum_one(first_values + second_value)

print(f"Result higher function: {sum_two_values_and_add_one(5, 2)}")            # = Result higher function: 8


def sum_two_values_and_add_one(first_values, second_value, f_sum):
    return f_sum(first_values + second_value)

print(f"Result higher function: {sum_two_values_and_add_one(5, 2, sum_one)}")   # = Result higher function: 8


def sum_two_values_and_add_value(first_values, second_value, f_sum):
    return f_sum(first_values + second_value)

print(f"Result higher function: {sum_two_values_and_add_value(5, 2, sum_five)}")   # = Result higher function: 12


### Closures ###

def sum_ten():
    def add(value):
        return value + 10
    return add
    
add_closure = sum_ten()
print(add_closure(5))           # = 15


def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add
    
add_closure = sum_ten(1)
print(add_closure(5))           # = 16

print(sum_ten(5)(1))            # = 16


### Build-in Higher Order Funtions ###

numbers = [2, 5, 10, 21, 3, 30]

#Map
def multyply_two(number):
        return number * 2

print(list(map(multyply_two, numbers)))                     # = [4, 10, 20, 42, 3, 30]
print(list(map(lambda number: number * 2, numbers)))        # = [4, 10, 20, 42, 3, 30]

#Filter
def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False

print(list(filter(filter_greater_than_ten, numbers)))       # = [21, 30]
print(list(filter(lambda number: number > 10, numbers)))    # = [21, 30]

#Reduce
def sum_two_values(first_value, second_values):
    return first_value + second_values

print(reduce(sum_two_values, numbers))                      # = 71