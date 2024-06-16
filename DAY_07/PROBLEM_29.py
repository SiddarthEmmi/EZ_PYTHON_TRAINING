'''
Nearest Corner:
Bruce is a newly hired employee at a company. The Office Management Department
has given him a desk number, which is stored in string S. He has also been handed
a string array A. containing all the N office desk numbers.

Array A also includes the symbol"-", which stands for the gap in the sitting arrangement.
Comer seats are those that are on either side of the gap. Your task is to help Bruce find
and retum an integer value representing how far he is from the nearest corner seat. 
Return O, if he is in the corner seat.

Note:

There will always be at least one gap in the string array A

Desk number is always in a format of a number first followed by an English letter in uppercase

Assume 0-based indexing

Input Specification:

A string S. representing Bruce's newly assigned desk number

Second line containing space seperated strings showing the seat positions and gaps

Sample Input:
4D
1A - 2B 3C 4D 5E - 6F

Sample Output:
1

'''
chair = input()
s = list(input().split())

#Find index
z = 999
c_ind = s.index(chair)
#till c_ind
for i in range(0,c_ind):
    if s[i]=="-":
        if abs(c_ind-i)-1<z:
            z = abs(c_ind-i)-1
#Right side
for i in range(c_ind+1,len(s)):
    if s[i]=="-":
        if abs(i-c_ind)-1<z:
            z = abs(i-c_ind)-1
            
print(z)
'''
Output:
4D
1A - 2B 3C 4D 5E - 6F
1
'''