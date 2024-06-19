'''
Pyramid sum:
Adam has a pyramid of numbers. The pyramid structure is formed by
arranging the numbers in the following pattern

     1
    212
   32123
  4321234
 543212345
N---212---N


The first row contains the number 1. The second row contains the numbers 
2, 1, and 2. The third row contains the numbers 3, 2, 1, 2, and 3. This
pattern continues for subsequent rows, until it reaches N, which represents the height of the pyramid.

Given height of pyramid N find the sum of the numbers in the pyramid and return the sum as the output.

Sample input:
4

Sample output:
36
'''
rows = int(input())#4
ans = 0
for i in range(2,rows+1):#2,3,4
    n = i #2 #3 #4
    while n>1:
        ans += 2*n #2*2=4 #4+2*3=10 #4+2*3+2*2=14 #14+2*4
        n = n-1 #1 #2
ans += rows #36 
print(ans)
'''
Output:
4
36
'''