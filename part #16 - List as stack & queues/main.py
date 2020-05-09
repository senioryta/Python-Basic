"""

print("list as stack")

numbers = [1,2,3,4]

print(numbers)

numbers.append(5)

print(numbers)

numbers.append(6)
numbers.append(7)

print(numbers)

numbers.pop()

print(numbers)

numbers.pop()

print(numbers)

numbers.pop()

print(numbers)

numbers.pop()
numbers.pop()

print(numbers)

print(30*"=","\n")

"""

print("list as queue")

from collections import deque

numbers = deque([1,2,3,4])

print(numbers)

numbers.append(5)

print(numbers)

numbers.append(6)

print(numbers)

numbers.popleft()

print(numbers)

numbers.popleft()

print(numbers)

numbers.popleft()
numbers.popleft()

print(numbers)