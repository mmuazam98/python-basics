from sympy import limit
from sympy import sin
from sympy.abc import x
print(limit((sin(x)-x)/ x**3, x, 0))