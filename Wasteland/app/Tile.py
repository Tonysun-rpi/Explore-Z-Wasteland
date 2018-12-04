# class for tiles
class Tile:
	def __init__(self, name, items=None, player_on=False, mob_on=False):
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


if __name__ == '__init__':
	pass
