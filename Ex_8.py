"""8. Write a Python function that takes a list of words and return the longest word and the length
of the longest one.
Sample Output:
Longest word: Exercises
Length of the longest word: 9"""
n = int(input("Nhap so cau ban muon: "))
sen = []
for i in range(n):
    sen.append(input())
max_sen = sen[0]
for s in sen :
    if len(s) > len(max_sen) :
        max_sen = s
print(f"Longest word: {max_sen}")
print(f"Length of the longest word: {len(max_sen)}")



