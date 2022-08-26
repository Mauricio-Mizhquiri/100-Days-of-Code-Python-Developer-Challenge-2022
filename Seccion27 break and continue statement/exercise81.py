'''Write a program that checks if the given number is a prime number (use the break statement):

number = 13

Print one of the following to the console depends on the result:

13 - prime number
13 - not a prime number
Expected result:

13 - prime number'''
number = 13
estado = True
for val in range(2, number):
    if number%val == 0:
        estado = False
        break;
if estado:
    print('13 - prime number')

