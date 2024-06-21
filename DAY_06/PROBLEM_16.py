'''
Vowel Repetition Problem:
Given a string s print the most frequent vowel that is present in the string as a output.

Input Format:
A single line containing the string s.

The input will be read from the STDIN by the candidate

Output Format:

Print a single character which represents the most frequent vowel in the given string.

Example:

Input:
helloworld

Output:
o
'''
#Vowel count

s = input()
d = {}
y = "aeiou"
mx = -999
ans = 0
for i in s:
    if i in y:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
        if d[i]>mx:
            mx = d[i]
            ans = i
print(d)
print(ans)
'''
OUTPUT:
helloworld
{'e': 1, 'o': 2}
o
'''
