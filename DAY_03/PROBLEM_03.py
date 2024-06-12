'''
MATH TEST:
Alice has Maths test for which she is underprepared. She has to do atleast 1 question
correctly to pass the test. She decided to do question needs her to find smallest prime 
number which is larger then a given integer N. Your task is to find and return an integer 
value representing the smallest prime number larger then N.
INPUT: An integer value N
Output:Return an integer value representing the smallest prime number larger then N.
'''
def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
num = int(input())
k=num+1
while True:
    if isprime(k):
        print(k)
        break
    k = k+1
    
#==========OUTPUT============
#34
#37