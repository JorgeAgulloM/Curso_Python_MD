### Python Package Manager ###

# PIP https://pypi.org/


# How install pip >>> pip install pip --user  
# How update pip >>> pip install --upgrade pip --user 
 
# How install numpy >>> pip install numpy --user   

import numpy

print(numpy.version.version)                                # = 1.23.5

np_array = numpy.array([32, 45, 56, 56, 73, 39, 91, 19])
print(type(np_array))                                       # = <class 'numpy.ndarray'>
print(np_array)                                             # = [32 45 56 56 73 39 91 19]
np_array *= 2
print(np_array)                                             # = [ 64  90 112 112 146  78 182  38]