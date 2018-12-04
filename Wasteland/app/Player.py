import pygame


# class for player
class Player:
	def __init__(self):
		self.x_pos = 49
		self.y_pos = 49
		self.tile_size = 20
		self.is_moving = False
		self.speed = 1
		self.backpack = dict()
		self.rect = pygame.Rect(max(self.x_pos - 7, 0) * self.tile_size, min(self.y_pos - 7, 99) * self.tile_size, self.tile_size * 15, self.tile_size * 15)
		print(self.rect)

	def move_up(self):
		if self.y_pos > 0:
			self.y_pos -= 1
			self.rect.move_ip(0,-1 * self.tile_size)

	def move_down(self):
		if self.y_pos < 99:
			self.y_pos += 1
			self.rect.move_ip(0, 1 * self.tile_size)

	def move_left(self):
		if self.x_pos > 0:
			self.x_pos -= 1
			self.rect.move_ip(-1 * self.tile_size, 0)

	def move_right(self):
		if self.x_pos < 99:
			self.x_pos += 1
			self.rect.move_ip(1 * self.tile_size, 0)

	def get_pos(self):
		return self.x_pos, self.y_pos

	def get_area(self):
		return self.x_pos * self.tile_size, self.y_pos * self.tile_size, self.tile_size, self.tile_size

	def get_rect(self):
		return self.rect


if __name__ == "__init__":
	pass
