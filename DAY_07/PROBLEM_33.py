'''
You are given an array A of N Integers. The array A can be divided into two parts:
the first part consists of the first 'l' elements of A (where ranges from 1 to N),
and the second part consists of the last (N-1) elements of A
Your task is to find and return a new array named result of the same size as A,
where each element of result[1] represents the absolute difference between the sum
of the elements in the first part of A and the sum of the elements in the second part of A

Note: For i= N,N-i=0.So, consider the sum of last N-i integers as O in this case

Input Specifications:
Input1: An integer value representing the size of the array A.
Input2: An integer array A.

Output Specification:
Return a new integer array named result of the same size as A, where each element of 
result[i) represents the absolute difference between the sum of the elements in the 
first part A and the sum of the elements in the second part of A

Sample Input:
5
12345

Sample Output:
[13, 9, 3, 5, 15]
'''
a = list(map(int,input().split()))
#sum
tot_sum = 0
left_sum = 0
right_sum = 0
curr_sum = 0
ans = []
for i in a:
    tot_sum += i
    
#Left sum
for i in a:
    left_sum += i
    right_sum = tot_sum - left_sum
    curr_sum = abs(right_sum-left_sum)
    ans.append(curr_sum)
    
print(ans)
'''
Output:
1 2 3 4 5
[13, 9, 3, 5, 15]
'''