'''Find the roots of the quadratic equation:
            x^2+5x+4 = 0
Print the result to the console as shown below.
Expected result: x1 = -4.0, x2 = -1.0
'''
from math import sqrt

a = 1
b = 5
c = 4

x1 = (-b - sqrt(b**2 -4*a*c))/2*a
x2 = (-b + sqrt(b**2 -4*a*c))/2*a
print(f'x1 = {x1}')
print(f'x2 = {x2}')