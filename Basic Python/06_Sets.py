### Sets ###

my_set = set()
my_other_set = {}

print(type(my_set))             # class set
print(type(my_other_set))       # class dic ??

my_other_set = {39, 1.87, "Jorge", 'Agulló'}
print(type(my_other_set))       # class set

# The Sets are not structured in order, 
# each time they are queried they will display the objects in a different order.
my_other_set.add("Hello")
print(my_other_set)        

# it is not posible repeat the values in Sets.
my_other_set.add("Hello")
print(my_other_set)     

# print(my_other_set[1])        # Error. When there is no order, a specific element cannot be accessed.

# It is possible to search for a specific item
print("Jorge" in my_other_set)  # = True
print("Jorga" in my_other_set)  # = False

# delete element
my_other_set.remove("Jorge")
print(my_other_set)             # = {1.87, 39, 'Agulló', 'Hello'}


# delete element??
##my_other_set.remove("Jorge")  # Error
# Sets are especially good for "listing" items that do not require ordering

my_other_set.clear()
print(my_other_set)             # = set()

my_set = {39, 1.87, "Jorge", 'Agulló'}
print(my_set)                   # = {1.87, 'Jorge', 39, 'Agulló'}
my_set = list(my_set)
print(my_set)                   # = [1.87, 'Jorge', 39, 'Agulló']

my_set = {39, 1.87, "Jorge", 'Agulló'}
my_other_set = {"Kotlin", "Java", "Python", 'CSharp'}
my_new_set = my_set.union(my_other_set)
print(my_new_set)               # = {1.87, 'CSharp', 'Python', 39, 'Kotlin', 'Java', 'Agulló', 'Jorge'}

my_new_set = my_new_set.union(my_set)
print(my_new_set)               # have no changes, because it is not possible to repeat values in the Sets

# diference beetwin the two sets
print(my_new_set.difference(my_set))    # = {'Java', 'Python', 'Kotlin', 'CSharp'}




####### El porque user una lista, una tupla o un set
"""
    # Tupla: Si queremos que nuestra lista de elementos sea inmutable, una tupla es la mejor opción.
    # Set: Si queremos tener preferencia en cuanto a valores repetidos y no nos importa el orden de
    la misma, aquí el rey es el set.
    # List: Si todo lo anterior no nos importa y necesitamos acceso a las posiciones de cada elemento
    lo mejor es utilizar una list.
    
    Al final todo depende de la contexto de uso de las mismas, debiendo razonar la opción a tomar debidamente
    antes de usar una u otra.
    """

