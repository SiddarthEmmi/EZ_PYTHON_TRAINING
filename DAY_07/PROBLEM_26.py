'''
Missing Alphabets:
Pangram is a sentence containing every letter in the English alphabet.
Given a string, find all characters that are missing from the string
i.e., the characters that can make the string a pangram. We need to 
print output in alphabetic order.

For example:

Input: welcome to geeksforgeeks

Output: abdhijnpquvxyz
'''
s = input()
org = "abcdefghijklmnopqrstuvwxyz"
ans = ""
for i in org:
    if i not in s:
        ans = ans + i
print(ans)
'''
Output:
welcome to geeksforgeeks
abdhijnpquvxyz
'''
