'''
FIND MISSING AND REPEATED VALUES:
You are given a 0-Indexed 2D integer matrix grid of size n*n with values in the range [1,n**2] Each integer appears exactly once except a which appears twice and b which is missing. The task is to find the repeating and missing numbers a and b.

Return a O-Indexed integer array ans of size 2 where ans (9) equals to a and ana [1] equals to b

Example 1:

Input 1 grid = [[1,3],[2,2]]

Output: [2,4]

Explanation: Number 2 is repeated and number 4 is missing so the answer is [2,4]

Example 2:

Input 1 grid: [[9,1,7],[8,9,2],[3,4,6]]

Output: [9,5]

Explanation: Number 9 is repeated and number 5 is missing so the answer is [9,5]
'''
a = []
r,c=3,3
for i in range(0,r):
    sub = []
    print("Enter values for row ",i)
    for j in range(0,c):
        print("enter values for column ",j)
        ele = int(input())
        sub.append(ele)
        print(sub)
    a.append(sub)
    print(a)
    
d = {}
ans = []
for i in range(0,r):
    for j in range(0,c):
        if a[i][j] not in d:
            d[a[i][j]] = 1
        else:
            d[a[i][j]] += 1
            if d[a[i][j]] == 2:
                ans.append(a[i][j])


#MISSING
for i in range(1,r**2+1):
    if i not in d:
        ans.append(i)
print(d)
print(ans)    
'''
OUTPUT:
[[9, 1, 7], [8, 9, 2], [3, 4, 6]]
{9: 2, 1: 1, 7: 1, 8: 1, 2: 1, 3: 1, 4: 1, 6: 1}
[9, 5]
'''