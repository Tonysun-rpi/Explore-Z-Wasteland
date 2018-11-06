from PIL import Image, ImageDraw


img_name = [
	'forest',
	'grassland',
	'marshland',
	'plain',
	'exit',
	'hill',
	'ice',
	'snowberg',
	'mountain',
	'snowfield',
	'water',
	'player'
]

# img = Image.open('./img/bridge_v.jpg')
# img = img.resize((48, 48), Image.ANTIALIAS)
# img.save('large_bridge_v.jpg')
#
# for item in img_name:
# 	filename = './img/' + item + '.png'
# 	im = Image.open(filename)
# 	rgb_im = im.convert('RGB')
# 	rgb_im.save('./img/' + item + '.jpg')


# my_map = ImageDraw.Draw(new_map)

x = 0
y = 0
with open('map.csv', 'r') as f:
	bg = Image.new('RGB', (4800, 4800), color=(255, 255, 255))
	lines = f.readlines()
	for line in lines:
		row = line.lower().strip().split(',')
		for item in row:
			temp = ''
			print(item)
			if item == 'g':
				temp = 'grassland'
			elif item == 'w':
				temp = 'water'
			elif item == 'mt':
				temp = 'mountain'
			elif item == 'h':
				temp = 'hill'
			elif item == 'p':
				temp = 'plain'
			elif item == 'f':
				temp = 'forest'
			elif item == 'i':
				temp = 'ice'
			elif item == 'sf':
				temp = 'snowfield'
			elif item == 'sb':
				temp = 'snowberg'
			elif item == 'ml':
				temp = 'marshland'
			elif item == 'e':
				temp = 'exit'
			elif item == 'b1':
				temp = 'bridge_h'
			elif item == 'b2':
				temp = 'bridge_v'
			print(item)

			img_name = './img/large_' + temp + '.jpg'
			img = Image.open(img_name, 'r')
			bg.paste(img, (x, y))

			x += 48
		x = 0
		y += 48
	bg.save('large_out_2.jpg')
