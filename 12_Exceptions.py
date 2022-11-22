### Exceptions ###

number_one = 5
number_two = 1

print(number_one + number_two)          # = 6


number_two = "1"
#print(number_one + number_two)         # = exception


try:
    print(f"Se ha sumado:{number_one + number_two}")
except:     # Only executed if there is a error
    print("error!")
    
    
try:
    print(f"Se ha sumado:{number_one + number_two}")
except:     # Only executed if there is a error
    print("error!")
else:       # Only executed if there is no error
    print("continue")
    
    
try:
    print(f"Se ha sumado:{number_one + number_two}")
except:     # Only executed if there is a error
    print("error!")
else:       # Only executed if there is no error
    print("continue")
finally:    # alwais executed
    print("final")
    

# Type exceptions capture
try:
    print(f"Se ha sumado:{number_one + number_two}")
except TypeError:      # Only executed if there is a TypeError error
    print("TypeError!")
except ValueError:     # Only executed if there is a ValueError error
    print("ValueError!")
    

# Adde exception info
try:
    print(f"Se ha sumado:{number_one + number_two}")
except TypeError as e:      # Only executed if there is a TypeError error
    print(f"TypeError! {e}")


# Info exceptions capture
try:
    print(f"Se ha sumado:{number_one + number_two}")
except ValueError as e:     # Only executed if there is a ValueError error
    print(f"ValueError! {e}")
except Exception as e:      # Executed in case the above exceptions do not catch the e
    print(f"Exception! {e}")