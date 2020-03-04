import random

#tracking wins
user_wins = 0
comp_wins = 0

lose = ('Haha, you got beat by 50 lines of code')
win = ('You won this round')

user_input = input('Choose rock, paper or scissors: \n')

if user_input in ['Rock', 'rock', 'R', 'r']:
    user_choice = 'r'
elif user_input in ['Paper', 'paper', 'P', 'p']:
    user_choice = 'p'
elif user_input in ['Scissors', 'scissors', 'S', 's']:
    user_choice = 's'
else:
    print('Thats not rock paper or scissors')
    exit()

comp_choice = random.randint(1,3)
comp_choice = 3

if comp_choice == 1:
    comp_choice = 'r'
elif comp_choice == 2:
    comp_choice = 'p'
else:
    comp_choice = 's'

#comparing user to comp choice
if user_choice == comp_choice:
    print('Issa draw')
elif (user_choice == 'r' and comp_choice == 'p') \
    or (user_choice == 'p' and comp_choice == 's') \
    or (user_choice == 's' and comp_choice == 'r'):
        print(lose)
else:
    print(win)

print('Your wins', user_wins)
print('Computer wins, comp_wins')
