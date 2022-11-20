### Dictionaries ###

# dictionaries is a data structure listed by key:value. It's same to Json file

my_dict = dict()
my_other_dict = {}

print(type(my_dict))            # = class dict()
print(type(my_other_dict))      # = class dict()

my_dict = {"name":"Jorge", "surname":"Agulló", "age":39, "heigth":1.87}
print(my_dict)                  # = {'name': 'Jorge', 'surname': 'Agulló', 'age': 39, 'heigth': 1.87}


# add values with key:value
my_other_dict = {               
    "name":"Jorge", 
    "surname":"Agulló", 
    "age":39, 
    1:1.87,
    "languages": {"Kotlin", "Java", "Python"}
    }

print(my_other_dict)    # = _
#{'name': 'Jorge', 'surname': 'Agulló', 'age': 39, 1: 1.87, 'languages': {'Java', 'Python', 'Kotlin'}}

print(len(my_other_dict))           # = 5

# observ values
print(my_other_dict["name"])        # = Jorge
print(my_other_dict["languages"])   # = {'Kotlin', 'Java', 'Python'}
print(my_other_dict["surname"])     # = Agulló

# change values
my_other_dict["name"] = "Yorch"
print(my_other_dict["name"])        # = Yorch

# add new key with value
my_other_dict["nick"] = "Jorge"
print(my_other_dict)                # = _
# {'name': 'Yorch', 'surname': 'Agulló', 'age': 39, 1: 1.87, 'languages': {'Kotlin', 'Python', 'Java'}, 'nick': 'Jorge'}


print(my_other_dict.items())                    # = _
#dict_items([('name', 'Yorch'), ('surname', 'Agulló'), ('age', 39), (1, 1.87), ('languages', {'Python', 'Java', 'Kotlin'}), ('nick', 'Jorge')])
print(my_other_dict.keys())                     # = dict_keys(['name', 'surname', 'age', 1, 'languages', 'nick'])
print(my_other_dict.values())                   # = dict_values(['Yorch', 'Agulló', 39, 1.87, {'Python', 'Java', 'Kotlin'}, 'Jorge'])

# create a new dict with keys without values
print(my_other_dict.fromkeys(("name", "age")))  # = {'name': None, 'age': None}

my_key_list = ("name", "nick", "age")
print(my_other_dict.fromkeys(my_key_list))      # = {'name': None, 'nick': None, 'age': None}

my_key_list = ["name", "nick", "age"]
print(my_other_dict.fromkeys(my_key_list))      # = {'name': None, 'nick': None, 'age': None}

# create new dict with other dict keys
print(my_other_dict.fromkeys(my_other_dict))    # = {'name': None, 'surname': None, 'age': None, 1: None, 'languages': None, 'nick': None}