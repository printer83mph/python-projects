from random import choice

class Grid(object):
	
	def __init__(self,grid_size,mine_count):
		x_row = [0 for i in range(grid_size)]
		self.grid = [x_row for i in range(grid_size)]
		for i in range(mine_count):
			do:
				j = choice(choice(self.grid))
			while j == 0
			j = 1
	
	def print_grid(self):
		for y in self.grid:
			line = ""
			for x in self.grid[y]:
				line += str(self.grid[y][x])
			print line

	def get_tile(x,y):
		return self.grid[y][x]
