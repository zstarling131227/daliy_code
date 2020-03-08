"""
写一个验证掷骰子概率的程序，同时投掷2颗6面骰子n次，计算其和得到各数字的概率。
"""
import numpy

n, i = 10, 0
list1 = []
dict1 = {}
while i < n:
    x, y = numpy.random.uniform(1, 7, 2)
    x, y = int(x), int(y)
    list1.append(x + y)
    i += 1

print(list1)
for r in list1:
    dict1[r] = list1.count(r) / len(list1)
print(dict1)

"""
编写程序解决以下问题：长度为N的数组，随机放入值为1-50中间的任意整数，请编写程序找出其中的偶数数字，并按照该数字在数组中出现次数从多到少排序输出。
"""
n = 20
list2 = numpy.random.randint(51, size=n)
print(list2, type(list2))
list2 = list(list2)
# x = numpy.random.randint(1, 51)
# y = numpy.random.randint(len(list2))
# list2 = numpy.insert(list2, y, x)
print(type(list2))
dict1 = {}
list3 = []
for i in list2:
    if i % 2 == 0:
        dict1[i] = list2.count(i)
print(dict1, type(dict1))
min_values = dict1[i]
for key, values in dict1.items():
    if min_values > values:
        min_values = values
        temp=min_values
        values=temp
        list3.append(min_values)
