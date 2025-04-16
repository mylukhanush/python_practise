
 # set data type
s={0,1,2,3,1,2,3,4,2,3,4,23}
print(s)
s.add(6)
# print(s)
s.update(["ps"])
print(s)
s.remove(2)
print(s)

# dictionary type
a={1:"Bunny",2:"harsh"}
print(a)
del(a[1])
print(a)
for i,j in a.items():
    print(i,j)
for key in a.keys():
    print(key)
for value in a.values():
    print(values)

# Tuples
# syntax to create tuple "()"
# tuple properties
# mutable ,immutable
# indexing
k="Achieve"
print(k)   #THIS LOGIC DEFINES.......
print(type(k))
# indexing
# index values always starts from zero/
# 0    1    2    3    4    5    6      positive index
# A    c    h    i    e    v    e
# -7   -6   -5   -4   -3   -2   -1     negative index
print(k[3])
print(k*3)
print(k[3]*3)
print(len(k))
# SLICING
print(k[0:3])
print(k[3:])
print(k[:4])
print(k[-3:-1:])
print(k[0:6:2])
