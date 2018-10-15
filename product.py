import itertools

my_list = list(itertools.product(range(10), repeat=4))
print(my_list)
print(len(my_list))
