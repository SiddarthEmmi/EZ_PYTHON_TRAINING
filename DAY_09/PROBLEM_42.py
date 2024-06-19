'''
Generated Numbers:
You have a jar which initially contains N marbles. You can perform the below operations in any order:
1. Taking out A number of marbles from the jar.
2. Taking out B number of marbles from the jar.
Your task is to find and return an integer value, representing the total number of unique positive number of marbles that can be left behind by performing these operations, including the initial number of marbles.

Note:
You can perform the above operations any number of times and in any order keeping in mind that the jor should never become empty.

Input Specification:
A single line containing space seperated integers N,A,B

Sample input:
10 3 5

Sample output:
6
'''
n,a,b = map(int,input().split())

a1 = n//a
b1 = n//b
c = 0
for i in range(a1+1):
    for j in range(b1+1):
        if i*a+j*b<10:
            c += 1
print(c)
'''
Output:
10 3 5
6
'''