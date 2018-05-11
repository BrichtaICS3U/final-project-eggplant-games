import pygame, random

#Import classes
from hero import Hero, Enemy, Bullet

pygame.init()

def TEXT(TXT,x,y,TF):
    """this function exists to create headings for each menu screens"""

    fontTitle = pygame.font.Font('freesansbold.ttf', TF)
    textSurfaceTitle = fontTitle.render(TXT, True,M_TEXT)
    textRectTitle = textSurfaceTitle.get_rect()
    textRectTitle.center = (x,y)
    screen.blit(textSurfaceTitle,textRectTitle)

GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLUE = (81, 222, 232)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
M_TEXT = (164,44,214)
        
SCREENWIDTH=1250
SCREENHEIGHT=800
 
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Irrelevant")
shoot = True

#List containing all sprites 
all_sprites_list = pygame.sprite.Group()

#Other sprite lists
enemy_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()

#Create Hero, enemy, bullet
player = Hero(30, 50)
player.rect.x = 200
player.rect.y = 300
playerHealth = player.HP

enemy = Enemy(BLACK, 40, 40)
enemy_list.add(enemy)

bullet = Bullet(BLACK, 5, 5, player.rect.x, player.rect.y)
 
# Add sprites to list of sprites
all_sprites_list.add(player)
all_sprites_list.add(enemy)

#Set shoot = False for later
shoot = False

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
        if keys[pygame.K_d]:
            player.move()
        if keys[pygame.K_w]:
            player.move()
        if keys[pygame.K_s]:
           player.move()

        #Player Sprint
        if keys[pygame.K_LSHIFT]:
            if keys[pygame.K_a]:
                player.sprint()
            elif keys[pygame.K_d]:
                player.sprint()
            elif keys[pygame.K_w]:
                player.sprint()
            elif keys[pygame.K_s]:
                player.sprint()
                    
        #Enemy follow player
        enemy.move_to_player(player)
                
        #Player shooting
        if event.type==pygame.MOUSEBUTTONDOWN and shoot == True:
                bullet = Bullet(BLACK,5,5,player.rect.x ,player.rect.y)
                shoot = False
                all_sprites_list.add(bullet)
                bullet_list.add(bullet)
                
        #this allows the player to shoot again when he/she releases the mouse button        
        if event.type==pygame.MOUSEBUTTONUP:
            shoot = True
                        
        #Game Logic
        all_sprites_list.update()
        collision_list = pygame.sprite.spritecollide(player, enemy_list, False)
        bullet_collision = pygame.sprite.spritecollide(bullet, enemy_list, False)
        
        #Drawing on Screen
        screen.fill(WHITE)
        pygame.draw.rect(screen, GREEN, [20, 30, 15, 25], 0) #Draw player health bars
        pygame.draw.rect(screen, GREEN, [40, 30, 15, 25], 0)
        pygame.draw.rect(screen, GREEN, [60, 30, 15, 25], 0)
        pygame.draw.rect(screen, GREEN, [80, 30, 15, 25], 0)
        pygame.draw.rect(screen, GREEN, [100, 30, 15, 25], 0)
        TEXT("Player Health", 60, 20, 15)
        pygame.draw.rect(screen, RED, [enemy.rect.x+5, enemy.rect.y-10, 30, 5], 0)  #Enemy health bar

        #Updating health bars
        for collision in collision_list:
            player.HP -= 20
            print(player.HP)
            player.rect.x -= 100  ###### Adjust later
            player.rect.y -= 50

        for collision in bullet_collision:
            enemy.HP -= 5
            print(enemy.HP)

        # This draws white (alternatively other background colour) over
        # original health bars to simulate the bars disappearing
            #Player health bars
        if player.HP <= 80:
            pygame.draw.rect(screen, WHITE, [100, 30, 15, 25], 0)
            if player.HP <= 60:
                pygame.draw.rect(screen, WHITE, [80, 30, 15, 25], 0)
                if player.HP <= 40:
                    pygame.draw.rect(screen, WHITE, [60, 30, 15, 25], 0)
                if player.HP <= 20:
                    pygame.draw.rect(screen, WHITE, [40, 30, 15, 25], 0)
                if player.HP == 0:
                    pygame.draw.rect(screen, WHITE, [20, 30, 15, 25], 0)
                    player.die()
                    carryOn = False
                #Enemy health bar
        if enemy.HP <= 80:
            pygame.draw.rect(screen, WHITE, [enemy.rect.x+29, enemy.rect.y-10, 6, 5], 0)
            if enemy.HP <= 60:
                pygame.draw.rect(screen, WHITE, [enemy.rect.x+23, enemy.rect.y-10, 6, 5], 0)
                if enemy.HP <= 40:
                    pygame.draw.rect(screen, WHITE, [enemy.rect.x+17, enemy.rect.y-10, 6, 5], 0)
                if enemy.HP <= 20:
                    pygame.draw.rect(screen, WHITE, [enemy.rect.x+11, enemy.rect.y-10, 6, 5], 0)
                if enemy.HP <= 0:
                    pygame.draw.rect(screen, WHITE, [enemy.rect.x+5, enemy.rect.y-10, 10, 5], 0)
                    all_sprites_list.remove(enemy)
                    enemy_list.remove(enemy)
                    ##### FIND WAY TO REMOVE ENEMY FROM GAME ENTIRELY

        
        #wall restrictions
        #Right wall
        if player.rect.x + 30 > SCREENWIDTH:
            player.rect.x -= 2
            if keys[pygame.K_LSHIFT]:
                player.rect.x -= 2
        #Left wall
        elif player.rect.x < 0:
            player.rect.x += 2
            if keys[pygame.K_LSHIFT]:
                player.rect.x += 2
        #top wall
        elif player.rect.y < 0:
            player.rect.y += 2
            if keys[pygame.K_LSHIFT]:
                player.rect.y += 2
        #Bottom wall
        elif player.rect.y + 40 > SCREENHEIGHT:
            player.rect.y -= 2
            if keys[pygame.K_LSHIFT]:
                player.rect.y -= 2

        
        #Draw all the sprites
        all_sprites_list.draw(screen)
 
        #Refresh Screen
        pygame.display.flip()
 
        #Number of frames per secong e.g. 60
        clock.tick(60)
 
pygame.quit()
