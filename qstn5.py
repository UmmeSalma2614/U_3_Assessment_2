# Write a Python program to count the number of characters (character frequency) in a string

str1= input('Enter the string:')
freq = {} 
for i in str1: 
     if i in freq: 
        freq[i] += 1
     else: 
        freq[i] = 1
print ("Count of all characters in string is :\n"),
str(freq))