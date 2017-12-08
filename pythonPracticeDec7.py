from itertools import product, permutations, combinations
from collections import Counter
a = [1, 2]
b = [3, 4]
print(*product(a, b))

print(*combinations('12345', 2))
print(list(combinations('12345', 2)))
print(*list(combinations('12345', 2)))
print(list(combinations('12345', 2))[0])
a = 'HACK'

for i in range(1, 2 + 1):
    for j in combinations(sorted(a), i):
        print(''.join(j))

p = (1, 2)
print(p)
print(''.join(str(i) for i in p))
print(''.join(str(j) for i in range(1, 3) for j in combinations(sorted(a), 2)))

print(''.join(j) for i in range(1, 2 + 1) for j in combinations(sorted(a), i))

aq = '1 2 3 3 6 6'
print(aq)
print(''.join(str(a) for a in aq))
print(Counter(aq).keys())
print(Counter(aq).values())
print(Counter(aq).items())


shoes = list(map(int, aq.split()))
print(Counter(shoes))

print(''.join(aq))
