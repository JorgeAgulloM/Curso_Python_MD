### TUPLES ###

my_tuple = tuple()
my_other_tuple = ()
my_other_tuple = (34, 26, 90)

my_tuple = (39, 1.87, "Jorge", 'Agulló')
print(type(my_tuple))           # = class tuple
print(my_tuple)                 # = (39, 1.87, "Jorge", 'Agulló')

print(my_tuple[2])  
print(my_tuple[-1]) 
#print(my_tuple[6])             # error
#print(my_tuple[-4])            # error

print(my_tuple.count(39))       # = 1
print(my_tuple.count(41))       # = 0

print(my_tuple.index("Jorge"))  # = 2

#my_tuple[1] = 1.90             # error. Tuples are inmutable

my_new_tuple = my_tuple + my_other_tuple
print(my_new_tuple)             # = (39, 1.87, 'Jorge', 'Agulló', 34, 26, 90)
print(my_new_tuple[1:5])        # = (1.87, 'Jorge', 'Agulló', 34)
print(my_new_tuple[0:5])        # = (1.87, 'Jorge', 'Agulló', 34)

my_new_tuple = list(my_new_tuple)
print(type(my_new_tuple))       # = class list

#### Tuples are for using values that we know should not be mutable, 
#       so if we want the data to change we must use another data type or container for the variables.
