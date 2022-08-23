'''From the following text:
string = 'PKV-89415-PLN'
extract the code containing the first three and last three characters. Print the result to the console.
Expected result:
PKVPLN'''
string = 'PKV-89415-PLN'
firstVal = string.split('-')[0]
finalVal = string.split('-')[2]
print(f'{firstVal}{finalVal}')

#Otra solución
stringPart = string[:3] + string[-3:]
print('StringPart',stringPart)