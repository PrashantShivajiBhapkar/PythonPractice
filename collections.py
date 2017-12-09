from collections import namedtuple
from collections import OrderedDict

color = namedtuple('Colour', ['red', 'green', 'blue'])

color1 = color(55, 25, 175)
print(color1)
print(color1.red)

# Ordered Dictionary
od = OrderedDict()
od['a'] = 1
od['b d'] = 2
od['c'] = 3
od['d'] = 4
od['e'] = 5
od['f'] = 6

print(od)

od['a'] = 11
od['b'] = 22
od['c'] = 33
od['d'] = 44
od['e'] = 55
od['f'] = 66

print(od)


l = [1,2,5,5,9,99]
print(l[-1])

odd = OrderedDict()

odd[1] = 5
print(odd)
print(odd[1])
for i in range(5):
    odd[1] += i

print(odd[1])
print(odd[1])
