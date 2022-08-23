'''From the following text:

string = '1 0 0 1 0 1'

remove spaces using slicing. Then convert the result to decimal notation and print to the console as shown below.

Expected result: Number found: 37'''
string = '1 0 0 1 0 1'
result = int(string[-1])*2**0+int(string[-3])*2**1+int(string[-5])*2**2+int(string[-7])*2**3+int(string[-9])*2**4+int(string[-11])*2**5
print(f'Number found: {result}')

#otra solucionn
binary = string[::2]
number = int(binary,2)
print('Number found:',number)