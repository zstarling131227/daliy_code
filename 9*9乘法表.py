# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('%d*%d=%d ' % (j, i, i * j), end="")
#     print("")

i = 0
while i < 9:
    i += 1
    j = 0
    while j < i:
        j += 1
        # print('%d*%d=%2d ' % (j, i, i * j), end="")
        # print('%d*%d=%2d' % (j, i, i * j), end=" ")
        print('%d*%d=%d' % (j, i, i * j), end="\t")
    print("")


