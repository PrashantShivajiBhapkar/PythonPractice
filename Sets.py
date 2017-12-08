# SETS
# Sets = unordered collection of UNIQUE/NON-DUPLICATE Elements
# Uses = membership testing and eliminating duplicate entries
# Dont use {} to create an emplty set. This creates empty dictionary!!
# Use set()

basket = {1, 2, 6, 'hello'}
print(basket)
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)  # prints only unique values as set has only unique values

# membership testing
print('apple' in basket)
print('zebra' in basket)

a = set('abracadabra')  # set() accepts an iterable
print(a)
b = set('alacazam')
print(b)
print('--SET OPERATIONS--')
print('a - b: ', a - b)
print('b - a: ', b - a)
print('a UNION b: ', a | b)
print('a INTERSECTION b ', a & b)
print('Symmetric difference(letters in a or b but not both) ', a ^ b)

a = {1, 2, 30}
b = {4, 5, 6}
a.union(b)  # a doesn't get changed
print(a)  # a doesn't get changed
# print(a |= b)

asd = {i for i in range(5)}
print(asd)
print(type(asd))

qwe = {i: i**2 for i in range(10)}
print(qwe)
print(type(qwe))
