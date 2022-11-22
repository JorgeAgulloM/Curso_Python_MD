### List Comprehension ###

my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]
print(my_original_list)                         # = [0, 1, 2, 3, 4, 5, 6, 7]

my_range_list = range(8)
print(list(my_range_list))                      # = [0, 1, 2, 3, 4, 5, 6, 7]

my_comp_list = [i for i in range(8)]
print(my_comp_list)                             # = [0, 1, 2, 3, 4, 5, 6, 7]

my_comp_list = [i + 1 for i in range(8)]
print(my_comp_list)                             # = [1, 2, 3, 4, 5, 6, 7, 8]

my_comp_list = [i * 2 for i in range(8)]
print(my_comp_list)                             # = [0, 2, 4, 6, 8, 10, 12, 14]

my_comp_list = [i * i for i in range(8)]
print(my_comp_list)                             # = [0, 1, 4, 9, 16, 25, 36, 49]

my_comp_list = [i for i in my_original_list]
print(my_comp_list)                             # = [0, 1, 2, 3, 4, 5, 6, 7]


def sum_five(number) -> int:
    return number + 5

my_comp_list = [sum_five(i) for i in my_original_list]
print(my_comp_list)                             # = [5, 6, 7, 8, 9, 10, 11, 12]