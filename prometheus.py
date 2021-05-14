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
        }

levels = {
        'level1' : [['-' for i in range(grid)], ['-' for i in range(grid)], ['-' for i in range(grid)]],
	'level2' : [['-' for i in range(grid)], ['-' for i in range(grid)], ['-' for i in range(grid)]],
	'level3' : [['-' for i in range(grid + 2)],['-' for i in range(grid + 2)],['-' for i in range(grid + 2)],['-' for i in range(grid + 2)],['-' for i in range(grid + 2)]]
        }
# 81206
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
        
	generateCharacters('level2')
	print(levels.get('level2'))
	while isRunning:
		gamePlay()

def moveUp():
        checkMove(player.get('x') - 1, 0)
        player['x'] = player.get('x') - 1
        print( player.get('x'))
def moveDown():
	print('move down')
	#make sure they move down

def moveRight():
	print('move right')
	#make sure they move right

def moveLeft():
	print('move left')
	#make sure they move left

def checkMove(x, y):
        try:
                levels.get('level2')[x][y] = player.get('name') 
        except:
                chooseMove('error') 

def fightRun():
        print('Calculations for the players')
        
def checkSqure():
        #check if they are in line with the a fire or wolf or treasure
        #if in line with wolf
        print('WOLFFFFFF!\n')
        print('1.FIGHT!')
        choice = input('2.RUN ')
        fightRun(choice)
        
        #if in line with fire
        print('FIREEEEE!\n')
        print('1.FIGHT!')
        choice = input('2.RUN ')
        fightRun(choice)
        
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
                        moveRight()
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
