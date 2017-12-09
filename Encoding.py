import chardet

st = 'My name is Prashant'
a = st.encode('UTF-8')
print(a)
print(a.decode('UTF-8'))

a = st.encode('UTF-16')
print(a)
print(a.decode('UTF-16'))
print(chardet.detect('Donald Trump - Wikipedia'.encode('utf-8')))
print(st.encode('UTF-8'))
print(st.encode('UTF-16'))
print(st.encode('UTF-32'))

s = (st.encode('UTF-8')).decode('utf-8')
print(s)

# print(chardet.deetect('b\'asdads'))

print(chardet.detect('Donald Trump - Wikipedia'.encode('utf-16')))


a = b'Donald Trump - Wikipedia'
print(a)
print(a.decode('utf-8'))
