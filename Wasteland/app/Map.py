from app.Tile import Tile


class Map:
	def __init__(self, tiles, width, height):
		self.tiles = tiles
		self.width = width
		self.height = height

	def get_tiles(self):
		return self.tiles

def read_map(filename):
	temp_map = []
	with open(filename, 'r') as f:
		lines = f.readlines()

		for line in lines:
			row = line.lower().strip().split(',')
			temp_row = []
			for item in row:
				temp_row.append(Tile(item))

			temp_map.append(temp_row)

	my_map = Map(temp_map, 100, 100)
	return my_map


def obstacle(my_map, x, y):
	this_map = my_map.get_tiles()
	if this_map[x][y].is_obstacle():
		return True
	return False
