'''
Problem Statement:
In a quaint village nestled between rolling hills, there were N different salt containers
and N different pepper containers in two separate groups. Each container had a specific level
of bitterness, represented by arrays A and B respectively. The task at hand was to form N 
combinations, each consisting of one salt container and one
pepper container However, there was a twist to the challenge. The objective was to arrange the
combinations in such a way that the maximum bitterness level, which is the sum of salt and pepper
quantities in each combination, was minimized.

Print the lowest possible maximum bitterness level.

Input Format:
The first line contains a single integer N, the number of salt and pepper containers in each group.

The second line contains N space-separated Integers, denoting the bitterness level of N salt containers.

The third line contains N space-separated integers, denoting the bitterness level of N pepper containers.

sample input:
3
1 3 5
2 8 6
sample output:
3
'''
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
mini = 999
for i in range(0,len(a)):
    if a[i]+b[i]<mini:
        mini = a[i] + b[i]
print(mini)
'''
Output:
3
1 3 5
2 8 6
3
'''