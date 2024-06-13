'''
ANT ON RAIL:
There is a ant on your balcony it wants to leave the rail so sometimes it moves
right and sometimes it moves left until it get exhasted.Given an integer array A
of given size N which consists of integer 1 and -1 only representing ant's moves
Where 1 means ant moved unit distance towards the right side and -1 means it moves
unit distance towards left. Your task is to find and return the integer value
representing how many times the ant reaches back to original starting position.

NOTE: -Assume 1-Based Indexing
- Assume that railing extends infinetly on the either side.

Input Formate:
Input 1: An integer value N representing the number of moves made by the Ant
Input 2: An integer array A consisting of the ant's moves towards either side
    
Sample I/P:
    5
    1 -1 1 -1 1
Sample O/P:
    2
'''
steps = int(input())  # 5
a = list(map(int, input().split()))
sp = 0
ans = 0
for i in a:
    sp = sp+i
    if sp == 0:
        ans = ans+1
print(ans)
# ===================================
# =============OUTPUT================
'''
5
1 -1 1 -1 1
2
'''
