'''
Reverse the order of string:
You are given a string cntaining words seperated by spaces. Your task is to write a 
function or program that reverse the order of wordes in the string.

Sample input:
Hello World

Sample Output:
World Hello
'''
s = input().split()
l = list(s)

i = 0
j = len(l)-1

while i<=j:
    temp = l[i]
    l[i]=l[j]
    l[j]=temp
    i += 1
    j -= 1
    
print(' '.join(l))
'''
Output:
Hello World
World Hello
'''