group1 = (1,2,10,88)

print(group1)

# print("total & position index of number 10 is",group1.count(10),group1.index(10))

group2 = (0.96,2.93,100.9,-33)

# all = group1 + group2
all = (group1,group2)

print(all)

import sys,timeit


list_date = [1,2,102,"hello, world!","jm","software enginner",3.12]
tuple_date = (1,2,102,"hello, world!","jm","software enginner",3.12)

print("total size of list is", sys.getsizeof(list_date))
print("total size of tuple is", sys.getsizeof(tuple_date))


list_proc = timeit.timeit(stmt="[1,2,102,'"'hello, world!'"','"'jm'"','"'software enginner'"',3.12]",number=1000000)
tuple_proc = timeit.timeit(stmt="(1,2,102,'"'hello, world!'"','"'jm'"','"'software enginner'"',3.12)",number=1000000)

print("date list proccess", list_proc)
print("date tuple proccess", tuple_proc)