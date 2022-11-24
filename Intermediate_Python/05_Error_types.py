### Error Types ###

## SyntaxError

#print "Hello people"   #Error. SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
print("Hello people")   # = Hello people


## NameError

language = "spanish"
#print(language2)       #Error. NameError: name 'language2' is not defined
print(language)         # = Spanish

# IndexError

my_list = ["Python", "Kotlin", "Java", "JavaScript"]
print(my_list[0])       # = Python
#print(my_list[4])      #Error. IndexError: list index out of range

