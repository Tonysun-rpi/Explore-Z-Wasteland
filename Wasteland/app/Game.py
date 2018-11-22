import pygame
from app.Map import read_map,loadMapSurface
from app.Player import Player

class Game:
    def __init__(self):
        self.filename = "src/map.csv"
        # TODO: read config
        screen_size = (720,820)
        map_small_size = (450,450)
        # TODO: load data
        image_dict_str = {
            'f':'forest.jpg',   'g':'grassland.jpg',
            'p':'plain.jpg',    'mt':'mountain.jpg',
            'ml':'marshland.jpg', 'h':'hill.jpg',
            'i':'ice.jpg',      'sf':'snowfield.jpg',
            'sb':'snowberg.jpg','e':'exit.jpg',
            'w':'water.jpg',    'b1':'bridge_h.jpg',
            'b2':'bridge_v.jpg'
        }

        direct = 'img/'
        image_dict = {}
        for c,str in image_dict_str.items():
            image_dict[c] = pygame.image.load(direct+str)


        #initialize map
        self.map = read_map(self.filename)

        #initialize player
        self.player = Player()

        #initialize surfaces
        screen = pygame.display.set_mode(screen_size)
        map_surface = loadMapSurface(self.map,self.player.x_pos,self.player.y_pos,image_dict)
        map_surface = pygame.transform.scale(map_surface,map_small_size)
        screen.blit(map_surface,(0,0)+map_small_size)
        pygame.display.flip()




def initGame():
    return Game()