'''
Sub array with max sum
You are given a list of integers, and your task is to find the subarray with the maximum sum.
Write a function or method to solve this problem efficiently and return the maximum sum.

Input:
n: the no of elements in the array

nums (List of integers): A list of integers (1 <= len(nums) <= 10^5)

Sample input:
8
-1 2 3 10 -4 7 2 -5

Sample output:

20

Explanation:

The max subarry sum is 20. The subarray is [2,3,10,-4,7,2]
'''
#3 4 6 -13 9 8 2
a = list(map(int,input().split()))
c_sum = 0
mx_sum = 0
for i in a:
    c_sum += i
    
    if c_sum<0:
        c_sum=0
        
    if c_sum>mx_sum:
        mx_sum = c_sum
        
print(mx_sum)
'''
OUTPUT:
-1 2 3 10 -4 7 2 -5
20
'''