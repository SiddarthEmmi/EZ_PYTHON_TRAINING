'''
ENCODE THE NUMBER:
You work in the Message encoding department of a national security agency. Every
message that is sent from or received in your office is encoded. You have an
integer N and each digit of N is squared and the squared are concatinated together
to encode the original number. Your task is to find and return an integer value
representing the encoded value of the number.

INPUT : An integer value N representing number to be encoded.

OUTPUT : Return an integer value representing the encoded value of the number.

SAMPLE INPUT : 167
SAMPLE OUTPUT : 16394
'''
n = 167


def sum_of_digits(n):
    c = 0
    while n > 0:
        c = c+1
        n = n//10
    return c


def rev(n):
    ans = 0
    while n > 0:
        digit = n % 10
        sq = digit**2
        sod_sq = sum_of_digits(sq)
        ans = ans*(10**sod_sq)+sq
        n = n//10
    return ans


ans = rev(n)


def rev2(n):
    ans2 = 0
    while n > 0:
        digit = n % 10
        ans2 = ans2*10+digit
        n = n//10
    return ans2


print(rev2(ans))
# ================================
# ===========OUTPUT===============
'''
16394
'''