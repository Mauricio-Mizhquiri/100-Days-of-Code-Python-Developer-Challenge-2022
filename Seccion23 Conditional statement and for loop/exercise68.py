'''Write a program that finds all two-digit numbers divisible by 11 and indivisible by 3 (use a for loop). 
Print the result to the console as comma-separated values as shown below.

Expected result: 11,22,44,55,77,88'''
elements = []
for val in range(11,100, 11):
    if val %3 != 0:
        elements.append(str(val))

print(','.join(elements))