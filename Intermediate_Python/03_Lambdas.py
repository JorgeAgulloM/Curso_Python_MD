### Lambdas ###

sum_to_values = lambda first_value, second_value: first_value + second_value
print(f"Result lambda: {sum_to_values(2, 4)}")              # = Result lambda: 6

sum_to_values = lambda first_value, second_value: print(f"Result lambda: {first_value + second_value}")
sum_to_values(2, 4)                                         # = Result lambda: 6

multiply_values = lambda first_value, second_value: first_value * second_value
print(f"Result lambda: {multiply_values(2, 4)}")            # = Result lambda: 8

def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value
print(f"Result lambda: {sum_three_values(5)(2, 4)}")        # = Result lambda: 11
