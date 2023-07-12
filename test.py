import os
print("早安 ",end=" 啾咪")
mylist = [97,77.7,89.3,0,100]
print(sum(mylist))
print((mylist))
mydict = dict([[1,"123"],[2,"456"]])
print(mydict)
print(mydict.pop(1))
print(mydict)
print(sum([i if type(i) == type(1.1) else 0 for i in mylist]))
