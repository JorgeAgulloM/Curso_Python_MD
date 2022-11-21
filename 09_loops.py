### Loops ###

# While

my_condition = 0

while my_condition < 10:
    my_condition += 2
    print(f"my_condition = {my_condition}")
else:
    print("my_condition is upper than my_condition")


## use break
my_condition = 0

while my_condition < 20:
    my_condition += 3
    print(f"my_condition = {my_condition}")
    if my_condition == 15:
        print("break. my_condition is 15")
        break
else:
    print("my_condition is upper than my_condition")
    

# For

my_list = [24, 54, 64, 34, 12, 9, 50, 34]

for elemets in my_list:
    print(elemets)
    
my_tuple = (39, 1.87, "Jorge", 'Agulló')

for elemets in my_tuple:
    print(elemets)
    
# use brak & continue
my_dict = {"name":"Jorge", "surname":"Agulló", "age":39, "heigth":1.87}

for elements in my_dict:
    print(elements)
    if elements == "age":
        print("Break for")
        break
    else:
        continue
    
    
for elements in list(my_dict.values()):
    print(elements)
else:
    print("Block finished")