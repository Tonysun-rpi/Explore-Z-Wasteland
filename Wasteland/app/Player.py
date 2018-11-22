# class for player
class Player:
	def __init__(self):
		self.x_pos = 70
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


if __name__ == "__init__":
	pass
