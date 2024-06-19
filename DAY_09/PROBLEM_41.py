'''
Robo Race:
There is a robot race happening between two robots named Robotop and Robocop. 
Both the robots reach the starting point to begin the race on a Circular track

Race starts at time T = 0 seconds. Robotop starts the race at T = Xth second and
takes exactly N seconds to complete one lap. On the other hand. Robocop starts the
race at T = Yth second and takes exactly M seconds to complete one lap.

Your task is to find and return an integer value, representing the least time T (in seconds) 
at which these two robots meet each other again at the starting point.

Sample Input:
2314

Sample Outputs
5

Explanation:

x = 2 N = 3 Y = 1 , N = 4

Robotop starts at T = 2 and completes one lap every 3 seconds. Robocop starts at T = 1 and 
completes one lap every 4 seconds. The smallest point where both meet at the starting point is 5 seconds.

'''
x,n,y,m = map(int,input().split())
time = max(x,y)
while True:
    if time>=x and (time-x)%n==0 and time>=y and (time-y)%m==0:
        print(time)
        break
    time += 1
'''
Output:
2 3 1 4
5
'''