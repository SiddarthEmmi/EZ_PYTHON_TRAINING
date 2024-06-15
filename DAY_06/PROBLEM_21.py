'''
Given an array of integers and a target product, find all unique triplets
in the array that, when multiplied together, equal the target product. The
function should also count the number of such triplets.
You are given an array of integers and a target product. Your task is to write
a function that identifies all unique triplets of indices (i, j, k) in the array
where the product of the numbers at these indices equals the target product. The 
function should return the count of such triplets and print the indices and values
of these triplets.

Input:
An array of integers: [5, 3, 20, 10, 1, 4, 2]
A target product: 60

Output:
Print the indices and values of the triplets.
Print the count of such triplets.
'''
a = [5,3,20,10,1,4,2]
pro = 1
c = 0
t = 60
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        for k in range(j+1,len(a)):
            print("indexes",i,j,k)
            print("Values",a[i],a[j],a[k])
            pro = a[i]*a[j]*a[k]
            if pro==t:
                print(pro)
                print("triplet",a[i],a[j],a[k])
                c = c+1
        print()
print(c)
'''
OUTPUT:
indexes 0 1 2
Values 5 3 20
indexes 0 1 3
Values 5 3 10
indexes 0 1 4
Values 5 3 1
indexes 0 1 5
Values 5 3 4
60
triplet 5 3 4
indexes 0 1 6
Values 5 3 2

indexes 0 2 3
Values 5 20 10
indexes 0 2 4
Values 5 20 1
indexes 0 2 5
Values 5 20 4
indexes 0 2 6
Values 5 20 2

indexes 0 3 4
Values 5 10 1
indexes 0 3 5
Values 5 10 4
indexes 0 3 6
Values 5 10 2

indexes 0 4 5
Values 5 1 4
indexes 0 4 6
Values 5 1 2

indexes 0 5 6
Values 5 4 2


indexes 1 2 3
Values 3 20 10
indexes 1 2 4
Values 3 20 1
60
triplet 3 20 1
indexes 1 2 5
Values 3 20 4
indexes 1 2 6
Values 3 20 2

indexes 1 3 4
Values 3 10 1
indexes 1 3 5
Values 3 10 4
indexes 1 3 6
Values 3 10 2
60
triplet 3 10 2

indexes 1 4 5
Values 3 1 4
indexes 1 4 6
Values 3 1 2

indexes 1 5 6
Values 3 4 2


indexes 2 3 4
Values 20 10 1
indexes 2 3 5
Values 20 10 4
indexes 2 3 6
Values 20 10 2

indexes 2 4 5
Values 20 1 4
indexes 2 4 6
Values 20 1 2

indexes 2 5 6
Values 20 4 2


indexes 3 4 5
Values 10 1 4
indexes 3 4 6
Values 10 1 2

indexes 3 5 6
Values 10 4 2


indexes 4 5 6
Values 1 4 2



3
'''