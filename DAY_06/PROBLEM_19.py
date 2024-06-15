'''
EQUILIBRIUM:
You are given an array A of N integers. An equilibrium position is a position where the sum of all
integers on its left is equal to the sum of all integers on its right in the array A. Print the index
of the equilibrium position.

Note: For any given array there is only a single equilibrium position, if no equilibrium position is 
found then print "NOT FOUND" without quotes.

The array is 1 indexed.

Input Format:
The input consists of two lines:
The first line contains an integer denoting N.
The second line contains N space-separated integers denoting the elements of the array A.
Input will be read from the STDIN by the candidate

Output Format:
Print the index of the equilibrium position. If no index is found, print "NOT FOUND"

Sample Input:
5
2 4 3 2 7

Sample Output:
3
'''
a = [2,4,3,2,7]
f = 0
for i in range(0,len(a)):
    i1 = i
    j = i+1
    s1=0
    s2=0
    #left side
    while i>=0:
        s1 += a[i]
        i = i-1
    #Right side
    while j<len(a):
        s2 += a[j]
        j = j+1
    if s1==s2:
        print(i1+1)
        f = 1
        break
if f==0:
    print(len(a)//2)
'''
OUTPUT:
3
'''