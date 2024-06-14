'''
MINIMUM ARRAY SUM:
Paul is given an array A of length N. He must perform the following operations on array sequentially.

-->Choose any 2 integer from the array and calculate their average.

-->If any element is less then average, update it to 0. However, if the element is greater then or equal
tothe average, he need not update it.

-->Your task is to help paul find and return integer value, representing the maximum possible sum of all
the elements in the array by performing the above operations.

NOTE : An exact average should be calculated even if it results in a decimal.

INPUT FORMAT:
I/P 1: An integer N, representing the size of the array A
I/P 2: An integer array A

OUTPUT FORMAT:
Return an integer value representing the minimun possible sum of all the elements in the array by.

SAMPLE I/P: 5
            1 2 3 4 5
SAMPLE O/P: 5
'''
#12,16,2,23,1
a=list(map(int,input().split()))
mx = -999
mx2 = -999
#max1
for i in a:
    if i>mx:
        mx = i
        
#max2
for i in a:
    if i>mx2 and i!=mx:
        mx2 = i
        
avg = (mx + mx2)/2
ans=0
for i in a:
    if i>avg:
        ans += i
print(ans)
'''
OUTPUT:
1 2 3 4 5
5
'''
