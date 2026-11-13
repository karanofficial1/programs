"""Build a program that analyses a paragraph entered by the user.
REQUIREMENTS
• Clean the input using strip() and convert it to lowercase for analysis.
• Display the total number of words and the total number of vowels.
• Find and display the longest word and the most frequently repeated word.
• Display the paragraph in title case.
• Check whether the entire sentence is a palindrome using slicing [::-1], ignoring spaces."""

sen = input("Enter your sentence: ").lower()
sentence = sen.strip()
word = 1    # Every sentence has single word
vowels = 0
title_case = sentence.title()  # convert to title case
without_space = sentence.replace(" ", "")  # remove all spaces
if without_space == without_space[::-1]:   #check for palindrome.
    print("Palindrome")
else:
    print("Not Palindrome.")
for i in sentence:
    if i == " ":
        word +=1
    if i in 'aeiou':
        vowels += 1

print('Number of Word: ', word)
print('Number of vowels: ', vowels)
print("Sentence in title case: ", title_case)


words_split = sentence.split(" ")
count = 0
count_word = ""
d = []
for i in words_split:
   
    if len(i) > count:
        count = len(i)
        count_word = i
#     elif len(i) == count:
#         d.append(i)
print(count_word)







# printing most repeated word
c={}
for i in words_split:
    if i in c:
        c[i] +=1
    else:
        c[i] = 1

largest = 0
largest_word= ""
for key, value in c.items():
    if largest < value:
        largest_word = key
        largest = value  

print(largest_word)
