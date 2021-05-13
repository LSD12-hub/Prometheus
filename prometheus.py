import random

grid = 3
isRunning = True
playerDirection
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
	'level2' : [['-' for i in range(grid + 1)],['-' for i in range(grid + 1)],['-' for i in range(grid + 1)],['-' for i in range(grid + 1)]],
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
		levels.get(level)[player.get('x')][player.get('y')] = player.get('name')
		levels.get(level)[wolf.get('x')][wolf.get('y')] = wolf.get('name')
		levels.get(level)[fire.get('x')][fire.get('y')] = fire.get('name')
	if level == 'level3':
		grid = 5
		levels.get(level)[player.get('x')][player.get('y')] = player.get('name')
		levels.get(level)[wolf.get('x')][wolf.get('y')] = wolf.get('name')
		levels.get(level)[fire.get('x')][fire.get('y')] = fire.get('name')
	
def main():
	print('************level 1***********')
	generateCharacters('level1')
	for i in range(len(levels.get('level1'))):
		for j in range(len(levels.get('level1'))):
			print(levels.get('level1')[i][j], end = '')
		print('')
	print('******************************\n')
	
	while isRunning:
		gamePlay()

def moveUp():
	print('move up')
	#make sure they move up
	
def moveDown():
	print('move down')
	#make sure they move down

def moveRight():
	print('move right')
	#make sure they move right

def moveLeft():
	print('move left')
	#make sure they move left

def checkMove():
        #Check if move can be made
        #if can be made return false
        #if not return true
        return false

#def fightRun():
        #do the calualations for the Xp and all
        
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
        
def gamePlay():
	print('XP: ' + str(player.get('xp')))
	print('Location ' + str(player.get('x')) + ',' + str(player.get('y')))
	print('1. UP')
	print('2. DOWN')
	print('3. LEFT')
	print('4. RIGHT')
	playerDirection = input('Please input a move: ')
	print()
	
	while checkMove():
                playerDirection = input('Sorry not valid move, please retry: ')
                
        if playerDirection == '1':
                moveUp()
        if playerDirection == '2':
                moveDown()
        if playerDirection == '3':
                moveRight()
        if playerDirection == '4':
                moveLeft()

        checkSquare()
        checkItems()
	print('XP: ' + str(player.get('xp')))
	print('Location ' + str(player.get('x')) + ',' + str(player.get('y')))
	
main();
