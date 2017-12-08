# Looping Techniques
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

questions = ['name', 'age']
answers = ['Prashant', 26]
for q, a in zip(questions, answers):
    print("What's your {0}: It's {1}".format(q, a))

# Looping in reverse
for i in reversed(range(10)):  # values [0:9]
    print(i)

for i in range(10, 0, -1):  # values [10:1]
    print(i)

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(list(basket))
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(set(basket)):
    print(i)

print((1, 2) > (4, 5))  # element by element comparison
print((1, 2, 3) == (1.0, 2.0, 3.0))
