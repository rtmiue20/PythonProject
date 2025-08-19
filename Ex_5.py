"""5. Write a Python program to get a single string from two given strings, separated by a space and
swap the first two characters of each string.
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz"""
s1 =str(input('Enter a string 1: '))
s2 =str(input('Enter a string 2: '))
if len(s1)  >= 2 and len(s2) >= 2:
    new_s1 = s2[:2] + s1[2:]
    new_s2 = s1[:2] + s2[2:]
    print( new_s1 +" "+ new_s2)
else :
    result  = s1 + " "+ s2
    print(result)

