### Regular Expresions ###

import re # R. Expresions module

my_string = "Esta es la lección número 7: Lección llamada Expresiones regulares"
my_other_string = "Esta no es la lección número 7: Expresiones regulares"

print(re.match("Esta es la lección", my_string))                # = <re.Match object; span=(0, 18), match='Esta es la lección'>
print(re.match("Esta es la lección", my_other_string))          # = none

# R.E. defult >>> re.I
match = re.match("Esta es la lección", my_string, re.I)
print(match)                                                    # = <re.Match object; span=(0, 18), match='Esta es la lección'>
start, end = match.span()
print(start, end)                                               # = 0 18
print(my_string[start:end])                                     # = Esta es la lección

match = re.match("Esta no es la lección", my_other_string)
#if match not(match == None): e.g
#if match != None: e.g
if match is not None:
    print(match)                                                # = <re.Match object; span=(0, 18), match='Esta es la lección'>
    start, end = match.span()
    print(my_other_string[start:end])                           # = Esta es la lección


# search

search = re.search("lección", my_string, re.I)
print(search)                                                   # = <re.Match object; span=(11, 18), match='lección'>
start, end = search.span()
print(my_string[start:end])                                     # = lección


# findall

findall = re.findall("lección", my_string, re.I)
print(findall)                                                  # = ['lección', 'lección']


# split

split = re.split(" ", my_string)                                # = ['Esta', 'es', 'la', 'lección', 'número', '7:', 'Lección', 'llamada', 'Expresiones', 'regulares']
print(split)

split = re.split(":", my_string)                                # = ['Esta es la lección número 7', ' Lección llamada Expresiones regulares']
print(split)


# sub

sub = re.sub("Expresiones regulares", "RegEx", my_string)
print(sub)
# = Esta es la lección número 7: Lección llamada RegEx
sub = re.sub("[L|l]ección", "LECCIÓN", my_string)
print(sub)                                                      # = Esta es la LECCIÓN número 7: LECCIÓN llamada Expresiones regulares


# Patterns

pattern = r'[Ll]ección'
print(re.findall(pattern, my_string))                           # = ['lección', 'Lección']

pattern = r'[Ll]ección|Expresiones'
print(re.findall(pattern, my_string))                           # = ['lección', 'Lección', 'Expresiones']
print(re.findall(pattern, my_string))                           # = ['lección', 'Lección']

pattern = r'[a-z]'
print(re.findall(pattern, my_string))                           # = ['s', 't', 'a', 'e', 's', 'l', 'a', 'l', 'e', 'c', 'c', 'i', 'n', 'n', 'm', 'e', 'r', 'o', 'e', 'c', 'c', 'i', 'n', 'l', 'l', 'a', 'm', 'a', 'd', 'a', 'x', 'p', 'r', 'e', 's', 'i', 'o', 'n', 'e', 's', 'r', 'e', 'g', 'u', 'l', 'a', 'r', 'e', 's']

pattern = r'[0-9]'
print(re.findall(pattern, my_string))                           # = ['7']
print(re.search(pattern, my_string))                            # = <re.Match object; span=(26, 27), match='7'>

pattern = r'\d'
print(re.findall(pattern, my_string))                           # = ['7']

pattern = r'\D'
print(re.findall(pattern, my_string))                           # = ['E', 's', 't', 'a', ' ', 'e', 's', ' ', 'l', 'a', ' ', 'l', 'e', 'c', 'c', 'i', 'ó', 'n', ' ', 'n', 'ú', 'm', 'e', 'r', 'o', ' ', ':', ' ', 'L', 'e', 'c', 'c', 'i', 'ó', 'n', ' ', 'l', 'l', 'a', 'm', 'a', 'd', 'a', ' ', 'E', 'x', 'p', 'r', 'e', 's', 'i', 'o', 'n', 'e', 's', ' ', 'r', 'e', 'g', 'u', 'l', 'a', 'r', 'e', 's']

pattern = r'[l].'
print(re.findall(pattern, my_string))                           # = ['la', 'le', 'll', 'la']

pattern = r'[l].*'
print(re.findall(pattern, my_string))                           # = ['la lección número 7: Lección llamada Expresiones regulares']

def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-z]+$"
    return re.match(pattern, email)

print(is_valid_email("agullojorge@gmail.com"))                   # = <re.Match object; span=(0, 21), match='agullojorge@gmail.com'>
print(is_valid_email("agullojorge.gmail.com"))                   # = None
print(is_valid_email("agullojorge.gmail"))                       # = None
print(is_valid_email("agullojorge@gmail"))                       # = None
print(is_valid_email("agullojorge.com"))                         # = None

# https://regex101.com/