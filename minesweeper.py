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
			self.grid[y][x] = "B"
		for y in range(grid_size):
			for x in range(grid_size):
				if self.grid != "B":
					print("natab")

	def surrounding_mines(self,x,y):
		amt = 0
		if self.get_tile(x+1,y) == "B": amt += 1
		if self.get_tile(x+1,y+1) == "B": amt += 1
		if self.get_tile(x+1,y-1) == "B": amt += 1
		if self.get_tile(x-1,y) == "B": amt += 1
		if self.get_tile(x-1,y+1) == "B": amt += 1
		if self.get_tile(x-1,y-1) == "B": amt += 1
		if self.get_tile(x,y+1) == "B": amt += 1
		if self.get_tile(x,y-1) == "B": amt += 1

	def print_grid(self):
		for y in range(self.grid_size):
			line = ""
			for x in range(self.grid_size):
				line += self.get_vis_tile(x,y)
			print line

	def get_tile(self,x,y):
		if x >= self.grid_size or x < 0 or y >= self.grid_size or y < 0:
			return 0
		else: return self.grid[y][x]

	def set_tile(self,x,y,val):
		if not (x >= self.grid_size or x < 0 or y >= self.grid_size or y < 0):
			self.grid[y][x] = val

	def get_vis_tile(self,x,y):
		return str(self.grid[y][x]) if self.visible[y][x] else "-"

	def set_vis_tile(self,x,y,val):
		self.visible[y][x] = val

	def click(self,x,y):
		self.set_vis_tile(x,y,1)
		if self.get_tile(x,y) == "B":
			print("bomb hit")
		else: self.check_surroundings(x,y)

	def check_surroundings(self,x,y):
		if x+1 != self.grid_size:
			if self.get_tile(x+1,y) != "B":
				self.click(x+1,y)
			if y+1 != self.grid_size:
				if self.get_tile(x+1,y+1):
					self.click(x+1,y+1)
			if y != 0:
				if self.get_tile(x+1,y-1) != "B":
					self.click(x+1,y-1)
		if x != 0:
			if self.get_tile(x-1,y) != "B":
				self.click(x-1,y)
			if y+1 != self.grid_size:
				if self.get_tile(x-1,y+1) != "B":
					self.click(x-1,y+1)
			if y != 0:
				if self.get_tile(x-1,y-1) != "B":
					self.click(x-1,y-1)
		if y+1 != self.grid_size:
			if self.get_tile(x,y+1) != "B":
				self.click(x,y+1)
		if y != 0:
			if self.get_tile(x,y-1) != "B":
				self.click(x,y-1)


def main():
	game = Grid(16,40)
	game.set_vis_tile(5,3,1)
	game.set_vis_tile(5,4,1)
	game.print_grid()

if __name__ == "__main__":
	main()
