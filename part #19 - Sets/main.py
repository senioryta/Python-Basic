friends = {"joao","fransisco","ronaldo","joao","joao","fransisco"}

print(friends)

friends.add("tomas")

print(friends)

# fruits = set("apple")

fruits = set()

fruits.add("apple")

print(fruits)

fruits.add("orange")
fruits.add("grape")
fruits.add("apple")

print(fruits)

fruits.remove("orange")

print(fruits)

print(30*'+')

group1 = {1,3,5,7,9}
group2 = {2,4,6,8,10}
group3 = {2,3,5,7}

print(group1.union(group2))
print(group1.intersection(group3))