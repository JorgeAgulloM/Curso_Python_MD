### File Handling ###

### .txt file
dir_file = "Intermediate_Python\my_text_file.txt"
#txt_file = open("Intermediate_Python\my_text_file.txt", "r")    # read
#txt_file = open("Intermediate_Python\my_text_file.txt", "r+")   # read and write
#txt_file = open("Intermediate_Python\my_text_file.txt", "w")    # write
txt_file = open(dir_file, "w+")                                  # write and Override
txt_file.write("my name is Jorge \nmy surname is Agullo \nmy age is 40 \nmy favorite language is Python")

print(txt_file.read(10))            # reads 10 more characters after the previous reading (empty)

# read line to line
txt_file = open(dir_file, "r+")     # read and write
print(txt_file.readline())          # = my name is Jorge
print(txt_file.readline())          # = my surname is Agullo

# read all and list encaptusalated
txt_file = open(dir_file, "r+")     # read and write
print(txt_file.readlines())         # = ['my name is Jorge\n', 'my surname is Agullo\n', 'my age is 40\n', 'my favorite language is Python']

txt_file = open(dir_file, "r+")     # read and write
for line in txt_file.readlines():
    print(line)
    
# add new data
txt_file.write("\nalthough i also like kotlin language too")
txt_file = open(dir_file, "r+")     # read and write
print(txt_file.readlines())         # = ['my name is Jorge\n', 'my surname is Agullo\n', 'my age is 40\n', 'my favorite language is Python\n', 'but i love kotlin language\n', 'but i also like kotlin language\n', 'but i also like kotlin language']            # =

# close file
txt_file.close()

import os
#os.remove(dir_file)


### .json file

import json

dir_json = "Intermediate_Python\my_file.json"
json_file = open(dir_json, "w+")

json_data = {
    "name":"Jorge", 
    "surname":"Agullo", 
    "age":39, 
    "heigth":1.87,
    "languages": ["Python", "Kotlin", "Java", "Swift"],
    "experience": ["Android Developer", "Control Specialist", "Scada supervisor"]
}

json.dump(json_data, json_file, indent=4)

json_file.close()

with open(dir_json) as my_other_file:
    for line in my_other_file.readlines():
        print(line)
    my_other_file.close()


# parse to dict
json_dict = json.load(open(dir_json))
print(type(json_dict))      # = <class 'dict'>
print(json_dict)            # = {'name': 'Jorge', 'surname': 'Agullo', 'age': 39, 'heigth': 1.87, 'languages': ['Python', 'Kotlin', 'Java', 'Swift'], 'experience': ['Android Developer', 'Control Specialist', 'Scada supervisor']}
print(json_dict["name"])    # = Jorge