# count é um iterador sem fim (itertools)
from itertools import count

c1 = count(8,8)
r1 = range(8,100,8) 

print('c1', hasattr(c1,'__inter__'))
print('c1', hasattr(c1,'__next__'))
print('r1', hasattr(r1,'__inter__'))
print('r1', hasattr(r1,'__next__'))

for i in c1:
    if i>= 100:
        break
    print(i)
print()
print('range')
for i in r1:
    if i > 100:
        break
    print(i)