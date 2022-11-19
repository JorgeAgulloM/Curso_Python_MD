### Aritmetic operators ###

# Simple operations
print('Addition:', 3 + 4)                           # = 7
print('Substraction:', 3 - 4)                       # = -1
print('Multiplication:', 3 * 4)                     # = 12
print('Division:', 3 / 4)                           # = 0.75
print('Modulus:', 10 % 3)                           # = 1 Module operator. Rest returned
print('Division without the remainder:', 10 // 3)   # = 3 floor division discards the fractional part
print('Exponentiation:', 4 ** 3)                    # = 64 squared "Potencia, 4 elevado a 3"
print(2 ** 3 + 3 - 7 / 2 // 4)                      # = 11.0
print('Complex number: 1 + 1j')                     # = 1 + 1j

a = 3
b = 4

total = a + b
diff = a - b + b
product = a * b + b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

print('a + b =', total)
print('a - b =', diff)
print('a * b =', product)
print('a / b =', division)
print('a % b =', remainder)
print('a // b =', floor_division)
print('a ** b =', exponential)



# String operations
print('Hello' + 'Python')                       # = Hello Python
# print('Hello' + 5)                            Error
# print('Hello' / 5)                            Error
# print('Hello' * 5.5)                          Error
#my_val = 2.5 * 2                               # = 5.0 float
#print('Hello' * my_val)                        # Error, string chain cannot be multiplied by floats
print('Hello' + str(5))                         # = Hello 5
print('Hello' * 5)                              # = HelloHelloHelloHelloHello
print('Hello' * int(2 ** 3 + 3 - 7 / 2 // 4))   # = HelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHello


### Comparative operators ###
print(3 > 4)            # false
print(3 < 4)            # true
print(3 >= 4)           # false
print(3 >= 4)           # true
print(3 == 4)           # false
print(3 != 4)           # true
print(3 > 4 == 2)       # false
print(3 > 4 > 2)        # false
print(3 < 4 > 2)        # true

# compare ASCII alphabetic order
print('Hello' > 'Python')       # false
print('Hello' < 'Python')       # true
print('Hello' >= 'Python')      # false
print('Hello' <= 'Python')      # true
print('Hello' == 'Python')      # false
print('Hello' == 'Hello')       # true
print('Hello' == 'Hellos')      # false
print('Hello' != 'Python')      # true
print('Hello' == 'Holas')       # false
print('aaaa' == 'aaaa')         # true
print('aaaa' == 'abaa')         # true


### Logic operations ###

true = True
false = False

print('true and true = ', true and true, '||', 'not(true and true) = ', not(true and true))           # True || False
print('true and false = ', true and false, '||', 'not(true and false) = ', not(true and false))       # False || True
print('false and true = ', false and true, '||', 'not(false and true) = ', not(false and true))       # false || True
print('false and false = ', false and false, '||', 'not(false and false) = ', not(false and false))   # True || False



print('3 > 4 and "Hello" > "Python" =', 3 > 4 and "Hello" > "Python")                                   # false
print('3 > 4 or "Hello" > "Python" =',3 > 4 or "Hello" > "Python")                                      # false
print('3 < 4 and "Hello" > "Python =', 3 < 4 and "Hello" > "Python")                                    # false
print('3 < 4 or "Hello" > "Python" =', 3 < 4 or "Hello" > "Python")                                     # true
print('3 < 4 and "Hello" < "Python" =', 3 < 4 and "Hello" < "Python")                                   # true
print('3 < 4 and ("Hello" < "Python" or 3 > 4) =', 3 < 4 and ("Hello" < "Python" or 3 > 4))             # true
print('not(3 < 4 and ("Hello" < "Python" or 3 > 4))', not(3 < 4 and ("Hello" < "Python" or 3 > 4)))     # false
