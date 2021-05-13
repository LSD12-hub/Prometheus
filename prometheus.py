import random

grid = 3
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
		grid = 4
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
	
	
main();
