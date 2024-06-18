'''
Boring arrays:
You are given an array A of size N. In one operation you can select any two elements from it,
add their absolute difference in your score.
Your task is to find and return an integer value, representing the maximum score.

Note: Assume 1 based indexing

The elements on which operation has been performed cannot be selected again.

Input Specification:
Input1: An integer value N, representing the size of array A
Input2: An integer array A

Output Specification:
Return an integer value, representing the maximum score.

sample input:
4
1 2 3 4
sample output:
4
'''
n = int(input())
a = list(map(int,input().split()))
a.sort()
left = 0
right = len(a)-1
s = 0
while left<=right:
    d = abs(a[right]-a[left])
    s += d
    left += 1
    right -= 1
print(s)
'''
Output:
4
1 2 3 4
4
'''
