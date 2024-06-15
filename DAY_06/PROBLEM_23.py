'''
Target Sum:
Given an array of integers and a target sum, find the indices of the two numbers in the
array that add up to the target sum.
You are given an array of integers and a target sum. Your task is to write a function
that identifies the indices of the two numbers in the array that, when added together, 
equal the target sum. The function should return the indices of these two numbers in the form of a list.
input :
2 7 11 15
9

output:
[0,1]
'''

a = list(map(int,input().split()))
target_sum = int(input())
a.sort()
i = 0
j = len(a)-1
ans = 0
while i<j:
    curr_sum = a[i] + a[j]
    if curr_sum==target_sum:
        print(i,j)
        i += 1
        j -=1
    elif curr_sum<target_sum:
        i = i+1
    else:
        j = j-1
'''
Output:
2 7 11 15
9
0 1
'''