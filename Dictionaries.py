# DICTIONARY
# key: value pairs, UNORDERED

tel = {'jack': 1234, 'sape': 7895}
print(tel)
tel['Dannial'] = 9876
print(tel)
tel['Dannial'] = 7777
print(tel)  # Dannial's valus updated
del(tel["Dannial"])
print(tel)
print('Sachin' in tel)
print('jack' in tel)
print(sorted(tel.keys(), reverse=1))
print(sorted(tel.keys()))
print(type(tel.keys()))

d = dict([('jack', 1234), ('sape', 7895)])
print(d)

# Dict Comprehensions
d = dict([x, x**2] for x in range(10))
print(d)
print(type(d))
d = {x: x**2 for x in range(10)}
print(d)

# When keys are strings we can do following also
d = dict(sape=123, jack=7898)
print(d)
print(d.keys())
print(d.values())
# looping
d = {'Prashant': 6823869350, 'Prashant2': 8007305695}
print(d)
for key, value in d.items():
    print(key, value)


dict1 = {1: 5, 'a': 'b'}
print('-----------------')
print(dict1)
dict1.clear()  # delets all the items of the dict1
print(dict1)
del(dict1)  # deletes dict1
# print(dict1) # throws error as dict1 was deleted
