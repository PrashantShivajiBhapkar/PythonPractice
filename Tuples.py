# Tuples are immutable lists and usually contain heterogenous elements as
# opposed to lists which are mutable and generally contain homogenous elements
# Currently there are 3 SEQUENCE data types: list, tuple, range
t = 12345, 4568  # Tuple packing
print(t)
t1 = 12, 45, 'Hello!'
print(t1)
print(t.index(12345))
print(t1.index('Hello!'))
t2 = 12, 45, ('nested', 'tuple')
# Typles are IMMUTABLE
# t[o] = 4568798 #invalid
t3 = ([1, 2, 3], [4, 5, 6], [7, 8, 9])
print(t3)
print('----')
a, b, c = t3  # Tuple unpacking
print(a, b, c)

# Interesting cases of defining a tupple with 0 and 1 elements
tEmpty = ()
print(tEmpty)
tSingleton = 45
print(tSingleton)
print(type(tSingleton))
tSingleton = (45)
print(tSingleton)
print(type(tSingleton))
# tSingleton = tuple(45) #throws error
# CORRECT WAY for defining a tuple with one element
tSingleton = 45,
print(tSingleton)
print(str(type(tSingleton)) + ' Now we got it!!')  # + for string
tSingleton = (45,)
print(tSingleton)
print(str(type(tSingleton)) + ' Now we got it!!')  # + for string
print(type(tSingleton), 'Now we got it!!')

t = tuple([1, 2, 30])  # parametered a list
print(t)
print(type(t))

t = tuple((1, 2, 30))  # parametered a tuple
print(t)
print(type(t))

l = list([1, 2, 3])  # parametered a list
print(l)
print(l[0])
l = list((1, 2, 3))  # parametered a tuple
print(l)
l1 = list([[1, 2, 3]])
print(l1)

# Tuple of list is MUTABLE as list is mutable. Here we have one list in the
# tuple. And that list is mutable
t = ([[1, 2, 3]],)
print(t)
print(type(t))
t[0].append('asd')
print(t)
t = ([1, 2, 3, 4],)
print(t)
print(type(t))
t[0][1] = 999
print(t)

import numpy as np
a = np.array([[0], [1], [2]])
print(a)
print(a.shape)

import numpy as np
A = np.random.randn(4, 3)
B = np.sum(A, axis=0, keepdims=True)
print(B)
print(B.shape)
print(type(B))
C = np.sum(A, axis=0, keepdims=0)
print(C)
print(C.shape)
print(type(C))
B = np.sum(A, axis=1, keepdims=0)
print(B)
print(B.shape)
print(type(B))
B = np.sum(A, axis=1, keepdims=1)
print(B)
print(B.shape)
print(type(B))
