#Identifying defective chocolate for a prisoner
'''
Question:
There are 10 Chocolates i want to distrubute to prisoners, assume there are 
6 prisoners if i start distributing chocolates at 3rd prisoners it should go 
through circular find the prisoner who will get defective chocolate 
'''
#DAY-01
c=int(input("Enter no of chocolates:"))
n=int(input("Enter the no of prisoner:"))
s=int(input("Enter the starting point:"))
last=(s+c-1)%n
if(last==0):
    last=n
print(last)
#=================================================
#==================OUTPUT=========================
'''
Enter no of chocolates:10
Enter the no of prisoner:6
Enter the starting point:3
6
'''