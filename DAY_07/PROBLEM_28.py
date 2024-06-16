'''
Fellis Function:
morris fellis has come with a new function called fellis function morris defines the function as follows:
f(0)=1
f(1)=1
f(N)=f(N-1)+7*f(N-2)+(N/4) modulo 10^9 + 7

Given an integer N, ur task is to help morris find and return an integer value of f(N).
after performing fellis function.

NOTE: Here the division operator is integer division operator i.e., divides two numbers and return 
the integer part of the result. 

Input 1 : An integer value N,representing the fellis function value.

sample input:
8
sample output:
6713
'''
n = int(input())
x = [1,1]
for i in range(2,n+1):
    ans = (x[i-1]+7*x[i-2]+i//4)%(10**9+7)
    x.append(ans)
    
print(x[n])

#Recursion
def fel(n):
    if n==0:
        return 1
    if n==1:
        return 1
    return (fel[i-1]+7*fel[i-2]+i//4)%(10**9+7)
'''
Output:
8
6713
'''