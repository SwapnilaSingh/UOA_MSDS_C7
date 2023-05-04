n = int(input())
mylist = []
i = 0
j = 1
for l in range(n):
    mylist.append(i)
    k = i + j
    i = j
    j = k
for i in range(len(mylist)):
    print(mylist[i])
