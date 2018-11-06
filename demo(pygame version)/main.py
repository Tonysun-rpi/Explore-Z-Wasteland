import pygame
import time
import sys


# class for player
class Player:
	def __init__(self):
		self.x_pos = 49
		self.y_pos = 49
		self.is_moving = False
		self.speed = 1
		self.backpack = dict()

	def move(self, direction):
		if direction == 'up' and self.y_pos > 0:
			self.y_pos -= 1
		elif direction == 'down' and self.y_pos < 99:
			self.y_pos += 1
		elif direction == 'left' and self.x_pos > 0:
			self.x_pos -= 1
		elif direction == 'right' and self.x_pos < 99:
			self.x_pos += 1

	def get_pos(self):
		return self.x_pos, self.y_pos


class Tile:
	def __init__(self, name, items=None, player_on=False, mob_on=False):
		# self.is_obstacle = is_obstacle
		if name == 'w' or name == 'mt' or name == 'sb':
			self.obstacle = True
		else:
			self.obstacle = False
		self.name = name
		self.items = items
		self.player_on = player_on
		self.mob_on = mob_on
		self.mob = None
		self.player = None

	def is_obstacle(self):
		return self.obstacle

	def get_name(self):
		return self.name

	def get_items(self):
		return self.items

	def add_items(self, item):
		self.items.append(item)

	def add_player(self):
		self.player_on = True

	def del_player(self):
		self.player_on = False


class Map:
	def __init__(self, tiles, width, height):
		self.tiles = tiles
		self.width = width
		self.height = height


def obstacle(my_map, x, y):
	this_map = my_map.tiles
	if this_map[x][y].is_obstacle():
		return True
	return False


def button(msg, x, y, w, h, ic, ac, action=None):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	# print(click)

	if x + w > mouse[0] > x and y + h > mouse[1] > y:
		pygame.draw.rect(main_canvas, ac, (x, y, w, h))
		if click[0] == 1 and action is not None:
			action()
	else:
		pygame.draw.rect(main_canvas, ic, (x, y, w, h))

	small_txt = pygame.font.Font('freesansbold.ttf', 20)
	txt_surf, txt_rect = text_object(msg, small_txt)
	txt_rect.center = ((x + w / 2), (y + h / 2))
	main_canvas.blit(txt_surf, txt_rect)


def load_image(disp, x, y, img):
	disp.blit(img, (x, y))


def text_object(text, font):
	text_surface = font.render(text, True, black)
	return text_surface, text_surface.get_rect()


def message_display(text):
	large_text = pygame.font.Font('serif.ttf', BIG_FONT_SIZE)
	text_surf, text_rect = text_object(text, large_text)
	text_rect.center = ((DISPLAY_WIDTH / 2), (DISPLAY_HEIGHT / 2))
	main_canvas.blit(text_surf, text_rect)

	pygame.display.update()
	time.sleep(2)


def open_backpack():
	pass


def open_character():
	pass


def quit_game():
	pygame.quit()
	sys.exit()


def game_intro():
	intro = True

	while intro:
		for event in pygame.event.get():
			# print(event)
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					sys.exit()

		main_canvas.fill(white)
		large_txt = pygame.font.SysFont('comicsansms', BIG_FONT_SIZE)
		txt_surf, txt_rect = text_object('Explore-Z-Wasteland', large_txt)
		txt_rect.center = ((DISPLAY_WIDTH / 2), (DISPLAY_HEIGHT / 2))
		main_canvas.blit(txt_surf, txt_rect)

		button('Game start!', DISPLAY_WIDTH * 0.1, DISPLAY_HEIGHT * 0.7, DISPLAY_WIDTH * 0.2, DISPLAY_HEIGHT * 0.1, green, bright_green, game_loop)
		button('Quit', DISPLAY_WIDTH * 0.6, DISPLAY_HEIGHT * 0.7, DISPLAY_WIDTH * 0.2, DISPLAY_HEIGHT * 0.1, red, bright_red, quit_game)

		pygame.display.update()
		clock.tick(15)


