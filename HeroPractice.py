import pygame, random

#Import classes
from hero import Hero
from hero import Enemy
pygame.init()
 
GREEN = (20, 255, 140)
GREY = (210, 210 ,210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 251, 36)
BLUE = (81, 222, 232)
BLACK = (0, 0, 0)
        
SCREENWIDTH=1250
SCREENHEIGHT=800
 
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Irrelevant")
#List containing all sprites 
all_sprites_list = pygame.sprite.Group()
 
player = Hero(30, 50)
player.rect.x = 200
player.rect.y = 300

enemy_list = pygame.sprite.Group()
enemy = Enemy(BLACK, 40, 40)
 
# Add the car to the list of objects
all_sprites_list.add(player)
enemy_list.add(enemy)
 
#Allowing the user to close the window...
carryOn = True
clock=pygame.time.Clock()
 
while carryOn:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                carryOn=False
         
        keys = pygame.key.get_pressed()
        #Player Move
        if keys[pygame.K_a]:
            player.move()
            enemy.move_to_player(player)
        if keys[pygame.K_d]:
            player.move()
            enemy.move_to_player(player)
        if keys[pygame.K_w]:
            player.move()
            enemy.move_to_player(player)
        if keys[pygame.K_s]:
           player.move()
           enemy.move_to_player(player)

        #Player Sprint
        if keys[pygame.K_LSHIFT]:
                if keys[pygame.K_a]:
                    player.sprint()
                    enemy.move_to_player(player)
                elif keys[pygame.K_d]:
                    player.sprint()
                    enemy.move_to_player(player)
                elif keys[pygame.K_w]:
                    player.sprint()
                    enemy.move_to_player(player)
                elif keys[pygame.K_s]:
                    player.sprint()
                    enemy.move_to_player(player)

        #If enemy hits player
        collision_list = pygame.sprite.spritecollide(player, enemy_list, False)
        for collision in collision_list:
            player.die()


        #Game Logic
        all_sprites_list.update()
        enemy_list.update()
 
        #Drawing on Screen
        screen.fill(WHITE)
        
        #Draw all the sprites
        all_sprites_list.draw(screen)
        enemy_list.draw(screen)
 
        #Refresh Screen
        pygame.display.flip()
 
        #Number of frames per secong e.g. 60
        clock.tick(60)
 
pygame.quit()
