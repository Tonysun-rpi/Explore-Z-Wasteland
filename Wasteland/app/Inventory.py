# class for character's inventory
class Inventory:
	def __init__(self):
		self.capacity = 100  # maximum capacity of the inventory
		self.items = list()  # use list to store the items. Can change to dict for quick searching
		self.used = 0        # keeps track of spaces used

	# add an item in the Inventory
	# return True if successfully added
	# return False if not
	def add_item(self, item):
		if self.used < self.capacity:
			self.items.append(item)
			self.used += 1
			return True
		else:
			return False

	# remove an item from Inventory by using uid
	# if found and removed, return True
	# if not, return False
	def del_item(self, target):
		temp_index = 0
		while temp_index < self.capacity:
			if self.items[temp_index].get_uid() == target:
				del self.items[temp_index]
				return True
			temp_index += 1

		return False

	# sort items in Inventory
	def sort_items(self):
		pass
