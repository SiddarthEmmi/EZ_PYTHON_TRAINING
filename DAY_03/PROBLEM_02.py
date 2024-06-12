# ELECTIONS
'''
Input 1: An integer value representing number of voters
Input 2: An integer array A representing the votes of voter

Output: Which party won
Example:
input: 6
1 1 2 2 2 3
output:
6                        (no. of voters)
1 1 2 2 2 3              (no. of votes)
[(1, 2), (2, 3), (3, 1)] (arranged votes like 1st party got 2 votes(1,2), 2nd party got 3 votes(2,3))
[(2, 3), (1, 2), (3, 1)] (same arranged votes in accending order)
2                        (Winning party)
'''
n = int(input())
arr = list(map(int, input().split()))
d = {}
if n == 1:
    arr[0][0]
    print(arr[0])
    exit(0)
else:
    for i in arr:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
ans = -1
vals = list(d.items())
print(vals)
vals.sort(reverse=True, key=lambda x: x[1])
# [(1,2)(2,3)(3,3)]
print(vals)
if len(vals) == 1:
    ans = vals[0][0]

else:
    if vals[0][1] == vals[1][1]:
        ans = -1
    else:
        ans = vals[0][0]
# print(vals)
print(ans)

#==============================================================================
#================================OUTPUT========================================
'''
6
1 1 2 2 2 3
[(1, 2), (2, 3), (3, 1)]
[(2, 3), (1, 2), (3, 1)]
2
'''
