'''Using the slicing, reverse the order of the characters in the following text:
text = '100 days of code'

Print the result to the console as shown below.

Expected result:

edoc fo syad 001'''
text = '100 days of code'
reversed_text = text[::-1]
print(reversed_text)



#other solution
reversed_string = ''.join(reversed(text))
print(reversed_string)