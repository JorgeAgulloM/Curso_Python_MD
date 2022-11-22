### Strings ###

my_string = "My String"
my_other_string = 'My other String'

print(len(my_string))                       # = 9
print(len(my_other_string))                 # = 15

print(my_string + my_other_string)          # = My StringMy other String
print(my_string, my_other_string)           # = My String My other String
print(my_string + " " + my_other_string)    # = My String My other String
print(my_string + "\n" + my_other_string)   # = My String 
                                            #   My other String
print('This text containe\na line break')   # = This text containe 
                                            #   a line break
print('This text containe \n a line break') # = This text containe 
                                            #     a line break
print('This text containe \t a tab')        # = This text containe      a tab
print('This text containe \\t a tab')       # = This text containe \t a tab


# Strings Format
name, surname, age = 'Jorge', 'Agullo', 39

print('My name is', name, surname, 'and im', age, 'years old')              # = My name is Jorge Agullo y mi edad es 39 !!!BAD
print('My name is {} {} and im {} years old'.format(name, surname, age))    # = My name is Jorge Agullo y mi edad es 39
print('My name is %s %s and im %d years old' %(name, surname, age))         # = My name is Jorge Agullo y mi edad es 39
print('My name is {name} {surname} and im {age} years old')                 # = My name is {name} {surname} and im {age} years old
# formatted with f first
print(f'My name is {name} {surname} and im {age} years old')                # = My name is Jorge Agullo and im 39 years old


# Char unpacking
language = "python"
a, b, c, d, e, f = language

print(a) # = P
print(c) # = t
print(f) # = n


# Char division
print(language[1:3])    # = yt
print(language[1:])     # = ython
print(language[0:6:2])  # = Pto
print(language[-2])     # = o
print(language[-3])     # = h


# Reverse
print(language[::-1])   # = nohtyP


# System functions
print(language.capitalize())            # = Python
print(language.upper())                 # = PYTHON
print(language.lower())                 # = python
print(language.count("t"))              # = 1
print(language.isnumeric())             # = false
print("1".isnumeric())                  # = true
print(language.upper().isupper())       # = true
print(language.upper().islower())       # = false
print(language.startswith("py"))        # = true
print(language.startswith("Py"))        # = false

