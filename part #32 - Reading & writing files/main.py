file = open('jm.txt','w')

file.write("hello, world!")
file.write("\nlearn how to reading & writing in python")

file.close()

file2 = open('jm.txt','r')

# print(file2.read(8))
print(file2.readline())

file2.close()

file3 = open('jm.txt','a')

file3.write("\nnew line!")

file3.close()