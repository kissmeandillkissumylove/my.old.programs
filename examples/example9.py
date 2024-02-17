import copy
some_list = [1, [2], 3]
print(some_list[1] is copy.copy(some_list)[1])
print(some_list[1] is copy.deepcopy(some_list)[1])