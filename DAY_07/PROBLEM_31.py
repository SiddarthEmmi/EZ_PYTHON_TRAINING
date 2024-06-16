'''
Maximum pair product:
Noah is given an Integer array A of length N. He must perform the foliowing operations:
Select any integer pair having sum equal to 18 from the array.
Select the pair with maximum product such that the first element of the pair is greater than the second element of the pair

Your task is to help Noah find and return a pair in the form of an integer array, which satisfies the mentioned conditions.

Input Specification:

Input1: An integer value N, representing the size of array A.

Input2: An integer array A.

Output Specification:

the pair in the form of an integer array, which satisfies the mentioned
sample input:
8
11 12 2 8 10 11 9 8
sample output:
[10,8]
'''
n = int(input())
a = list(map(int,input().split()))
p_max = -999
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]+a[j]==18:
            if a[i]>a[j]:
                p = a[i]*a[j]
                if p>p_max:
                    p_max = p
                    k = a[i]
                    h = a[j]
print(k,h)
'''
Output:
8
11 12 2 8 10 11 9 8
10 8
'''