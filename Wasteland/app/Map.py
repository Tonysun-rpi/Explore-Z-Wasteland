import pygame
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

def loadMapSurface(map,x,y,image_dict,surface=None):
	if(not surface):
		surface = pygame.Surface((300,300))
	row_s = 0
	for row_m in range(y-15,y+16):
		col_s = 0
		for col_m in range(x-15,x+16):

			if(row_m < 0 or col_m < 0):
				surface.blit(image_dict['mt'],(row_s*20,col_s*20,20,20))
			else:
				surface.blit(image_dict[map.get_tiles()[row_m][col_m].name],(col_s*20,row_s*20,20,20))
			col_s += 1
		row_s += 1
	surface = surface.convert()
	return surface
