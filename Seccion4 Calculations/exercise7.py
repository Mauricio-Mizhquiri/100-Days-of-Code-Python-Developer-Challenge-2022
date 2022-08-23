'''The geometric sequence is given with the following formula: a_n = 8*2^(n-1)

Calculate the sum of the first six elements of this sequence. Print the result to the console as shown below.

Expected result: The sum of the first 6 elements of the sequence is: 504.0
'''
a1 = 8
r = 2
n = 6
s_6 = a1*(1-r**n)/(1-r)
print(f'The sum of the first 6 elements of the sequence is: {s_6}')
