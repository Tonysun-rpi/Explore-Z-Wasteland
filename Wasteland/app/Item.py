# class for Items in game
class Item:
	def __init__(self, name, action, uid):
		self.name = name      # name of the item
		self.action = action  # function to be called on use
		self.uid = uid        # unique id for the item

	# return the image filename for the item
	def get_image_name(self):
		return self.name + '.png'

	# call the on-use function and return result
	def use(self):
		return self.action()

	# return the uid of the item
	def get_uid(self):
		return self.uid