def game_loop():
	game_exit = False
	move_up = move_down = move_left = move_right = False

	while not game_exit:

		for event in pygame.event.get():
			if event == pygame.QUIT:
				game_exit = True

			if event.type == pygame.KEYDOWN:
				# TODO: This is for test only. When user clicked on escape, quit the game
				if event.key == pygame.K_ESCAPE:
					game_exit = True

				if event.key == pygame.K_UP or event.key == pygame.K_w:
					# if not obstacle(MY_MAP, AVATAR.y_pos, max(AVATAR.x_pos - 1, 0)):
					# print('Avatar pos: ', AVATAR.get_pos())
					# print('Tile up: ', MY_MAP.tiles[AVATAR.y_pos - 1][AVATAR.x_pos].get_name())
						# AVATAR.move('up')
					move_up = True
					# print('up')

				if event.key == pygame.K_DOWN or event.key == pygame.K_s:
					#if not obstacle(MY_MAP, AVATAR.y_pos, min(AVATAR.x_pos + 1, 99)):
					# print('Avatar pos: ', AVATAR.get_pos())
					# print('Tile up: ', MY_MAP.tiles[AVATAR.y_pos + 1][AVATAR.x_pos].get_name())
					# AVATAR.move('down')
					move_down = True
					# print('down')

				if event.key == pygame.K_LEFT or event.key == pygame.K_a:
					# if not obstacle(MY_MAP, max(AVATAR.y_pos - 1, 0), AVATAR.x_pos):
					# print('Avatar pos: ', AVATAR.get_pos())
					# print('Tile up: ', MY_MAP.tiles[AVATAR.y_pos][AVATAR.x_pos - 1].get_name())
					# AVATAR.move('left')
					move_left = True
					# print('left')

				if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
					# if not obstacle(MY_MAP, min(AVATAR.y_pos + 1, 99), AVATAR.x_pos):
					# print('Avatar pos: ', AVATAR.get_pos())
					# print('Tile up: ', MY_MAP.tiles[AVATAR.y_pos][AVATAR.x_pos + 1].get_name())
					# AVATAR.move('right')
					move_right = True
					# print('right')

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_UP or event.key == pygame.K_w:
					move_up = False

				if event.key == pygame.K_DOWN or event.key == pygame.K_s:
					move_down = False

				if event.key == pygame.K_LEFT or pygame.key == pygame.K_a:
					move_left = False

				if event.key == pygame.K_RIGHT or pygame.key == pygame.K_d:
					move_right = False

		if move_up and not obstacle(MY_MAP, max(AVATAR.y_pos - 1, 0), AVATAR.x_pos):
			AVATAR.move('up')

		if move_right and not obstacle(MY_MAP, AVATAR.y_pos, min(AVATAR.x_pos + 1, 99)):
			AVATAR.move('right')

		if move_left and not obstacle(MY_MAP, AVATAR.y_pos, max(AVATAR.x_pos - 1, 0)):
			AVATAR.move('left')

		if move_down and not obstacle(MY_MAP, min(AVATAR.y_pos + 1, 99), AVATAR.x_pos):
			AVATAR.move('down')


		# set main canvas background to white
		main_canvas.fill(white)

		# draw map display area
		# map_disp = pygame.Surface((TILE_LENGTH * TILE_NUM * MULTIPLIER, TILE_LENGTH * TILE_NUM * MULTIPLIER))  # display area for the game map
		# map_disp.fill(black)
		# main_canvas.blit(map_disp, (0, 0))

		# add a rect to buttom area
		button_disp = pygame.Surface((DISPLAY_WIDTH, DISPLAY_HEIGHT - TILE_LENGTH * TILE_NUM * MULTIPLIER))
		button_disp.fill(green)
		# button('Backpack', 10, 10, 100, 80, red, bright_red, button_disp)
		# pygame.display.update(button_disp.get_rect())
		button('Backpack', 0, DISPLAY_HEIGHT - 100, 200, 100, red, bright_red)
		button('Character', 200, DISPLAY_HEIGHT - 100, 200, 100, blue, bright_blue)

		# main_canvas.blit(button_disp, (0, TILE_LENGTH * TILE_NUM * MULTIPLIER))

		# TODO: get player position and render map
		# coords = AVATAR.get_pos()
		disp_area = (48 * max((AVATAR.x_pos - 7), 0), 48 * max((AVATAR.y_pos - 7), 0), 720, 720)
		main_canvas.blit(THE_MAP, (0, 0), disp_area)
		main_canvas.blit(THE_PLAYER, (336, 336))
		# render_x = 0
		# render_y = 0
		# # print(coords)
		# i = max(coords[0] - 7, 0)
		# while i <= min(coords[0] + 7, 99):
		# 	j = max(coords[1] - 7, 0)
		# 	while j <= min(coords[1] + 7, 99):
		# 		# tile_img = pygame.image.load('./img/' + MY_MAP.tiles[i][j].name + '.jpg')
		# 		# print(MY_MAP.tiles[i][j].name)
		# 		# tile_img = pygame.transform.scale(tile_img, (int(TILE_LENGTH * MULTIPLIER), int(TILE_LENGTH * MULTIPLIER)))
		# 		# map_disp.blit(tile_img, (render_x, render_y))
		# 		this_tile = MY_MAP.tiles[i][j].name
		# 		render_coords = (render_x, render_y)
		# 		print(render_coords)
		# 		if this_tile == 'forest':
		# 			map_disp.blit(FOREST, render_coords)
		# 		elif this_tile == 'grassland':
		# 			map_disp.blit(GRASSLAND, render_coords)
		# 		elif this_tile == 'marshland':
		# 			map_disp.blit(MARSHLAND, render_coords)
		# 		elif this_tile == 'plain':
		# 			map_disp.blit(PLAIN, render_coords)
		# 		elif this_tile == 'exit':
		# 			map_disp.blit(EXIT, render_coords)
		# 		elif this_tile == 'hill':
		# 			map_disp.blit(HILL, render_coords)
		# 		elif this_tile == 'ice':
		# 			map_disp.blit(ICE, render_coords)
		# 		elif this_tile == 'snowberg':
		# 			map_disp.blit(SNOWBERG, render_coords)
		# 		elif this_tile == 'mountain':
		# 			map_disp.blit(MOUNTAIN, render_coords)
		# 		elif this_tile == 'snowfield':
		# 			map_disp.blit(SNOWFIELD, render_coords)
		# 		elif this_tile == 'water':
		# 			map_disp.blit(WATER, render_coords)
		#
		# 		render_x += TILE_LENGTH * MULTIPLIER
		# 		j += 1
		# 		# TODO: add if statements to render the player
		# 	render_x = 0
		# 	render_y += TILE_LENGTH * MULTIPLIER
		# 	i += 1

		# draw surface that displays the player
		# player_disp = pygame.Surface((int(TILE_LENGTH * TILE_NUM * MULTIPLIER), int(TILE_LENGTH * TILE_NUM * MULTIPLIER)), pygame.SRCALPHA, 32)  # display area for player
		# # display the player sprite in the center of this surface
		# player_img = pygame.image.load('./img/player.jpg')
		# player_img = pygame.transform.scale(player_img, (int(TILE_LENGTH * MULTIPLIER), int(TILE_LENGTH * MULTIPLIER)))
		# player_disp.blit(player_img, (int(TILE_LENGTH * MULTIPLIER * 6), int(TILE_LENGTH * MULTIPLIER * 6)))

		pygame.display.flip()
		clock.tick(FPS)


