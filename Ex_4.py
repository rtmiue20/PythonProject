"""4. Write a Python program to get a string from a given string where all occurrences of its first
char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'
"""
s = str(input('Enter a string: '))
first_char = s[0]
print(first_char + s[1:].replace(first_char, '$'))

