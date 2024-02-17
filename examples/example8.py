func = lambda x: x**x
print(func(3))
##
##
my_list = [1, 3, 4, 6, 10, 11, 15, 12, 14]
new_list = list(filter(lambda x: (x % 2 == 0), my_list))
print(new_list, id(new_list))
##
##
current_list = [1, 3, 4, 6, 10, 11, 15, 12, 14]
out_list = list(map(lambda x: x * 2, current_list))
print(out_list, id(out_list))
##
##
from functools import reduce

current_list = [5, 15, 20, 30, 50, 55, 75, 60, 70]
summa = reduce((lambda x, y: x + y), current_list)
print(summa)

print(sum(current_list))
##
##
tables = [lambda x = x: x*10 for x in range(1, 11)]
for table in tables:
    print(table())
##
##
max_number = lambda a, b: a if a > b else b
print(max_number(-7, -5))
##
##
current_list = [[10,6,9],[0, -14, -16, -80],[8, 12, 30, 44]]
sorted_list = lambda x: (sorted(i) for i in x)
second_largest = lambda x, func: [y[len(y)-2] for y in func(x)]
result = second_largest(current_list, sorted_list)
print(result)
##
##
funk = lambda x, b ,fu= lambda b: b**2: print(x,fu(b))
funk(9,9) # 9 81