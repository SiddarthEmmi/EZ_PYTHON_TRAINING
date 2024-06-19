'''
Signature for LCM:
Given two numbers a and b. Find the GCD and LCM of and d.

Input:
• Two positive Integers a and b (1 <=a, b <=1000)

Output:
For GCD function, an integer representing the GCD of a and b
For LCM function, an integer representing the LCM of a and b

Sample Input:
12 18

Output:
6
36
'''
#gcd
a = int(input())
b = int(input())
orig_a = a
orig_b = b
while b!=0:
    temp = b
    b = a % b
    a = temp
gcd = a
print(gcd)

lcm = (orig_a*orig_b)//gcd
print(lcm)
'''
Output:
12
18
6
36
'''