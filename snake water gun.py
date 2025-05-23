import random
print('  WELCOME TO SNAKE🐍 WATER💦 GUN🔫 GAME\n')
name = input('Enter your name : ')
rules = ['Snake drinks water.','Water sinks gun.','Gun shoots snake.']
print('\nHere are the rules :- \n')
for index, rule in enumerate(rules, start=1) :
    print(f'{index}. {rule}')
user_points = 0
comp_points = 0
for i in range(10) :
    user_choice = input('\nYou want to choose Snake 🐍 , Water 💦 or   Gun 🔫 :  ') 
    possible_outcomes = ['Snake','Water','Gun']
    computer_choice = random.choice(possible_outcomes)
    print(f'Your Choice - {user_choice.capitalize()}\nComputer_choice - {computer_choice}')
    # If the match draws. 
    if (user_choice.lower() == computer_choice.lower()) :
        print("It's a DRAW.")
        user_points += 0
        comp_points += 0
    # If the match is not a draw.
    elif (user_choice.lower() == 'snake') :
        if (computer_choice.lower() == 'gun') :
            print('You LOSE. Gun killed the snake. ')
            user_points = user_points - 1
            comp_points += 1
        else :
            print('You WIN. Snake drank the water. ')
            user_points = user_points + 1
            comp_points = comp_points - 1
    elif (user_choice.lower() == 'water') :
        if (computer_choice.lower() == 'snake') :
            print('You LOSE. Snake drank the water. ')
            user_points = user_points - 1
            comp_points += 1
        else :
            print('You WIN. Gun sinked in water. ')
            user_points = user_points + 1
            comp_points = comp_points - 1 
    elif (user_choice.lower() == 'gun') :
        if (computer_choice.lower() == 'water') :
            print('You LOSE. Gun sinked in water. ')
            user_points = user_points - 1
            comp_points += 1
        else :
            print('You WIN. Gun killed the snake. ')
            user_points = user_points + 1
            comp_points = comp_points - 1
    else :
        print('Kindly enter a valid choice')
    print(f'Your Points : {user_points}\nComputer Points : {comp_points}')    
# Telling points of user. 
if (user_points == 0 or user_points == 1):
    print(f'\nSo you scored {user_points} point.')
else :
    print(f'\nSo you scored {user_points} points. ') 
# Telling points of computer. 
if (comp_points == 0 or comp_points == 1):
    print(f'Computer scored {comp_points} point.')
else :
    print(f'Computer scored {comp_points} points.')
# Deciding the final result. 
result = '\nCongratulations! You Won!!' if user_points > comp_points else '\nIt is a tie!' if user_points == comp_points else '\nYou lose!! '
print(result)