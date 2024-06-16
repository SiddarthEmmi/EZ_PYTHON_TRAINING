'''
Reduce To Zero:
Write a program that takes two positive integers as input and continuously
reduces the larger number by subtracting the smaller number from it until one 
of the numbers becomes zero. The program should then output the non-zero number,
which will be the greatest common divisor (GCD) of the two input numbers.

The program follows these steps:
1) if x<y swap
2) if y=0 then return x
3) itherwise let T=x-y
4) set x=y and the set y=t
5) repeat from step 1

Ur task is to find and return an integer value, representing the value of x,
when the value of y has been reduced to zero.

NOTE: Atleast one of the x or y will be a non zero integer.

Input: 48
       18
Output: 6
'''
x = int(input())
y = int(input())
while y>0:
    if x<y:
        temp = x
        x = y
        y = temp
    t=x-y
    x=y
    y=t  
print(x)
'''
Output:
48
18
6
'''