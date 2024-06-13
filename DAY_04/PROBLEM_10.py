'''
SPACE COUNTER:
You have been given the task to making the content on a social media platform
more user friendly. Your task is to find and return an integer value representing
the count of number of spaces in a given string.

INPUT :
    A String S
OUTPUT :
    Return integer value representing the count of the number of spaces in a given string.
    
EXAMPLE:
    I/P : Hello World Hey
    O/P : 2
'''
# =========WITHOUT SPLIT============
s = input()
c = 0
for i in s:
    if i == " ":
        c = c+1
print(c)
# ==========WITH SPLIT==============
h = s.split()

print(len(h)-1)
# ==================================
# ============OUTPUT================
'''
Hello World Hey
2
'''