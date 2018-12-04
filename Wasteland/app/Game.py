import pygame
from app.Map import read_map
from app.Player import Player
import sys


class Game:
	def __init__(self):
		self.filename = "src/map.csv"
		# TODO: read config
		self.screen_size = (720, 820)
		self.map_player_area = (0, 0, 450, 450)
		self.map_main_size = (100, 100)
		self.map_main_loc = (500, 500)
		self.map_main_area = self.map_main_loc + self.map_main_size
		self.tile_size = 20

		self.intro_window = False  # tracks if the intro window is open

		# TODO: load data
		self.image_dict_str = {
		    'f' : 'forest.jpg',    'g' :    'grassland.jpg',
		    'p' : 'plain.jpg',     'mt':    'mountain.jpg',
		    'ml': 'marshland.jpg', 'h' :    'hill.jpg',
		    'i' : 'ice.jpg',       'sf':    'snowfield.jpg',
		    'sb': 'snowberg.jpg',  'e' :    'exit.jpg',
		    'w' : 'water.jpg',     'b1':    'bridge_h.jpg',
		    'b2': 'bridge_v.jpg',  'player':'player.jpg'
		}

		self.direct = 'img/'
		self.image_dict = {}
		for tag, img_name in self.image_dict_str.items():
			self.image_dict[tag] = pygame.image.load(self.direct + img_name)

		# initialize map
		self.map = read_map(self.filename)

		# initialize player
		self.player = Player()

		# initialize screen
		screen = pygame.display.set_mode(self.screen_size)

		# initialize main map
		self.map_main_surface = self.map.to_surface(self.image_dict, self.tile_size)

		# draw the player on main map
		self.map_main_surface.blit(self.image_dict['player'], self.player.get_area())

		# initialize player map
		self.map_main_surface.subsurface(self.player.get_rect())

		screen.blit(pygame.transform.scale(self.map_main_surface, self.map_main_size), self.map_main_area)
		pygame.display.flip()

	def intro(self):
		self.intro_window = True

		while self.intro_window:

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						pygame.quit()
						sys.exit()


def init_game():
	return Game()
