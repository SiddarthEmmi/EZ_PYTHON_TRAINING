'''
BASKETBALL:
You are in basketball contest. In this contest the score for each successfull shot
depends on both the distance from the basket and the players position. The ball
is shot N times successfully, you are given an array A containing the distance of
a player from basket for it shots. The index of array represents the position of
the player. Score is calculated by multiplying the position with distance from
the basket.

Your task is to find and return an integer value, representing the maximum possible
score you can achive by choosing a contiguous subarray of size K from the given array.

NOTE:
-->A subarray is a contiguous part of array.
-->Assume 1-Based Indexing.
-->The array player contains both negative and positive values.
-->Assume the player is standing on a cartesian plane.

INPUT FORMATE:
I/P 1 : An integer N representing Number of shots made by player.
I/P 2 : An integer K representing the size of subarray.
I/P 3 : An array of integer.

SAMPLE INPUT:
    5
    2
    1 2 3 4 5
SAMPLE OUTPUT:
    14
'''
input1 = int(input())
input2 = int(input())
arr = list(map(int, input().split()))
mx = -1
for i in range(0, len(arr)-input2+1):
    temp = arr[i:i+input2]
    k, s = 1, 0
    for j in temp:
        s += (j*k)
        k += 1

        if s > mx:
            mx = s
print(mx)
# ===================================
# ============OUTPUT=================
'''
5
2
1 2 3 4 5
14
'''