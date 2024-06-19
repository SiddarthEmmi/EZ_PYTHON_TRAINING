'''
Smallest Number:
prince participated in three olympiads at school and recived marks for all of them
he is intrested in finding out the lowest marks he obtained among the three olympiads.
Write a program to find the minimun mark.

Sample input:
30 55 23

Sample output:
23
'''
l = list(map(int,input().split()))
mini = 999
for i in l:
    if i<mini:
        mini = i
print(mini)
'''
Output:
30 55 23
23
'''