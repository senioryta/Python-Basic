fruits = ["apple","grape","orange","grape","watermelon","grape"]

print(fruits)

fruits.append("pear")
# fruits[len(fruits):] = ["jackfruit"]

fruits.extend("banana")
# fruits[len(fruits):] = "banana"

fruits.insert(1,"orange")

fruits.remove("grape")
fruits.remove("orange")

fruits.pop()

# fruits.clear()
# del fruits[:]

print(fruits)
print("index character of b is",fruits.index("b"))
print("index watermelon is",fruits.index("watermelon"))

print("total of apple is",fruits.count("apple"))
print("total character of n is",fruits.count("n"))

print(fruits)

fruits.sort()

print(fruits)

fruits.reverse()

print(fruits)

a = fruits.copy() # or a = fruits[:]
a.append("jm")
print(a)
print(fruits)