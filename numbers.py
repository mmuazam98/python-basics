x=7/3
y=7//3
print('x is {}'.format(x))
print('y is {}'.format(y))

print(type(x))
print(type(y))

from decimal import *

a = Decimal('.1')
b = Decimal('.4')

c = a + a + a - b

print(c)
