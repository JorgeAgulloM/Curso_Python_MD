### challenges ###

"""
EL FAMOSO FIZZ BUZZ:
 Escribe un programa que muestre por consola (con un print) los
 números de 1 a 100 (ambos incluidos y con un salto de línea entre
 cada impresión), sustituyendo los siguientes:
 - Múltiplos de 3 por la palabra "fizz".
 - Múltiplos de 5 por la palabra "buzz".
 - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""

def fizzbuzz():
    for n in range(1, 101):
        if module_three_and_five(n):
            print("fizzbuzz")
        elif module_five(n): 
            print("buzz")
        elif module_three(n):
            print("fizz")
        else:
            print(n)

def module_three(n) -> bool:
    return n % 3 == 0

def module_five(n) -> bool:
    return n % 5 == 0

def module_three_and_five(n) -> bool:
    return module_three(n) and module_five(n)

#fizzbuzz()

""" finish """

""" 
¿ES UN ANAGRAMA?
 Escribe una función que reciba dos palabras (String) y retorne
 verdadero o falso (Bool) según sean o no anagramas.
 - Un Anagrama consiste en formar una palabra reordenando TODAS
   las letras de otra palabra inicial.
 - NO hace falta comprobar que ambas palabras existan.
 - Dos palabras exactamente iguales no son anagrama.
"""

def is_anagrama(word_one, word_two) -> bool:
    if word_one.lower() == word_two.lower(): return False
    return sorted(word_one.lower()) == sorted(word_two.lower())

# print(is_anagrama("Nacionalista", "Altisonancia"))

""" finsish """

"""
LA SUCESION DE FIBONACCI:
 Escribe un programa que imprima los 50 primeros números de la sucesión
 de Fibonacci empezando en 0.
 - La serie Fibonacci se compone por una sucesión de números en
   la que el siguiente siempre es la suma de los dos anteriores.
   0, 1, 1, 2, 3, 5, 8, 13...
"""

def fibonacci_one() -> list :
    result = list()
    for n in range(50):
        if len(result) < 1:
            result.append(n)
        elif len(result) == 1:
            result.append(n + result[n - 1])
        else:
            result.append(result[n - 1] + result[n - 2])
        
    return result

def fibonacci_two() -> list:
    _prev = 0
    _next = 1
    
    for _ in range(50):
        print(_prev)
        
        _fib = _prev + _next
        _prev = _next
        _next = _fib    
        

## print(fibonacci_one())
## print(fibonacci_two())
    
""" finish """

"""
¿ES UN NÚMERO PRIMO?
 Escribe un programa que se encargue de comprobar si un número es o no primo.
 Hecho esto, imprime los números primos entre 1 y 100. 
"""


def is_prime_number(number):
    number_prime = True
    primes = list()
    
    for index in range(2, 101):
        
        is_prime = True
        
        if number_prime and index < number and number % index == 0:
            number_prime = False
        
        for n in range(2, index):
            if index % n == 0:
                is_prime = False
                break
            
        if is_prime:
            primes.append(index)
            
    print(f"¿El número {number} es primo?: {number_prime}")
    print(primes)

# is_prime_number(11)
# is_prime_number(23)
# is_prime_number(25)
# is_prime_number(51)
# is_prime_number(89)





""" Generador de contraseñas """
    
import secrets
import string

def generate_pass(pwd_length = 14) -> str:
    letters = string.ascii_letters
    digits = string.digits
    especial_chars = string.punctuation
    alphabet = letters + digits + especial_chars
    
    pwd = ""
    for _ in range(pwd_length):
        pwd += ''.join(secrets.choice(alphabet))
    
    return pwd

# print(generate_pass(14))

""" finish """