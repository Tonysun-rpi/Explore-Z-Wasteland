import pygame
import time
import sys
import sqlite3
from app.Player import Player
from app.Tile import Tile
from app.Map import Map, read_map, obstacle

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (200, 0, 0)
BRIGHT_RED = (255, 0, 0)
GREEN = (0, 200, 0)
BRIGHT_GREEN = (0, 255, 0)
BLUE = (0, 0, 200)
BRIGHT_BLUE = (0, 0, 255)


def quit_game():
	pygame.quit()
	sys.exit()


def text_object(text, font):
	text_surface = font.render(text, True, BLACK)
	return text_surface, text_surface.get_rect()


def button(main_canvas, msg, x, y, w, h, ic, ac, action=None):
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


def main_game_loop(game_map, avatar, main_canvas, clock, disp_w=720, disp_h=820, tile_len=20, tile_num=15, mult=2.4):
	game_exit = False
	move_up = move_down = move_left = move_right = False

	while not game_exit:

		for event in pygame.event.get():
			if event == pygame.QUIT:
				game_exit = True

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					game_exit = True

				if event.key == pygame.K_UP or event.key == pygame.K_w:
					move_up = True

				if event.key == pygame.K_DOWN or event.key == pygame.K_s:
					move_down = True

				if event.key == pygame.K_LEFT or event.key == pygame.K_a:
					move_left = True

				if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
					move_right = True

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_UP or event.key == pygame.K_w:
					move_up = False

				if event.key == pygame.K_DOWN or event.key == pygame.K_s:
					move_down = False

				if event.key == pygame.K_LEFT or pygame.key == pygame.K_a:
					move_left = False

				if event.key == pygame.K_RIGHT or pygame.key == pygame.K_d:
					move_right = False

		if move_up and not obstacle(game_map, max(avatar.y_pos - 1, 0), avatar.x_pos):
			avatar.move('up')

		if move_right and not obstacle(game_map, avatar.y_pos, min(avatar.x_pos + 1, 99)):
			avatar.move('right')

		if move_left and not obstacle(game_map, avatar.y_pos, max(avatar.x_pos - 1, 0)):
			avatar.move('left')

		if move_down and not obstacle(game_map, min(avatar.y_pos + 1, 99), avatar.x_pos):
			avatar.move('down')

		# end of event handlers

		# begin drawing the canvas
		# TODO: add more canvas here
		pass


def init():
	pass
