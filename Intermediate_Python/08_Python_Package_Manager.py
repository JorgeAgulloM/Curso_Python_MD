### Python Package Manager ###

# PIP https://pypi.org/


# How install pip >>> pip install pip --user  
# How update pip >>> pip install --upgrade pip --user 
# How uninstall pip >>> pip uninstall pip --user 
# How info package >>> pip info PACKAGE --user 
 
# How install numpy >>> pip install numpy --user   

import numpy

print(numpy.version.version)                                # = 1.23.5

np_array = numpy.array([32, 45, 56, 56, 73, 39, 91, 19])
print(type(np_array))                                       # = <class 'numpy.ndarray'>
print(np_array)                                             # = [32 45 56 56 73 39 91 19]
np_array *= 2
print(np_array)                                             # = [ 64  90 112 112 146  78 182  38]


# Pandas

# How install pandas >>> pip install pandas --user

# import pandas as pd


# Pandas

# How install requests >>> pip install requests --user

import requests

# get
response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151") 
print(response)                                                             # = <Response [200]>
print(response.status_code)                                                 # = 200
print(response.json())                                                      # = {'count': 1154, 'next': 'https://pokeapi.co/api/v2/pokemon?offset=151&limit=151', 'previous': None, 'results':...


# Package arithmetics  (my_package)

from my_package import arithmetics as art

print(art.sum(4, 2))                        # = 6

from my_other_package import other_arithmetics as o_art

print(o_art.sum(4, 2))                      # = 6
