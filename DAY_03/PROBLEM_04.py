# 6 28 66 120 190 276
# If we enter 6 then the following numbers should be displayed,
# 1st we should find  what is the logic b/w those numbers
'''
LOGIC:
2*3=6
4*7=28
6*11=66
8*15=120
10*19=190
12*23=276
14*27=378
'''
#========1ST METHOD=========
n = 6
k = 22
for i in range(1, 7):
    print(n)
    n = n+k
    k = k+16
#========2ND METHOD=========
a = 2
b = 3
for i in range(1, 7):
    n = a*b
    print(n)
    a = a+2
    b = b+4
#=========OUTPUT============
'''
6
28
66
120
190
276
'''
