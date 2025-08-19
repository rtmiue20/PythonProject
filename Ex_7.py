"""7. Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given
string. If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the
resulting string.
Sample String : 'The lyrics is not that poor!'
'The lyrics is poor!'
Expected Result : 'The lyrics is good!'
'The lyrics is poor!'
"""
s = "The lyrics is not that poor!"
words = s.split()
pos_not = -1
pos_poor = -1
for i in range(len(words)):
    if words[i] == "not" :
        pos_not = i
    if "poor" in words[i]:
        pos_poor = i
#neu poor truoc not
if pos_poor != -1 and pos_poor != -1 and pos_poor > pos_not:
    new_word = words[:pos_not] + ["good"] + words[pos_poor +1:]
    result = " ".join(new_word)
else:
    result = s
print(result)




