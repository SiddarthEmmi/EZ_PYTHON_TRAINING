'''
DIWALI CONTENT:
Max is planning to take part i Diwali contest at a Diwali Party that will begin at 8 PM
and will run until midnight(12 AM) i.e., for 4 Hours. He also need to travel to the party
venue within this time which takes him P minutes. The contest comprises of N problems that
are arranged in order of difficulty, with problem 1 being the simplest and problem N begin
the most difficult. Max aware that he will require 5*i minutes to solve the i th problem.

Your task is to help Max find and return an integer value, representing the number of problems
Max can solve and reach the party venue within the given time frame of 4 hours.

NOTE: Max will leave his home at exactly 8 PM to reach the party venue.

INPUT FORMATE:
I/P 1 : An integer value N, representing the total number of problems
I/P 2 : An integer value P representing the time to travel in minutes from the home to party venue.

SAMPLE INPUT:
            6
            180
SAMPLE OUTPUT:
            4
            
EXPLINATION:
The amount of time left to solve problem is 4*60-180 = 60
1st Problem : 5 Mins, Time left 60-5 = 55 Mins
2nd Problem : 10 Mins, Time left 55-10 = 45 Mins
3rd Problem : 15 Mins, Time left 45-15 = 30 Mins
4th Problem : 20 Mins, Time left 30-20 = 10 Mins
5th problem : 25 Mins
So he can solve only 4 problems as he is not left with 25 Mins to complete 5th Problem.
'''
problems = int(input())
time = int(input())
c = 0
s = 0
rem_time = 4*60-180
for i in range(1, problems+1):
    s = s+5*i
    if s > rem_time:
        break
    c = c+1
print(c)
# =========OUTPUT===========
'''
6
180
4
'''