from sympy import *
import sympy as sym

num = int(input("Enter a number: "))
sqr = sqrt(num)
print(sqr.evalf(100))

a = sym.Rational(1, 2)
b = sym.Rational(1, 3)
print(a+b)

x, y = symbols('x y')
print(expand((x + y) ** 6))


print(simplify(sin(x)/cos(x)))


print(limit((sin(x)-x)/ x**3, x, 0))