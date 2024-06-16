'''
Special Fibonacci:
Alex is exploring a series and she can came accorss a special series in which
f(N)=f(N-1)*f(N-1)+(N-2)*(N-2) mod 47

where f(0) = 1,f(1)=1

ur task is to help alex find and return an integer value,representing the Nth 
Number in the special series

Input: An integer value N

Output: return an integer value, representing the Nth number in the special series.
'''
#2-->2
#3-->5
def sfib(n):
    if n==0:
        return 1
    if n==1:
        return 1
    return(sfib(n-1)**2+(n-2)**2)%47
print(sfib(6))
'''
Output:
34
'''