'''
QUESTION:
Tom is an programmer. He has designed a program to run the robocar on a horizontal
number line. Initially the car is parkect at C.

-Given an array A of N integer which can be A,B,C the robocar runs as follows as per 
the designed program.

-First the robocar can moves A units in specified direction(right in case the integer is 
Positive and left if the integer is Negative)

-Then robocar first move A unit and then B units in a specified direction.

-In the next step the robocar moves A unit, B unit and the C units in a specified direction

-This process keeps on repeating as per the number of integers in the sequence

-Your task is to find and return an integer value, representing the farthest coordinate
reached by the robocar from the beginning to the end of the process.

SAMPLE INPUT : 
1 -2 3 4

SAMPLE OUTPUT : 
6
'''
a = list(map(int, input().split()))
maxi = -1
s = 0
for i in a:
    s = s+i
    if s > maxi:
        maxi = s
print(maxi)
# =================================
# =============OUTPUT==============
'''
1 -2 3 4
6
'''