'''
CHOCOLATE JAR:
You are given an integer array of size N, representing jars of chocolates.
Three students A,B&C respectively will pick chocolates one by one from each
chocolate jar till the jar is empty and then repeat same with the rest of the
jars. Your task is to find and return an integer value representing the total
number of chocolates that student A will have after all chocolates have been 
picked from all the jars.

NOTE: Once a jar is done A will start taking the chocolate from new jar.

INPUT FORMATE:
I/P 1: An integer array representing the quantity of the chocolate in each jar.
I/P 2: An integer value N representing the number of jars.

OUTPUT FORMATE:
Return an integer value representing the total number of chocolate that student
A will have, after all the chocolates are picked.

EXAMPLE:
I/P : 10 20 30
      3
O/P : 21
'''
l = list(map(int, input().split()))
n = int(input())
a = 0
for i in l:
    a = a+(i//3)
    # remainder
    if i % 3 != 0:
        a = a+1
    else:
        a = a+0
print(a)
# ================================
# ===========OUTPUT===============
'''
10 20 30
3
21
'''