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
		self.rect = pygame.Rect(self.x_pos * self.tile_size, self.y_pos * self.tile_size, self.tile_size, self.tile_size)

	def move(self, direction):
		if direction == 'up' and self.y_pos > 0:
			self.y_pos -= 1
			self.rect.move_ip(0, -1)
		elif direction == 'down' and self.y_pos < 99:
			self.y_pos += 1
			self.rect.move_ip(0, 1)
		elif direction == 'left' and self.x_pos > 0:
			self.x_pos -= 1
			self.rect.move_ip(-1, 0)
		elif direction == 'right' and self.x_pos < 99:
			self.x_pos += 1
			self.rect.move_ip(1, 0)

	def get_pos(self):
		return self.x_pos, self.y_pos

	def getArea(self):
		return (self.x_pos * self.tile_size,self.y_pos * self.tile_size,self.tile_size,self.tile_size)

	def getRect(self):
		return self.rect


if __name__ == "__init__":
	pass
