# 在这里写上你的代码 :-)
import random, sys
print('The Game For the ROCK, PAPER,SCISSORS')
wins = 0
losses = 0
ties = 0

while True:
    print('%s wins, %s losses, %s ties' % (wins, losses, ties))

    while True: #用户输入
        print('Enter your move:(r for ROCK, p for PAPER, s for SCISSORS, or q for exit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit()
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break
        else:
            print('please enter the valid input r, p, S, or q')

    #显示用户选择
    if playerMove == 'r':
        print('ROCK vs ...')
    if playerMove == 'p':
        print('PAPER vs ...')
    if playerMove == 's':
        print('SCISSORS vs ...')

    #显示电脑选择
    computerNumber = random.randint(1,3)
    if computerNumber == 1:
        computerMove = 'r'
        print('ROCK')
    if computerNumber == 2:
        computerMove = 'p'
        print('PAPER')
    if computerNumber == 3:
        computerMove = 's'
        print('SCISSORS')

    #判断
    if playerMove == computerMove:
        print('It is a tie.')
        ties+=1
    elif (playerMove == 'r' and computerMove == 's') \
    or (playerMove == 'p' and computerMove == 'r') \
    or (playerMove == 's' and computerMove == 'p'):
        print('You are win.')
        wins+=1
    else:
        print('You are lose.')
        losses+=1

print()

















