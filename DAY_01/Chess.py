even_rows="2468"
odd_rows='1357'
even_col='bdfh'
odd_col='aceg'
s='h7'
if s[0] in even_rows:
    if s[1] in even_rows:
        print('Black')
    else:
        print('White')
else:
    if s[1] in even_rows:
        print('White')
    else:
        print('Black')