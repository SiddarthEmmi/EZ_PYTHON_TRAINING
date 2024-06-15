#1,3,2,20,4,6,5,1
'''
Find Peak Element
A peak element is an element that is strictly greater than its neighbors.
Given a 0-indexed integer array nums, find and return peak element. 

Input: nums = 1 3 2 20 4 6 5 1
Output: 20
'''
a = list(map(int,input().split()))
mp = -999
for i in range(1,len(a)-1):
    if a[i]>a[i-1] and a[i]>a[i+1]:
         p = a[i]
         if p>mp:
            mp = p
print(mp)
'''
1 3 2 20 4 6 5 1
20
'''