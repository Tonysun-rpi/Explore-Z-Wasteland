import pygame
import time
import sqlite3
from app.Player import Player
from app.Tile import Tile


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (200, 0, 0)
BRIGHT_RED = (255, 0, 0)
GREEN = (0, 200, 0)
BRIGHT_GREEN = (0, 255, 0)
BLUE = (0, 0, 200)
BRIGHT_BLUE = (0, 0, 255)


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


def init():
	pass
