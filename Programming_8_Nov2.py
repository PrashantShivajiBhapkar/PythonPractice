# Powerful inbuilt functions
# type(), str() and dir()

print(type((1, 2, 5, 6)))
print(type(type(1)))  # just a bit sexy!! :)

# String coercion
# str() function coerces data into a string
# EVERY Datatype can be coerced into string
print(type(str(1)))  # int
print(str((1, 2, 5, 6)))  # tuple, '(' too is not spared
print(str((4, 5, 6))[0])  # '(' too is not spared and is the first char of string
print(type(str((1, 2, 5, 6))))
print(str([1, 5, 4, 8, 9]))  # list
print(str([1, 5, 7, 9, 9])[0])  # '[' too is not spared and is the first char of string
print(str([1, 5, 7, 9, 9])[2])  # even , is not spared
print(type(str([1, 5, 4, 8, 9])))
print(str(None))
print(str(None)[2])
print(str(True))

# dir()
# dir returns a list of the attributes and methods of any object: modules,
# functions, strings, lists, dictionaries... pretty much anything.
print('---------dir()---------')
li = []
print(dir(li))
di = {}
print(dir(di))

# callable()
# the callable function takes any object and returns True if the object
# can be called, or False otherwise. Callable
# objects include functions, class methods, even classes themselves
import string
print(string.punctuation)
print(type(string.punctuation))
print(callable(string.punctuation))
# print(callable(string.join)) this should be true

# gertattr()
li = []
print(li.pop)
print(getattr(li, 'pop'))
# This also returns a reference to the pop method, but this time,
# the method name is specified as a string argument to the getattr
# function. getattr is an incredibly useful built-in function that
# returns any attribute of any object. In this case, the object is
# a list, and the attribute is the pop method.
print(getattr(li, 'append')('Prashant'))
print(li)

# DIspatccher with gertattr
s = 'append'
l = []
print(getattr(l, "%s" % s))
getattr(l, "%s" % (s))('Prashant')
print(l)
getattr(l, "randomemethodname", l.append)('Bhapkar')
print(l)

# if else inline trick
a = 2
b = 3
print(1 and a or b)
print(0 and a or b)

# when this fails
a = 0  # that is False
b = 'asd'
print(1 and a or b)  # this fails
print(0 and a or b)  # this works fine though

# Lambda Functions
# fun = lambda x: x*2
# print(fun(4))

print((lambda x: x**2)(5))

l = []
print(dir(l))
print(type(dir(l)))