if __name__ == '__main__':
	# set up variables
	DISPLAY_WIDTH = 720  # px
	DISPLAY_HEIGHT = 820  # px
	FPS = 15

	TILE_LENGTH = 20  # px
	TILE_NUM = 15
	MULTIPLIER = 2.4

	BIG_FONT_SIZE = 60
	temp_map = list()
	# read_map('map(Explore_Z_Wasteland).csv', temp_map)
	# print('len of map: ', len(temp_map))
	# print(temp_map[0][0].name)

	# read in map
	with open('map.csv', 'r') as f:
		lines = f.readlines()
		for line in lines:
			row = line.lower().strip().split(',')
			temp_row = []
			for item in row:
				temp_row.append(Tile(item))

			temp_map.append(temp_row)

	print('len of map: ', len(temp_map))
	print(temp_map[0][0].name)

	MY_MAP = Map(temp_map, 100, 100)

	AVATAR = Player()

	# define colors in format of RGB
	black = (0, 0, 0)
	white = (255, 255, 255)
	red = (200, 0, 0)
	bright_red = (255, 0, 0)
	green = (0, 200, 0)
	bright_green = (0, 255, 0)
	blue = (0, 0, 200)
	bright_blue = (0, 0, 255)

	# load all images
	# EXIT = pygame.image.load('./img/large_exit.jpg')
	# FOREST = pygame.image.load('./img/large_forest.jpg')
	# GRASSLAND = pygame.image.load('./img/large_grassland.jpg')
	# HILL = pygame.image.load('./img/large_hill.jpg')
	# ICE = pygame.image.load('./img/large_ice.jpg')
	# MARSHLAND = pygame.image.load('./img/large_marshland.jpg')
	# MOUNTAIN = pygame.image.load('./img/large_mountain.jpg')
	# PLAIN = pygame.image.load('./img/large_plain.jpg')
	# PLAYER = pygame.image.load('./img/large_player.jpg')
	# SNOWBERG = pygame.image.load('./img/large_snowberg.jpg')
	# SNOWFIELD = pygame.image.load('./img/large_snowfield.jpg')
	# WATER = pygame.image.load('./img/large_water.jpg')
	THE_MAP = pygame.image.load('./img/large_out_2.bmp')
	THE_PLAYER = pygame.image.load('./img/large_player.bmp')

	pygame.init()  # init pygame
	main_canvas = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))  # set resolution 16:9 (main disp)

	pygame.display.set_caption('Explore-Z-Wasteland')  # set game title

	clock = pygame.time.Clock()  # create clock

	game_intro()

	# if game loop ended: quit the program
	pygame.quit()
	sys.exit()
