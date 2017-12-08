d = {1: 2}
print(d)
print(repr(d))


str1 = 'asd'
str2 = 'asd'
print(str1 == str2)
print(str1 is str2)

str1 = 'asd'
str2 = str1
print(str1 == str2)
print(str1 is str2)

str3 = 'ASDER'
fun = str3.lower
print(str3)
print(fun())
# print(open.__doc__)

f = open("F:/mp3/02 - rehna tu [songslover.org].mp3", 'rb')
print(print(f.name))
print(f.read(128))
f.seek(-128, 2)
print(f.tell())
print(f.read())

# REGULAR EXPRESSIONS
# Split the US phone number into 4 groups: xxx-xxx-xxx-xxxx
# 800-555-1212
# 800 555 1212
# 800.555.1212
# (800) 555-1212
# 1-800-555-1212
# 800-555-1212-1234
# 800-555-1212x1234
# 800-555-1212 ext. 1234
# work 1-(800) 555.1212 #1234

import re

phonePattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})$')
print(phonePattern.search('682-386-9350').groups())
# foll can't be parsed corrrectly
# print(phonePattern.search('800-555-1212-1234').groups())
phonePattern = re.compile(r'(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
print(phonePattern.search('work 1-(800) 555.1212 #1234').groups())
# phonePattern = re.compile(r'(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')


import numpy as np
print(np.exp(1))

m = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[9, 8, 7], [6, 5, 4], [98, 78, 87]]])
print(m)
print(type(m.shape))
print(m.shape)
print(np.sum(m))

image = np.array([[[0.67826139,  0.29380381],
                   [0.90714982,  0.52835647],
                   [0.4215251,  0.45017551]],

                  [[0.92814219,  0.96677647],
                   [0.85304703,  0.52351845],
                   [0.19981397,  0.27417313]],

                  [[0.60659855,  0.00533165],
                   [0.10820313,  0.49978937],
                   [0.34144279,  0.94630077]]])

print(image)
print('-------')
print(image[0])
print(2 ** 3)
print(np.sum(image))

a = np.array([[1, 2, 3], [4, 5, 6], [4, 5, 6], [7, 8, 9]])
print(a.shape)
b = np.array([[[1, 2, 3], [4, 5, 6], [8, 7, 9]], [[7, 8, 9], [8, 7, 9], [77, 88, 99]]])
print(b)
print(b.shape)
print(b.reshape(b.shape[0], -1))
print(b.reshape(b.shape[0], -1).shape)
print(b.reshape(b.shape[0], -1).T)
print(b.reshape(b.shape[0], -1).T.shape)

a = np.array([[1.], [2.]])
print(a)
print(a.shape)

b = np.array([[1, 0, 1]])
print(b.shape)
