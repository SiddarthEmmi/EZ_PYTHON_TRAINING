#DAY-01
n=153
n1=n
ans=0
o=n
count = 0
while n>0:
    count=count+1
    n=n//10 
    
while n1>0:
    digit=n1%10
    p=digit**count
    ans=ans+p
    n1=n1//10
if ans==o:
    print("Arm")
else:
    print('no')
