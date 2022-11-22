### classes ###

class MyPerson:
    pass

print(MyPerson)         # = class '__main__.MyPerson'


class Person:
    def __init__(self, name, surname, alias = "no alias") -> None:          # class constructor with parameters
        self.name = name                                # class properties inicialized with parameter
        self.__surname = surname                        # class properties inicialized with parameter it is private with __
        self.full_name = f"{name} {surname} ({alias})"           
        
    def get_surname(self):                              # getter propertie class
        return self.__surname
    
    def set_surname(self, surname):                     # setter propertie class
        self.__surname = surname
        
    def walk(self):                                     # function in class
        print(f"{self.full_name} is walking")
        
    def talk(self):                                     # function in class
        print(f"{self.full_name} is talking")
        
    
my_person = Person("Jorge", "Agulló")                   # = Person instance
print(my_person.name)                                   # = Jorge
print(my_person.get_surname())                          # = Agulló
print(my_person.full_name)                              # = Jorge Agulló
print(my_person.walk())                                 # = Jorge Agulló walking
my_person.set_surname("Martín")
print(my_person.get_surname())                          # = Martín


my_other_person = Person("Guido", "van Rossum", "Python Father's")  # = Person instance
print(my_other_person.full_name)                                    # = Guido van Rossum (Python Father's)
my_other_person.full_name = "Guido van Rossum (Father of Python)"
print(my_other_person.full_name)                                    # = Guido van Rossum (Father of Python)
my_other_person.talk()                                              # = Guido van Rossum (Father of Python) is talking