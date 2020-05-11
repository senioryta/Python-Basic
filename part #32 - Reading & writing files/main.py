"""
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
"""

htmlfile = open('index.html','w')

htmlfile.write("<!DOCTYPE html>\n")
htmlfile.write("<html>\n")
htmlfile.write("<head>\n")
htmlfile.write("\t<title>python r&w</title>\n")
htmlfile.write("</head>\n")
htmlfile.write("<body>\n")
htmlfile.write("\t<h3>Hello, World</h3>\n")
htmlfile.write("</body>\n")
htmlfile.write("</html>")

htmlfile.close()

htmlread = open('index.html','r')

print(htmlread.read())

htmlread.close()