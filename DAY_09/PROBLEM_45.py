'''
Number of toys:
Akshay has a number of toys and he decided to donate some of them to an NGO.
Af the donation, he still has some toys left. Write a program to help Akshay to determi the number of remaining toys.

Example:
Input: 50 45

Output: The remaining number of toys = 5

Input: 60 6

Output: The remaining number of toys = 54
'''
a,b = map(int,input().split()) 
print("The remaining number of toys = ",a-b)
'''
Output:
50 45
The remaining number of toys = 5
'''