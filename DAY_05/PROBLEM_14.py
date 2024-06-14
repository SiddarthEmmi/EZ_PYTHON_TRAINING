'''
HEAD AND TAIL:
You are playing a game of Toss and Score in the Hillwood City Mall with your friends. The game consists of the following rules:

Toss an unbiased coin multiple times.

For each heads you get 2 points and for each tails you lose 1 point.

The game ends as soon as you get 3 heads in a row, or you toss the coin throughout the length of string S.

You have been given a string 5 consisting of letters H (for heada) and T (for tails) denoting the sequence results you get on the
toss of coin N times. Your task is to find and return an integer valus representing the final score you get once the game ends.

Note: The final score can be negative too

Input Specification:

Input: A string s. representing the sequence of results you get on the toss of coin N times.

SAMPLE INPUT : HHHTT
SAMPLE OUTPUT : 6
'''
str = input()
head_count = 0
tail_count = 0
score = 0
for i in str:
    if i == "H" or i == "H":
        head_count += 1
        score += 2
        if head_count == 3:
            break
    else:
        tail_count += 1
        score -= 1
        if tail_count == 3:
            break
print(score)

# OUTPUT:
# HHHTT
# 6