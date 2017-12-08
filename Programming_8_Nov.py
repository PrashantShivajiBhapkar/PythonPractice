str = {"server": "mpilgrim",
       "database": "master",
       "uid": "sa",
       "pwd": "secret"
       }
print(str)
# x
# x = 1  # cannot reference a variable. variable is defined while assignment.
# print(x)
print(range.__doc__)
for i in range(0, 10, 2):
    print(i)

# String Formatting
print('_______String Formatting_______')
user = 'Prashant'
pwd = 'secret'
print('%s is pwd for the user %s' % (pwd, user))
print('%s %s' % (user, pwd))
name = 'Prashant Bhapkar'
print('%s %s %s' % (user, name, pwd))
# Only TUPLES are used while formatting
# print('%s %s' % [user, pwd]) #throws error
# except when there
# is only one thing to be formatted
print('%s' % [user])
print('%s' % user)
print('%s' % (user))
count = 10
print('%s' % (count,))
# print('count is ' + count) # throws error as count is not string
print('count is ', count)

print('______formatting Numbers_____')
print('Today\'s stock price is %f' % 50.458)
print('Stock price : %.2f' % 50.45698)
print('Stock price : %+.2f' % 50.7897)
# print('Stock price : %-.2f' % -50.7897)
print('Stock price : %+.2f' % -50.7897)  # %+.f takes care of =ve as well as -ve


print(8 / 2)
print(8 // 2)
print(8 / 5)
print(8 // 5)  # // only numerator

print('-------------Joining AND Splitting Strings------------')
# Split STRING into LISTS and join LISTS into STRINGS
print('-'.join(['%s' % i for i in range(10)]))
print(' AND '.join([i for i in 'qwerty']))
d = {'a': 1, 'b': 2}
print(d)
print(' AND '.join(['%s:%s' % (k, v) for k, v in d.items()]))
print(type(' AND '.join(['%s:%s' % (k, v) for k, v in d.items()])))
# JOIN WORKS ONLY WITH STRINGS. FOLL THROWS ERROR
# print('--'.join([i for i in range(10)]))
print("Prashant Shivaji Bhapkar".split())
name, middle_name, surname = "Prashant Shivaji Bhapkar".split()
print(name + middle_name + surname)
print('MY NAME IS ' + ' '.join([name, middle_name, surname]))
# SPLIT SPLITS THE STRING AND RETURNS A LIST OF INDIVIDUAL STRING VALUES
print(type("qwe qwe ert".split()))
print('-'.join('asd wer qwwe rte'.split(' ', 1)))


a = {1, 2, 3, 5, 5, 5, 50}
print(a)
a = {1: 5}
print(a)
print(type(a))
