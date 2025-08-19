"""3. Write a Python program to get a string made of the first 2 and last 2 characters of a given
string. If the string length is less than 2, return the empty string instead.
Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String"""
s = str(input('Enter a string: '))
print(s)
if len(s) < 2 :
    print ("Empty String")
else :
    print(s[:2] + s[-2:])