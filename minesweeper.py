from random import randint

class Grid(object):

	def __init__(self,grid_size,mine_count):
		self.grid_size = grid_size
		x_row = [0 for i in range(grid_size)]
		self.grid = [x_row[:] for i in range(grid_size)]
		self.visible = [x_row[:] for i in range(grid_size)]
		for i in range(mine_count):
			y = randint(0,grid_size-1)
			x = randint(0,grid_size-1)
			while self.grid[y][x] == 1:
				y = randint(0,grid_size-1)
				x = randint(0,grid_size-1)
			self.grid[y][x] = 1

	def print_grid(self):
		for y in range(self.grid_size):
			line = ""
			for x in range(self.grid_size):
				if self.visible[y][x] == 0:
					line += "-"
				else: line += self.grid[y][x]
			print line

	def get_tile(self,x,y):
		return self.grid[y-1][x-1]

def main():
	game = Grid(16,40)
	game.print_grid()

if __name__ == "__main__":
	main()
