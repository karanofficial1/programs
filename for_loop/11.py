# Write a Python program that loops through a list containing both strings and integers and collects only the
# elements that are palindromes (read the same forwards and backwards)

input  = ['apple', 'racecar', 'carac', 'mam', 'orange', 121, 331]
palindrome = []
for i in input:
    i = str(i)
    if i == i[::-1]:
        palindrome.append(i)
            
print(palindrome)