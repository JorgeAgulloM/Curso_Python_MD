### Modules ###

import module_example as me

result = me.sum(26, 11, 1982, 40)
print(result)                                   # = 2059


from module_example import minus, multiply

result = minus(26, 11, 1982, 40)
print(result)                                   # = -2059

result = multiply(26, 11)
print(result)                                   # = 2.3636363636363638


from module_example import division as d

# function imported
result = d(30, 15)
print(result)                                   # = 2.0


import math

print(f"factorial de 4: {math.factorial(4)}")   # = factorial de 4:24


import random

print(f"random number between 4 and 80: {random.randint(4, 80)}")   # = random number between 4 and 80: 35


from math import pi

print(pi)                                       # = 3.141592653589793