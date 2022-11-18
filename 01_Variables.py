#Variables
my_string_variable = 'im one string varible'
my_int_variable = 10
my_float_variable = 10.0
my_bool_variable = True

print(my_string_variable)
print(my_int_variable)
print(my_float_variable)
print(my_bool_variable)

# Concatenate variables
print(my_string_variable, my_int_variable, my_bool_variable)
print("My values is:", my_int_variable)

# Parese int to string
my_int_to_str_variable = str(my_int_variable)
print(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable)) #Im a class str

# System funtion eg
print(len(my_string_variable)) #Count of string in this case

# Variables in one line ¡¡USE WITH CARE!!
name, surname, alias, age = "Jorge", 'Agullo', "Yorch", 39
print("My name is", name, surname, ",my alias is", alias, "and my age is", age)

# Input
name = input('what is your name?')
age = input('what is your age?')
print(name)
print(age)

# Change types (soft type)
name = 39
age = "Jorge"
print(name)
print(age)


