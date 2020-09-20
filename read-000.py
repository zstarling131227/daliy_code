import pandas as pd
import csv

data1 = pd.read_excel("/home/tarena/练习6.xlsx")
print(data1.head())
list1 = data1.x2
print(list1[:5])
# for i in range(len(list1) - 2):
#     # if list1[i] + list1[i + 1] + list1[i + 2] == 0:
#     if list1[i] > 3 and list1[i + 1] > 3 and list1[i + 2] > 3:
#         index = ["索引", str(i), str(i + 1), str(i + 2),
#                  "值", str(list1[i]), str(list1[i + 1]), str(list1[i + 2]), "\n"]
#         # print(index)
#         str1 = "--".join(index)
#         filename = "data1.txt"
#         with open(filename, 'a') as f:
#             f.write(str1)

filename = "data6.csv"
with open(filename, 'a') as f:
    # 字段名
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(len(list1) - 2):
        if list1[i] + list1[i + 1] + list1[i + 2] == 0:
            # if list1[i] > 3 and list1[i + 1] > 3 and list1[i + 2] > 3:
            # index = ["索引", str(i), str(i + 1), str(i + 2),
            #          "值", str(list1[i]), str(list1[i + 1]), str(list1[i + 2]), "\n"]
            for j in range(2):
                index = [str(data1.num[i + j]), str(data1.date[i + j]), str(data1.x1[i + j]), str(data1.x2[i + j]), "\n"]
                # print(index)
                str1 = "--".join(index)
                f.write(str1)

