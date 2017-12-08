from collections import deque  # for deque
# LISTS
print('Learning Lists')
list1 = [1, 2, 3, 6, 5]
print(list1)

# APPEND
list1.append(6)
print(list1)
list1.append(7)
#list1.append(i for i in range(5))
# list1.append(8,9,10) invalid. append takes only one argument
print(list1)
list1.append([11, 22, 33, 44, 55, 66])
print(list1)
print(list1[5:])
list1.append(2)
list1.append(2)
list1.append(2)
list1.append(2)
print(list1)

# EXTEND
list1.extend(['a', 'b', 'c'])  # PURPOSE: only ONE ITERABLE argument
print(list1)
list1.extend('z')  # non iterable also works
print(list1)

# COUNT
print(list1.count('a'))
print(list1.count(11))
print(list1.count('z'))
print(list1.count(2))

# INDEX
print(list1)
print(list1.index('z'))
print(list1.index([11, 22, 33, 44, 55, 66]))

# SORT
# list1.sort(reverse=1)  # cannot sort as the list has alpha as well as nums
list2 = [8, 9, 7, 5, 6, 8, 4, 9, 7, 2]
list2.sort(reverse=1)
print(list2)
list2.sort(reverse=0)
print(list2)
print(list1)
list1[7].sort(reverse=1)
print(list1)
list1[0:7].sort(reverse=1)
print(list1)

# REVERSE
print('------')
list1.reverse()
print(list1)
list1.reverse()
print(list1)
list1[7].reverse()
print(list1)

# REMOVE
list1.remove(2)  # removes one at a time if multiple instances
print(list1)
list1.remove(2)
print(list1)
list1.remove(list1[6])
print(list1)

# INSERT
list1.insert(2, 999)  # indexing option available
print(list1)

# POP
list1.pop(2)
print(list1)
list1.pop()  # by default pops the last element
print(list1)

# for stack implementation APPEND() and POP()

# for Queue implementation


queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
print(queue)
queue.popleft()                 # The first to arrive now leaves
print(queue)
queue.popleft()                 # The second to arrive now leaves
print(queue)                    # Remaining queue in order of arrival

# List Comprehensions
lc = list(map(lambda x: x**2, range(10)))
print(lc)
lc2 = list(x**2 for x in range(10))
print(lc2)
lc3 = [x**2 for x in range(10)]
print(lc3)
lc4 = [[x**2] for x in range(10)]
print(lc4)
lc5 = [(x**2) for x in range(10)]
print('Printing lc5----------')
print(lc5)
lcombTup = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(lcombTup)
lcombList = [[x, y] for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(lcombList)

print('--------------------')
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
print(matrix)
matrixT = [[j[i] for j in matrix] for i in range(3)]
print(matrixT)
matrixT = [[j[i] for j in matrix for i in range(3)]]  # Different
print(matrixT)
print(*matrix)
print(zip(*matrix))
print(list(zip(*matrix)))

# DEL to delete an element of the list based on index
print('-----------------------')
print(matrix)
del matrix[0]
print(matrix)
del matrix
print("DELETED!! cannot reference matrix now!")

print('--------------------')
la = [1, 2, 3]
print(la)
print(*la)


for i in '1234':
    print(type(i))

a, b = [1, 2]
print(a, b)
print(type(a))
a = [1, 2]
print(type(a))
eval("print('123')")

_, a, _, b = eval("set([i for i in range(2)])," * 4)
print(a, b)

print('abs' * 4)
s = 'asdads erwer'
se1 = set(s.split())
print(type(s.split()))


print('--------List Operators--------')
l = [1, 2, 4, 5, 6]
l += ['a', 'b', 'c']
print(l)
l = ['a', 'b', 1, 2] * 3
print(l)


for i in range(0, 2):
    print(i)


# print([i for i in range(1, 5, 2) if (1 % 2) != 0 else])
str = 'asdasdd'
print(str)
print(str.count('a'))

print(int(5.2))
print(list(zip([1, 2], [3, 4])))

import numpy as np
a = np.array((1, 2, 3))
print(np.power(a, 2))
print(type(a))

print(a[a > 1])
a[a > 1]
print(a > 1)
b = a > 1
print(b)
