import random

grid = 3
isRunning = True
playerDirection = ''

player = {
	'name' : 'p',
	'x' : 1,
	'y' : 1,
	'xp' : 50
	#'fight' : fight(),
	#'up' : moveUp(),
	#'Down' : moveDown(),
	#'right' : moveRigh(),
	#'Left' : moveLeft(),
	#'run' : run()
}
wolf = {
	'name' : 'w',
	'x' : random.randint(0, grid - 1),
	'y' : random.randint(0, grid - 1),
	'xp' : 30
}
fire = {
	'name' : 'f',
	'x' : random.randint(0, grid - 1),
	'y' : random.randint(0, grid - 1),
	'xp' : 25
}
treasure = {
        'name1' : 't1',
        'name2' : 't2',
        'x1' : random.randint(0, grid - 1),
        'x2' : random.randint(0, grid - 1),
        'y1' : random.randint(0, grid - 1),
        'y2' : random.randint(0, grid - 1),
        'xp' : 20
        }

levels = {
        'level1' : [['-' for i in range(grid)], ['-' for i in range(grid)], ['-' for i in range(grid)]],
	'level2' : [['-' for i in range(grid)], ['-' for i in range(grid)], ['-' for i in range(grid)]],
	'level3' : [['-' for i in range(grid + 2)],['-' for i in range(grid + 2)],['-' for i in range(grid + 2)],['-' for i in range(grid + 2)],['-' for i in range(grid + 2)]]
        }

def generateCharacters(level):
	if level == 'level1':		
		grid = 3
		levels.get(level)[player.get('x')][player.get('y')] = player.get('name')
		levels.get(level)[wolf.get('x')][wolf.get('y')] = wolf.get('name')
		levels.get(level)[fire.get('x')][fire.get('y')] = fire.get('name')
	if level == 'level2':
		grid = 3
		levels.get(level)[treasure.get('x1')][treasure.get('y1')] = treasure.get('name1')
		levels.get(level)[treasure.get('x2')][treasure.get('y2')] = treasure.get('name2')
		levels.get(level)[wolf.get('x')][wolf.get('y')] = wolf.get('name')
		levels.get(level)[fire.get('x')][fire.get('y')] = fire.get('name')
		levels.get(level)[player.get('x')][player.get('y')] = player.get('name')
		
	if level == 'level3':
		grid = 5
		levels.get(level)[player.get('x')][player.get('y')] = player.get('name')
		levels.get(level)[wolf.get('x')][wolf.get('y')] = wolf.get('name')
		levels.get(level)[fire.get('x')][fire.get('y')] = fire.get('name')

def eee(level):
        while True:
                if 'f' in level.get(level) and 'p' in level.get(level) and 'w' in level.get(level):
                        break
                else:
                        generateCharacters(level)
                        
	
def main():
    print('************level 1***********')
    generateCharacters('level1')
    for i in range(len(levels.get('level1'))):
	    for j in range(len(levels.get('level1'))):
		    print(levels.get('level1')[i][j], end = '')
	    print('')
    print('******************************\n')

    print('************level 2***********\n')
    generateCharacters('level2')
    print(levels.get('level2'))
    while isRunning:
    	gamePlay()

    print('*****************************\n')
    
    print('***********level 3***********\n')
    generateCharacteres('level3')
    print(levels.get('level3'))
    while isRunning:
        gamePlay()

def moveUp():
    checkMove(player.get('x') - 1, 0)
    player['x'] = player.get('x') - 1
    checkCell()
    isRunning = killGame()

def moveDown():
    checkMove(player.get('x') + 1, 0)
    player['x'] = player.get('x') + 1 
    checkCell()
    isRunning = killGame()

def moveRight():
    checkMove(0, player.get('y') + 1)
    player['y'] = player.get('y') + 1
    checkCell()
    isRunning = killGame()

def moveLeft():
    checkMove(0, player.get('y') - 1)
    player['y'] = player.get('y') - 1
    checkCell()
    isRunning = killGame()

def killGame():
    print(levels.get('level2'))
    for lev in levels.get('level2'):
        if lev == 'w' or lev == 'f' or lev == 't1' or lev == 't2':
            return True
    return False

def checkMove(x, y):
    if x not in range(0, grid):
        chooseMove('error') 
    
    if y not in range(0,grid):
        chooseMove('error')

def fightOrRun(choice, NPC):
    while NPC == 'wolf':
        if choice == '1':
            print("You beat the wolf -30 XP ")
            player['xp'] = player.get('xp') - wolf.get('xp')
            levels.get('level2')[player.get('x')][player.get('y')] = '-'
            break
        elif choice == '2' :
            print("-1 Xp")
            player['xp'] =player.get('xp')-1
            player['x'] = 1
            player['y'] = 1
            break
        else:
            choice = input('Sorry not a valid move, Please try again: ')

    while NPC == 'fire':
        if choice == '1':
            print("You beat the fire -25 XP ")
            player['xp']=player.get('xp') - fire.get('xp')
            levels.get('level2')[player.get('x')][player.get('y')] = '-'
            break
        elif choice == '2' :
            print("-1 Xp")
            player['xp'] = player.get('xp') -1
            player['x'] = 1
            player['y'] = 1
            break
        else:
            choice = input('Sorry not a valid move, Please try again: ')

def checkCell():
    #check if they are in line with the a fire or wolf or treasure
    if player.get('x') == wolf.get('x') and player.get('y') == wolf.get('y'):
        print('\nWOLFFFFFF!\n')
        print('1.FIGHT!')
        choice = input('2.RUN ')
        fightOrRun(choice, 'wolf')
        
    if player.get('x') == fire.get('x') and player.get('y') == fire.get('y'):
        print('\nFIREEEEE!\n')
        print('1.FIGHT!')
        choice = input('2.RUN ')
        fightOrRun(choice, 'fire')
       
    if player.get('x') == treasure.get('x1') and player.get('y') == treasure.get('y1'):
        print('\nTREEEEEAAAAAASSSUUUURE\n')
        print('You just got treasure! +20 XP\n')
        #add player xp + 20
        player['xp'] = player.get('xp') + treasure.get('xp')
        levels.get('level2')[player.get('x')][player.get('y')] = '-'

    if player.get('x') == treasure.get('x2') and player.get('y') == treasure.get('y2'):
        print('\nTREEEEEAAAAAASSSUUUURE\n')
        print('You just got treasure! +20 XP\n')
        #add player xp + 20
        player['xp'] = player.get('xp') + treasure.get('xp')
        levels.get('level2')[player.get('x')][player.get('y')] = '-'


def checkItems():
        #I will do this one
        print('check')

def chooseMove(place):
        if place == 'playgame':
                playerDirection = input('Please input a move: ')
        elif place == 'error':
                playerDirection = input('Sorry not valid move, please retry: ')
        while True:
                if playerDirection == '1':
                        moveUp()
                        break
                elif playerDirection == '2':
                        moveDown()
                        break
                elif playerDirection == '3':
                        moveLeft()
                        break
                elif playerDirection == '4':
                        moveRight()
                        break
                else:
                        playerDirection = input('Sorry not valid move, please retry: ')                

def gamePlay():
	print('XP: ' + str(player.get('xp')))
	print('Location ' + str(player.get('x')) + ',' + str(player.get('y')))
	print('1. UP')
	print('2. DOWN')
	print('3. LEFT')
	print('4. RIGHT')
	chooseMove('playgame')
	print()
	print('XP: ' + str(player.get('xp')))
	print('Location ' + str(player.get('x')) + ',' + str(player.get('y')) + '\n')
	
main();
