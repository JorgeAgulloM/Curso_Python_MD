### Conditionals ###

my_condition = True

if my_condition:
    print("Condition executed")
else:
    print("The condition is not executed")
    
print("next flow")

my_condition = 5 * 2

if my_condition == 10:
    print("my_condition is 10")
else:
    print("my_condition is not 10")

print("next flow")

if my_condition > 10 and my_condition < 20:
    print("my_condition is greater than 10 or less than 20")
elif my_condition < 10:
    print("my_condition is less than 10")
elif my_condition > 50:
    print("my_condition is greater than 50")
else:
    print("my_condition is not greater than 10 or less than 20")


my_string = "my text"

if my_string == "":
    print("my_string is empty")
    
if not my_string:
    print("my_string is empty")
    
if my_string == "my text":
    print("my_string is the same than {}".format(my_string))