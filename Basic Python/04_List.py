### Lists ###

my_list = list()  # No confundir con las tuplas, que se definen my_list = () or my_list = tuple()
my_other_list = []

print(len(my_list))             # = 0
print(type(my_list))            # = class list
print(len(my_other_list))       # = 0 
print(type(my_other_list))      # = class list

my_list = [32, 45, 56, 56, 73, 39, 91, 19]
print(len(my_list))             # = 8
print(type(my_list))            # = class list

my_other_list = [39, 1.87, "Jorge", 'Agulló']
print(len(my_other_list))       # = 4
print(my_other_list)            # = [39, 1.87, 'Jorge', 'Agulló']

print(my_other_list[0])         # = 39
print(my_other_list[1])         # = 1.87
print(my_other_list[2])         # = Jorge
print(my_other_list[3])         # = Agulló
#print(my_other_list[4])        # = IndexError

print(my_other_list[-4])        # = 39
print(my_other_list[-3])        # = 1.87
print(my_other_list[-2])        # = Jorge
print(my_other_list[-1])        # = Agulló

# Repeat values counted
print(my_other_list.count("Jorge"))     # = 1
print(my_list.count("Jorge"))           # = 0
print(my_list.count(56))                # = 2

age, heigth, name, surname = my_other_list
print(age)              # = 39
print(heigth)           # = 1.87
print(name)             # = Jorge
print(surname)          # = Agulló

fusion_list = my_list + my_other_list
print(fusion_list)      # = new list with all data [32, 45, 56, 56, 73, 39, 91, 19, 39, 1.87, 'Jorge', 'Agulló']

#fusion_list = my_list - my_other_list      # Error

# add elements at list
my_list.append("Hello")         # = [32, 45, 56, 56, 73, 39, 91, 19, 'Hello']
print(my_list)

# add elements at list with especific position
my_list.insert(1, "blue")
print(my_list)                  # = [32, 'blue', 45, 56, 56, 73, 39, 91, 19, 'Hello']

# change value of element
my_list[1] = "Red"
print(my_list)                  # = [32, 'red', 45, 56, 56, 73, 39, 91, 19, 'Hello']

# remove elements at list with especific position
my_list.remove("Red")
print(my_list)                  # = [32, 45, 56, 56, 73, 39, 91, 19, 'Hello']

# remove with pop method. Pop returns value element removed
my_list.pop()
print(my_list.pop())            # = 19
print(my_list)                  # = [32, 45, 56, 56, 73, 39, 91]

# remove with pop method with especific index element and return value
print(my_list.pop(2))           # = [32, 45, 56, 73, 39, 91, 19]

########## Pop is used for unstack

my_list.clear()
print(my_list)                  # = []

my_list = [32, 45, 56, 73, 39, 91, 19]
# copi elements with first variable reference
my_new_list = my_list
print(my_new_list)              # = same values to my_list with state in al process
my_list.clear()                 
print(my_new_list)              # = []

# copi elements without first variable reference
my_new_list = my_other_list.copy()
print(my_new_list)              # = same values in this point without my_list reference
my_other_list.clear()          
print(my_new_list)              # = [39, 1.87, 'Jorge', 'Agulló']

# reverse values
#print(my_new_list.reverse())   # = none
# the reverse method has to be applied on the varialbe first
my_new_list.reverse()
print(my_new_list)              # = ['Agulló', 'Jorge', 1.87, 39]

# order
# my_new_list.sort() ### sort return error with different types of values
my_new_list = [32, 45, 56, 56, 73, 39, 91]
print(my_new_list)              # = [32, 45, 56, 56, 73, 39, 91]

# sublist
print(my_new_list[1:3])         # = [45, 56]


print(type(my_list))    # class list
my_list = "Hello"       # CARE WITH THIS!!!!!
print(type(my_list))    # class str
