import sys
print("\n".join(sys.path))
#    """ displays all the paths from where PYTHON tries to import any library
#    we specify"""
# interestingly sys module is not searched in any of these paths because
# it is a built-in module that python has
# Built-in modules behave just like regular modules,
# but their Python source code is not available,
# because they are not written in Python! (The sys module is written in C.)

l = [1, 2, 3, 55, 6, 'asd']
print(1 in l, ' - ',  'asd' in l)
print("" == False)
print([] == False)
print(1 and 0)
print(1 or 0)
