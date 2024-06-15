'''
Prime factors of a positive integer are the prime numbers that divide that integer exactly.
Given an array arr of n integers and a positive integer num.
Let's suppose prime factorization of num is: p^a x q^b x r^c....x z^f, where p,q,r...z are prime numbers.
Sum of numbers in array arr at indices of prime factors of number num is: a x arr[p] + b x arr[q] + c x arr[r] +......+ f x arr[z].
You are given an array arr of size n and a positive integer num. You are required to calculate the sum of numbers in arr as mentioned
above, and print the same.

Output Format:
Print the sum that was mentioned in the problem statement

Example:
Input:
6
11 21 32 45 1 23
6

Output:
77

Explanation:
6=2^1 x 3^1
sum=1*arr[2]+1*arr[3]=1*32+1*45=77
'''
def prime_factor(n):
    ans = []
    
    i = 2
    while i<=n:
        if n%i==0:
            ans.append(i)
            n = n//i
        else:
            i = i+1
    return ans

ans = prime_factor(6)
s =0
a = [11,21,32,45,1,23]
for i in ans:
    s = s+a[i]
print(s)
'''
OUTPUT:
77
'''