import pygame, sys, time
from random import randint

#Game Variables
gravity = 0.001
char_ymovement = 0
char_xmovement = 0
char_xpos = 250 
game_active = True

class back: 
    bg_y_pos = 0 
    def __init__(self,size ) :
        self.size = size
    @classmethod
    def draw_bg(cls):
        cls.bg_y_pos+=1
        screen.blit(bg_surface,(0,cls.bg_y_pos))
        screen.blit(bg_surface,(0,cls.bg_y_pos - 700))

class tilemaker:
    def __init__(self) :
         self.tile_list = []
    @staticmethod
    def create_tile(randpos):
        x=randint(10,randpos)
        new_tile = tile.get_rect(center = (x,0))
        return new_tile
    @staticmethod
    def move_tiles(tiles):
        for t in tiles:
            t.centery += 1
        return tiles
    @staticmethod
    def draw_tiles(tiles):
        for t in tiles:
            screen.blit(tile,t)
    @staticmethod
    def check_collision(tile_list):
        for t in tile_list:
            if char_rect.colliderect(t):
                char_ymovement -= 0.001
    @staticmethod
    def game_over():
        if char_rect.top >=700:
            return False
        return True

pygame.init()
clock = pygame.time.Clock()




bg1 = back((500,700))
screen = pygame.display.set_mode(bg1.size)
bg_surface = pygame.image.load('assets/bg.png').convert()#convert is good as it helps python to run code faster


char = pygame.image.load('assets/player.png')
char = pygame.transform.scale(char, (50,50))

char_rect = char.get_rect(center = (250,400))#Rect func creates a rectangle around the char. When this rect comes in contact with another rect we can know


tile = pygame.image.load('assets/tile.png')
tile = pygame.transform.scale(tile, (60,15))#Resize
tiling = tilemaker()


SPAWNTILE = pygame.USEREVENT
pygame.time.set_timer(SPAWNTILE,1100)



while True:#game loop
    screen.blit(bg_surface,(0,0))#Now it puts the bg surface at the coordinates mentioned
    for event in pygame.event.get():#Pygame tries to find events. Example moving mouse,closing screen,etc.
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()#Quits Pygame by pressing x

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                char_xmovement = 0
                char_xmovement -= 1
                char_xpos -= 1
            if event.key == pygame.K_RIGHT:
                char_xmovement = 0
                char_xmovement += 1
                char_xpos += 1
        
        if event.type == SPAWNTILE:
            tiling.tile_list.append(tiling.create_tile(500))


    screen.blit(char,char_rect)


    if game_active:
        
        
        bg1.bg_y_pos += 1
        bg1.draw_bg()
        if bg1.bg_y_pos>=700:
            bg1.bg_y_pos=0

        # char_ymovement += gravity
        char_rect.centery += char_ymovement
        char_rect.centerx += char_xmovement
        game_active = tiling.game_over()
        

        screen.blit(char,char_rect)

        #tiles
        tile_list = tiling.move_tiles(tiling.tile_list)
        tiling.draw_tiles(tile_list)
        char_ymovement=0
 
        for t in tile_list:
            if char_rect.colliderect(t):
                
                char_ymovement -= 0.001

        if char_rect.centerx >= 500 : 
            char_rect.centerx -= 2
        if char_rect.centerx <= 0 : 
            char_rect.centerx += 2
        if char_rect.centery >= 0 : 
            char_rect.centerx -= 2
        if char_rect.centery <= 700 : 
            char_rect.centerx += 2
        pygame.display.update()
        clock.tick(100)
char_rect.centery
#38:49 keep in mind when doing gravity
