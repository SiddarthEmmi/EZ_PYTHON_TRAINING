'''
Solve the equation:
Given a positive integer N, find all sets of three positive integers a,b, and c that satisfy the following equation:

a^2+b^2+c^2+ab+bc+ca = N

Note: a, b and c ore positive integers, and their values can be the same.

Input Specification:

Input1: An integer value N

Output Specification:

Return an integer value, representing the number of sets of three positive integers that satisfy the equation given above.

Sample Input:
6

Sample Output:
1

'''
n = 6
f = 0

for a in range(1, n):
    for b in range(1, n):
        for c in range(1, n):
            if a**2 + b**2 + c**2 + a*b + b*c + c*a == n:
                print(a, b, c)
                f += 1

print(f)
if f == 0:
    print("NP")
'''
Output:
1
'''