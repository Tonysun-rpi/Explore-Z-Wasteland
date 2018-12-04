import pygame
import sys
from app.Map import Map, read_map, obstacle
from app.Player import Player


class Game:
    def __init__(self):
        self.filename = "src/map.csv"
        # TODO: read config
        self.tile_size = 20
        self.screen_size = (720, 820)
        self.screen_player_size = (300, 300)
        self.screen_player_loc = (0, 0)
        self.screen_player_area = self.screen_player_loc + self.screen_player_size
        self.map_main_size = (100, 100)
        self.map_main_loc = (500, 500)
        self.map_main_area = self.map_main_loc + self.map_main_size
        self.player_area = (300 / 15 * 7, 300 / 15 * 7, 300 / 15, 300 / 15)

        # TODO: load data
        self.image_dict_str = {
            'f':'forest.jpg',     'g':'grassland.jpg',
            'p':'plain.jpg',      'mt':'mountain.jpg',
            'ml':'marshland.jpg', 'h':'hill.jpg',
            'i':'ice.jpg',        'sf':'snowfield.jpg',
            'sb':'snowberg.jpg',  'e':'exit.jpg',
            'w':'water.jpg',      'b1':'bridge_h.jpg',
            'b2':'bridge_v.jpg',  'player':'player.jpg'
        }

        self.direct = 'img/'
        self.image_dict = {}
        for c, img_filename in self.image_dict_str.items():
            self.image_dict[c] = pygame.image.load(self.direct + img_filename)

        # initialize map
        self.map = read_map(self.filename)

        # initialize player
        self.player = Player()

        # initialize screen
        self.screen = pygame.display.set_mode(self.screen_size)

        # initialize main map surface
        self.map_main_surface = self.map.to_surface(self.image_dict, self.tile_size)

        # initialize player map surface
        self.map_player_surface = self.map_main_surface.subsurface(self.player.get_rect())

        # initialize screen_player
        self.screen_player = pygame.transform.scale(self.map_player_surface, self.screen_player_size)

        # draw the player on screen_player
        self.screen_player.blit(self.image_dict['player'].convert(), self.player_area)

        # fill surfaces on the screen
        self.screen.blit(pygame.transform.scale(self.map_main_surface, self.map_main_size), self.map_main_area)
        self.screen.blit(self.screen_player, self.screen_player_area)

        pygame.display.flip()

        self.main_game_loop()

    def main_game_loop(self, disp_w=720, disp_h=820, tile_len=20, tile_num=15, mult=2.4):
        game_exit = False

        while not game_exit:
            player_map_update = False
            for event in pygame.event.get():
                print("Event")

                if event == pygame.QUIT:
                    game_exit = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_exit = True

                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        if not obstacle(self.map, max(self.player.y_pos - 1, 0), self.player.x_pos):

                            self.player.move_up()
                            player_map_update = True

                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        if not obstacle(self.map, min(self.player.y_pos + 1, 99), self.player.x_pos):
                            self.player.move_down()
                            player_map_update = True

                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        if not obstacle(self.map, self.player.y_pos, max(self.player.x_pos - 1, 0)):
                            self.player.move_left()
                            player_map_update = True

                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        if not obstacle(self.map, self.player.y_pos, min(self.player.x_pos + 1, 99)):
                            self.player.move_right()
                            player_map_update = True

                # if event.type == pygame.KEYUP:
                # 	if event.key == pygame.K_UP or event.key == pygame.K_w:
                # 		move_up = False
                #
                # 	if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                # 		move_down = False
                #
                # 	if event.key == pygame.K_LEFT or pygame.key == pygame.K_a:
                # 		move_left = False
                #
                # 	if event.key == pygame.K_RIGHT or pygame.key == pygame.K_d:
                # 		move_right = False

            # end of event handlers

            # begin drawing the canvas
            # TODO: add more canvas here

            # update the main surface
            if player_map_update:
                self.map_player_surface = self.map_main_surface.subsurface(self.player.get_rect())
                self.screen_player = pygame.transform.scale(self.map_player_surface, self.screen_player_size)
                self.screen_player.blit(self.image_dict['player'], self.player_area)
                self.screen.blit(pygame.transform.scale(self.screen_player, self.screen_player_size), self.screen_player_area)
                pygame.display.update(self.screen_player_area)

        if game_exit:
            pygame.quit()
            sys.exit()


def quit_game():
    pygame.quit()
    sys.exit()


def init_game():
    return Game()
