from collections import namedtuple

color = namedtuple('Colour', ['red', 'green', 'blue'])

color1 = color(55, 25, 175)
print(color1)
print(color1.red)
