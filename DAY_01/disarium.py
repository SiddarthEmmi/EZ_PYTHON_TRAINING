#DAY-01
#disarium

n=135
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
    count=count-1
    ans=ans+p
    n1=n1//10
if ans==o:
    print("Dis")
else:
    print('no')
