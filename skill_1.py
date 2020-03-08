from __future__ import division

"""
枚举（enumerate）
"""
i = 0
iterable = [1, 2, 3, 4, 5]
for item in iterable:
    print(i, item)
    i += 1

for i, item in enumerate(iterable):
    print(i, item)

print(list(enumerate(iterable)))
print(list(enumerate(iterable, 1)))

"""

"""
my_list = {i for i in range(10)}
my_dict = {i: i * i for i in range(10)}
my_set = {i * 15 for i in range(10)}
print(my_list, type(my_list))
print(my_dict, type(my_dict))
print(my_set, type(my_set))

result = 1 / 2
print(result)

import ast

expr = "[1,2,3]"
my_list1 = ast.literal_eval(expr)
my_list2 = eval(expr)
print(my_list1, my_list2)

a = [1, 2, 3, 4]
print(a[::-1])
a.reverse()  # 无返回值，但是会直接改变a的值
print(a)

'[on_true] if [expression] else [on_false]'
x, y = 50, 25
small = x if x < y else y
print(small)



import copy
existing_list=9090
new_list=copy.copy(existing_list)
print(new_list)

existing_list_of_dict={2:3,4:5}
new_list_of_dict=copy.deepcopy(existing_list_of_dict)
