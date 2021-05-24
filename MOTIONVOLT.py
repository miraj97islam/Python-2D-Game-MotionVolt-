
import pygame
from pygame.locals import *
import os
import sys
import math
import random

pygame.init()               #initial pygame

w_background = 1024   #background width
h_bacground = 512       #background height

resolution = (w_background, h_bacground)
window = pygame.display.set_mode(resolution)              #set the display window
background = pygame.image.load("background.png")          #load the background image
background1_X = 0
background2_X = background.get_width()


pygame.display.set_caption("MotionVolt")                #set the display caption
icon = pygame.image.load("icon.png")                    #load the display icon
pygame.display.set_icon(icon)                           #set the display icon

"""CLASS FOR MAIN CHARACTER"""
class player(object):
    """lOAD THE IMAGES OF THE MAIN CHARACTER"""
    character = [pygame.image.load("character_Right.png"), pygame.image.load("character_Left.png")]
    run_right = [pygame.image.load("run_right_3.png"), pygame.image.load("run_right_4.png"),
                 pygame.image.load("run_right_5.png"), pygame.image.load("run_right_7.png"),
                 pygame.image.load("run_right_8.png")]
    run_left = [pygame.image.load("character_Left.png"), pygame.image.load("run_left_1.png"),
                 pygame.image.load("run_left_2.png"), pygame.image.load("run_left_3.png"),
                pygame.image.load("run_left_4.png"), pygame.image.load("run_left_5.png"),
                pygame.image.load("run_left_6.png"), pygame.image.load("run_left_7.png"),
                pygame.image.load("run_left_8.png")]

    """INITIALIZE THE VARIABLES AND FUNCTION PARAMETERS"""
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.jumping = False
        self.sliding = False
        self.falling = False
        self.slideUp = False
        self.Left = False
        self.Right = False
        self.jumpCount = 10
        self.rotatcount = 0
        self.slideCount = 0
        self.walkCount = 0
        self.velocity = 5
        self.standing = True
        self.negative = 1
        self.hitbox = (self.x + 20, self.y + 10, 40, 115)

    """DRAW FUNCTION TO DRAW THE MAIN CHARACTER ON THE WINDOW AND DEFINE HOW IT MOVES"""
    def draw(self, window):
        if self.standing:
            window.blit(self.character[0], (self.x, self.y))   #SET THE PICTURE FOR STANDING POSITION

        keys = pygame.key.get_pressed()             #TAKE THE VALUE FOR KEYBOARD

        if not (self.standing):

            if self.Left:
                window.blit(self.character[1], (self.x, self.y))   #SET THE PICTURE FOR LEFT FACE POSITION

            elif self.Right:
                window.blit((self.character[0]), (self.x, self.y))  #SET THE PICTURE FOR RIGHT FACE POSITION

        else:
            if self.Right:
                window.blit(self.character[0], (self.x, self.y))  # whlie character is idle
            else:
                window.blit(self.character[0], (self.x, self.y))  # whlie character is idle

        self.hitbox = (self.x + 20, self.y + 10, 40, 115)


    """COLLIDE FUNCTION FOR COLLSION BETWEEN THE CHARACTER AND OBJECTS """
    def collide(self):
        if self.x > 110:
            self.x = self.x - 100
        if self.x < 110:
            self.x += 100
        # self.y = self.y
        self.walkCount = 0
        font1 = pygame.font.SysFont("comicsans", 100)
        text = font1.render("-10", 1, (255, 0, 0))             # "10" FONT APPEAR WILE COLLISION
        window.blit(text, (500, 5))                            # X AND Y AXIS VALUE WHERE "-10" FONT APPEAR
        pygame.display.update()
        i = 0
        while i < 50:
            pygame.time.delay(10)                   #DELAY TIME TO SHOW THE "-10" FONT
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()                   #QUIT FROM THE DELAY AND BACK TO THE NORMAL DISPLAY

    """FALL_1 FUNCTION FOR LEVEL_1 GAME OVER """
    def fall_1(self):
        global obstacles, background1_X, background2_X, score, heart, game_over_music,lvl1_music, lvl2_music  #CALL GLOBAL VARIABLES
        self.falling = True
        if self.falling:
            for obstacle in obstacles:
                if obstacle.x < 1111:
                    obstacles.pop(obstacles.index(obstacle))    #OBJECTECTS DISAPPEAR AFTER 1111 AXIS
                for bullet in bullets:
                # if bullet.x < 1024 and bullet.x > 0:
                    bullet.x = 1030
                # bullets.pop(bullets.index(bullet))
          #  window.blit(self.falling_load(10, 20))
            level_up_sound.stop()                   #SOUNDS AND MUSIC GET MUTE
            lvl1_music.stop()
            lvl2_music.stop()
            game_over_music.play()
            self.jumping = False                    #ALL THE ACTIVITY OF THE CHARACTER BECOME FALSE
            self.sliding = False
            self.slideUp = False
            self.Left = False
            self.Right = False
            self.standing = True
            enemy1_1.velocity = 0                   #ALL THE VELOCITY BECOME ZERO
            object1.velocity = 0
            bird1_1.velocity = 0
            first_aid.velocity = 0
            flag_port.velocity = 0
            funny.velocity = 0
            funny.rotatcount = 0

            bird1_1.rotatcount = 0
            score = 0
            heart = 0
            font1 = pygame.font.SysFont("comicsans", 100)
            text = font1.render("GAME OVER", 1, (255, 0, 0))            # "GAME OVER" FONT APPEAR IN THE WINDOW
            window.blit(text, (300, 50))
            pygame.display.update()

        background1_X = 0                            #BACKGROUND STOP BEING LOOPING
        background2_X = 0

    """FALL_1 FUNCTION FOR LEVEL_2 GAME OVER """
    def fall_2(self):
        global obstacles, background1_X, background2_X, score, heart, game_over_music,lvl1_music, lvl2_music   #CALL GLOBAL VARIABLES
        self.falling = True
        if self.falling:

          #  window.blit(self.falling_load(10, 20))
            lvl1_music.stop()
            lvl2_music.stop()
            game_over_music.play()

            self.jumping = False
            self.sliding = False
            self.slideUp = False
            self.Left = False
            self.Right = False
            self.standing = True
            enemy2_2.velocity = 0
            object2.velocity = 0
            bird2_2.velocity = 0
            first_aid.velocity = 0
            flag_port.velocity = 0
            flag_port2.velocity = 0
            funny.velocity = 0
            first_aid.velocity = 0

            for obstacle in obstacles:
                if obstacle.x < 1111:
                    obstacles.pop(obstacles.index(obstacle))                #OBJECTECTS DISAPPEAR AFTER 1111 AXIS
            for bullet in bullets:
                  bullet.x = 1030                 # bullets.pop(bullets.index(bullet))
            bird2_2.rotatcount = 0
            score = 0
            heart = 0
            font1 = pygame.font.SysFont("comicsans", 100)
            text = font1.render("GAME OVER", 1, (255, 0, 0))
            window.blit(text, (300, 50))
            pygame.display.update()

        background1_X = 0  # define background loop which way
        background2_X = 0

    def winn(self):
        global obstacles, background1_X, background2_X, score, heart, lvl1_music, lvl2_music
        lvl2_music.stop()               #SOUNDS AND MUSIC GET MUTE
        lvl1_music.stop()
        self.jumping = False            #ALL THE ACTIVITY OF THE CHARACTER BECOME FALSE
        self.sliding = False
        self.slideUp = False
        self.Left = False
        self.Right = False
        self.standing = True
        self.velocity = 0                #ALL THE VELOCITY BECOME ZERO
        enemy2_2.velocity = 0
        object2.velocity = 0
        bird2_2.velocity = 0
        first_aid.velocity = 0
        flag_port2.velocity = 0
        funny.velocity = 0
        enemy2_2.rotatcount = 0

        for obstacle in obstacles:
            if obstacle.x < 1111:
                obstacles.pop(obstacles.index(obstacle))
        for bullet in bullets:
            # if bullet.x < 1024 and bullet.x > 0:
            bullet.x = 1030  # bullets.pop(bullets.index(bullet))
        bird2_2.rotatcount = 0
        score = 0
        heart = 0
        font1 = pygame.font.SysFont("comicsans", 100)
        text = font1.render("WINNER!", 1, (255, 0, 0))      # "WINNER!" FONT APPEAR IN THE WINDOW
        window.blit(text, (400, 50))
        pygame.display.update()
        background1_X = 0  #BACKGROUND STOP BEING LOOPING
        background2_X = 0


"""LVL1_ENEMY FUNCTION IS FOR LEVEL_1 ENEMY"""
class lvl1_enemy(object):
    enemy_load = [pygame.image.load("enenmy01_Right.png"), pygame.image.load("enenmy01_Left.png")]   #LOAD THE ENEMY IMAGES

    """INITIALIZE ALL THE VARIABLES INSIDE THE FUCTION"""
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 3
        self.walkCount = 0
        self.path0 = 0
        self.path1 = 950
        self.path_enemy = (self.path0, self.path1)
        self.rotatcount = 0
        self.hitbox = (self.x + 10, self.y + 10, 40, 100)
        self.health = 10
        self.visible = True
        self.collide = False
        self.lvl1 = True

    """DRAW FUNCITON TO DRAW THE ENEMY AND DEFINE HOW IT BEHAVE"""
    def draw(self, window):
        if self.lvl1 == True:                 #ALL THE CONDITIONS WORK IF LEVEL 1 IS TRUE
            if self.visible == True:

                if self.velocity > 0:

                    if self.x + self.velocity < self.path_enemy[1]:
                        self.x += self.velocity          #VELOCITY INCREASES WHILE INSIDE THE SPECIFIC AXIS
                    else:
                        self.velocity = self.velocity * -1
                        self.walkCount = 0
                    # self.path1 -= 50
                else:
                    if self.x - self.velocity > self.path_enemy[0]:
                        self.x += self.velocity
                    else:
                        self.velocity = self.velocity * -1
                        self.walkCount = 0
                        # self.path0 -= 50

                if self.walkCount + 1 >= 33:
                    self.walkCount = 0

                if self.velocity > 0:
                    window.blit(self.enemy_load[0], (self.x, self.y))  # enemy[0] ===== enemy_Right
                    self.walkCount += 1  # enemy[1] ===== enemy_Left
                else:
                    window.blit(self.enemy_load[1], (self.x, self.y))
                    self.walkCount += 1
                pygame.draw.rect(window, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))  # CREATE THE HEALTH BAR FOR ENEMY
                pygame.draw.rect(window, (0, 128, 0),
                                 (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
                self.hitbox = (self.x + 10, self.y + 10, 40, 100)           #CREATE THE HITBOX FOR COLLISION
            #pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)
    """HIT FUNCTION FOR ENEMY"""
    def hit(self):
        if self.health > 0:
            self.health -= 1        #ENEMY HEALTH DECREAS WHILE GET SHOT
        if self.health <= 0:
            self.visible = False    #ENEMY DISAPPEAR IF GET 10 SHOT
            self.health = 10


"""LVL1_ENEMY FUNCTION IS FOR LEVEL_2 ENEMY"""
class lvl2_enemy(object):
    enemy_left = [pygame.image.load("Attack_left_5.png"), pygame.image.load("Attack_left_6.png"), pygame.image.load("Attack_left_7.png")]
                                                                                                                                    #LOAD THE ENEMY IMAGES
    enemy_right = [pygame.image.load("Attack_right_5.png"), pygame.image.load("Attack_right_6.png"), pygame.image.load("Attack_right_7.png")]

    """INITIALIZE ALL THE VARIABLES INSIDE THE FUCTION"""
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 4.4
        self.walkCount = 0
        self.path0 = 0
        self.path1 = 950
        self.path_enemy = (self.path0, self.path1)
        self.rotatcount = 0
        self.hitbox = (self.x + 10, self.y + 10, 70, 100)
        self.health = 10
        self.visible = False
        # self.delay = pygame.time.set_timer(USEREVENT, 10000)
        self.collide = False
        self.lvl2 = False

    def draw(self, window):
        if self.lvl2 == True:               #ALL THE CONDITIONS WORK IF LEVEL 1 IS TRUE
            if self.visible == True:
                if self.velocity > 0:
                    if self.x + self.velocity < self.path_enemy[1]:
                        self.x += self.velocity                  #VELOCITY INCREASES WHILE INSIDE THE SPECIFIC AXIS
                    else:
                        self.velocity = self.velocity * -1
                        self.walkCount = 0
                    # self.path1 -= 50
                else:
                    if self.x - self.velocity > self.path_enemy[0]:
                        self.x += self.velocity
                    else:
                        self.velocity = self.velocity * -1
                        self.walkCount = 0
                        # self.path0 -= 50

                if self.walkCount + 1 >= 33:
                    self.walkCount = 0

                if self.rotatcount >= 3:
                    self.rotatcount = 0

                if self.velocity > 0:
                    #window.blit(self.enemy_load[0], (self.x, self.y))  # enemy[0] ===== enemy_Right
                    window.blit(self.enemy_right[self.rotatcount], (self.x, self.y))
                    self.rotatcount += 1
                    self.walkCount += 1  # enemy[1] ===== enemy_Left
                else:
                   # window.blit(self.enemy_load[1], (self.x, self.y))
                    window.blit(self.enemy_left[self.rotatcount//2], (self.x, self.y))
                    self.rotatcount += 1
                    self.walkCount += 1

                pygame.draw.rect(window, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))            # CREATE THE HEALTH BAR FOR ENEMY
                pygame.draw.rect(window, (0, 128, 0),
                                 (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
                self.hitbox = (self.x +10, self.y + 30, 55, 80)                  #CREATE THE HITBOX FOR COLLISION
               # pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if self.health > 0:
            self.health -= 1         #ENEMY HEALTH DECREAS WHILE GET SHOT
        if self.health <= 0:
            self.visible = False        #ENEMY DISAPPEAR IF GET 10 SHOT
            self.health = 10


"""FOR OBSTACLE IN LEVEL 1"""
class lvl1_rock(object):
    rock_load = pygame.image.load("Crate.png")    #LOAD THE OBSTACLE IMAGE

    """INITIALIZE ALL THE VARIABLES"""
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.visible = True
        self.velocity = 1.5
        self.hitbox = (self.x, self.y + 10, self.width, self.height)
        self.lvl1 = True

    """DRAW FUNCTION TO DRAW TO OBSTACLE"""
    def draw(self, window):
        if self.lvl1 == True:        #WORKS IF LEVEL 1

            if self.visible == True:
                self.hitbox = (self.x, self.y, self.width, self.height)  #CREATE HITBOX FOR COLLISION
                #pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)
                window.blit(self.rock_load, (self.x, self.y))     #PUT THE IMAGE IN SPECIFIC AXIS

                if self.velocity > 0:
                    self.x -= self.velocity         #TO MOVE RIGHT TO LEFT
            if self.x < -350:
                self.x = 1000                       #APPEAR IN 1000 AXIS

    """FUNCTION FOR COLLISION"""
    def collide(self, rect):
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] + rect[3] > self.hitbox[1]:
                return True
        return False


"""FOR OBSTACLE IN LEVEL 1"""
class lvl2_rock(object):
    rock_load = pygame.image.load("DeadBush.png")            #LOAD THE OBSTACLE IMAGE

    """INITIALIZE ALL THE VARIABLES"""
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.visible = False
        self.velocity = 1.5
        self.hitbox = (self.x, self.y + 10, self.width, self.height)
        self.lvl2 = False

    """DRAW FUNCTION TO DRAW TO OBSTACLE"""
    def draw(self, window):
        if self.lvl2 == True:                #WORKS IF LEVEL 2

            if self.visible == True:
                self.hitbox = (self.x+20, self.y, self.width, self.height)     #CREATE HITBOX FOR COLLISION
                #pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)
                window.blit(self.rock_load, (self.x, self.y))                    #PUT THE IMAGE IN SPECIFIC AXIS

                if self.velocity > 0:
                    self.x -= self.velocity             #TO MOVE RIGHT TO LEFT
            if self.x < -350:
                self.x = 1000               #APPEAR IN 1000 AXIS

    """FUNCTION FOR COLLISION"""
    def collide(self, rect):
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] + rect[3] > self.hitbox[1]:
                return True
        return False


"""FOR CLOUD IN THE BACKGROUND"""
class cloud(lvl1_rock):
    cloud_load = pygame.image.load("cloud.png")   #LOAD THE IMAGE

    def draw(self, window):
        window.blit(self.cloud_load, (self.x, self.y))   #BLIT THE IMAGE IN THE SPECIFIC AXIS


"""FOR FIRST AID"""
class aid(object):
    first_aid_load = pygame.image.load("first_aid.png")    #LOAD THE IMAGE

    """INITIALIZE ALL THE VARIABLES"""
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 4
        self.visible = True
        self.hitbox = (self.x, self.y + 10, self.width, self.height)

    """DRAW FUNCTION TO DRAW AT THE WINDOW"""
    def draw(self, window):
        self.hitbox = (self.x, self.y + 10, self.width, self.height)   #CREATE HITBOX FOR COLLISION
        #pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)
        window.blit(self.first_aid_load, (self.x, self.y))

        if self.visible == True:

            if self.velocity > 0:
                self.x -= self.velocity             #GO RIGHT TO LEFT WHILE APPEAR

class flag(object):
    flag_load = pygame.image.load("ArrowSign.png")   #LOAD THE IMAGE

    """INITIALIZE ALL THE VARIABLES"""
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 1.5
        self.visible = True
        self.hitbox = (self.x, self.y + 10, self.width, self.height)

    """DRAW FUNCTION TO DRAW AT THE WINDOW"""
    def draw(self, window):
        self.hitbox = (self.x, self.y - 100, self.width, self.height+100)    #CREATE HITBOX FOR COLLISION
        #pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)
        window.blit(self.flag_load, (self.x, self.y))

        if self.visible == True:

            if self.velocity > 0:
                self.x -= self.velocity         #GO RIGHT TO LEFT WHILE APPEAR


"""FOR FINAL DESTINATION OF LEVEL 1"""
class flag2(object):
    flag_load = pygame.image.load("ArrowSign.png")      #LOAD THE IMAGE

    """INITIALIZE ALL THE VARIABLES"""
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 1.5
        self.visible = True
        self.lvl2 = False
        self.hitbox = (self.x, self.y + 10, self.width, self.height)

    """DRAW FUNCTION TO DRAW AT THE WINDOW"""
    def draw(self, window):
        if self.lvl2 == True:
            self.hitbox = (self.x, self.y - 100, self.width, self.height+100)        #CREATE HITBOX FOR COLLISION
            #pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)
            window.blit(self.flag_load, (self.x, self.y))

            if self.visible == True:

                if self.velocity > 0:
                    self.x -= self.velocity                 #GO RIGHT TO LEFT WHILE APPEAR


"""FOR FLYING ENEMY OF LEVEL 1"""
class lvl1_bird(object):
    bird1 = [pygame.image.load("PICTURE1.png"), pygame.image.load("PICTURE2.png"), pygame.image.load("PICTURE3.png"),
             pygame.image.load("PICTURE4.png")]             #LOAD IMAGES

    """INITIALIZE ALL THE VARIABLES"""
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rotatcount = 0
        self.walkCount = 0
        self.velocity = .5
        self.path0 = 0
        self.path1 = 950
        self.path_enemy = (self.path0, self.path1)
        self.health = 10
        self.visible = True
        self.delay = pygame.time.set_timer(USEREVENT, 10000)
        self.collide = False
        self.hitbox = (self.x, self.y + 15, self.width, 50)
        self.lvl1 = True

    """FUNCTION TO DRAW THE ENEMY AND DEFINE HOW IT BEHAVE"""
    def draw(self, window):

        if self.lvl1 == True:           #WORK IF LEVEL 1
            if self.rotatcount >= 8:
                self.rotatcount = 0
            window.blit(pygame.transform.scale(self.bird1[self.rotatcount // 2], (122, 68)), (self.x, self.y))
            self.rotatcount += 1        #COMBINE MULTIPLE IMAGES TO VUSUALISE BIRD FLYING

            if self.visible == True:

                if self.velocity > 0:
                    self.x -= self.velocity     #GO RIGHT TO LEFT WHILW APPEAR

            # pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)
            pygame.draw.rect(window, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 30, 50, 10))  #HEALTH BAR OF THE ENEMY
            pygame.draw.rect(window, (0, 128, 0),
                             (self.hitbox[0], self.hitbox[1] - 30, 50 - (5 * (10 - self.health)), 10))
            self.hitbox = (self.x, self.y + 15, 100, 50)           #CREATE HITBOX FOR COLLISION

    """FOR COLLISION"""
    def hit(self):
        if self.health > 0:
            self.health -= 2        #ENEMY HEALTH DECREASE
        if self.health <= 0:
            self.visible = False     #ENEMY DISAPPEAR
            self.health = 10

"""FOR FLYING ENEMY OF LEVEL 2"""
class lvl2_bird(object):
    bird1 = [pygame.image.load("airplane_1.png"), pygame.image.load("airplane_2.png"), pygame.image.load("airplane_3.png"),pygame.image.load("airplane_4.png")] # LOAD IMAGES

    """INITIALIZE ALL THE VARIABLES"""
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rotatcount = 0
        self.walkCount = 0
        self.velocity = .9
        self.path0 = 0
        self.path1 = 950
        self.path_enemy = (self.path0, self.path1)
        self.health = 10
        self.visible = False
        self.delay = pygame.time.set_timer(USEREVENT, 10000)
        self.collide = False
        self.hitbox = (self.x, self.y + 15, self.width, 50)
        self.lvl2 = False

    """FUNCTION TO DRAW THE ENEMY AND DEFINE HOW IT BEHAVE"""
    def draw(self, window):
        if self.lvl2 == True:           #WORK IF LEVEL 1
            if self.rotatcount >= 8:
                self.rotatcount = 0
            window.blit(pygame.transform.scale(self.bird1[self.rotatcount // 2], (140, 90)), (self.x, self.y-30))
            self.rotatcount += 1            #COMBINE MULTIPLE IMAGES TO VUSUALISE BIRD FLYING

            if self.visible == True:

                if self.velocity > 0:
                    self.x -= self.velocity     #GO RIGHT TO LEFT WHILW APPEAR

            pygame.draw.rect(window, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 30, 50, 10))         #HEALTH BAR OF THE ENEMY
            pygame.draw.rect(window, (0, 128, 0),
                             (self.hitbox[0], self.hitbox[1] - 30, 50 - (5 * (10 - self.health)), 10))
            self.hitbox = (self.x, self.y -10, 100, 70)          #CREATE HITBOX FOR COLLISION
           # pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)

    """FOR COLLISION"""
    def hit(self):
        if self.health > 0:
            self.health -= 2        #ENEMY HEALTH DECREASE
        if self.health <= 0:
            self.visible = False     #ENEMY DISAPPEAR
            self.health = 10


"""FOR BACKGORUND BIRD"""
class funny_bird(object):

    bird_load = [pygame.image.load("funny_bird_1.png"), pygame.image.load("funny_bird_2.png"), pygame.image.load("funny_bird_3.png"), pygame.image.load("funny_bird_4.png")]  #LOAD IMAGE

    """INITIALIZE ALL THE VARIABLES"""
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rotatcount = 0
        self.velocity = 2
        self.visible = True
        self.delay = pygame.time.set_timer(USEREVENT, 10000)

    """TO DRAW AT THE WINDOW"""
    def draw(self, window):
        if self.rotatcount >= 8:    #COMBINE MULTIPLE IMAGES TO VISUALISE FLYING BIRD
            self.rotatcount = 0
        window.blit(pygame.transform.scale(self.bird_load[self.rotatcount // 2], (140, 90)), (self.x, self.y))
        self.rotatcount += 1

        if self.visible == True:

            if self.velocity > 0:
                self.x -= self.velocity         #MOVE RIGHT TO LEFT WHILE APPEAR

            if self.x < -350:
                self.x = 1000           #APPEAR AT AXIS 1000


"""FINCTION FOR BULLET """
class tile(object):
    """INITIALIZE ALL THE VARIABLES"""
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 12* facing

    """FUNCTION TO DRAW"""
    def draw(self, win):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)


def endScreen():
    global pause, score, speed, obstacles

    obstacles = []
    run = True
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False
                runner.falling = False
                runner.sliding = False
                runner.jumpin = False
        window.blit(background, (0, 0))


"""FUNCTION FOR MUSIC AND SOUND"""
def load_sound(sound_filename):
    sound = pygame.mixer.Sound(sound_filename)
    return sound


"""FUNCTION FOR GLOBAL VARIABLES TO DRAW AT WINDOW PURPOSE"""
def redrwWindow():
    window.blit(background, (background1_X, 0))  # to make background continuous
    window.blit(background, (background2_X, 0))  # to make background continuous
    sun_load = pygame.image.load("sun3.png")     #LOAD SUN AT THE WINDOW
    window.blit(sun_load, (750, -160, 500, 500))  #SPECIFIC AXIS FOR SUN

    text = font.render("Score:  " + str(score), 1, (255, 0, 0))   #TO SHOW SCORE
    window.blit(text, (10, 5))

    text = font.render("Heart:  " + str(heart), 1, (255, 0, 0))     #TO SHOW HEART
    window.blit(text, (500, 5))

    """DRAW ALL THE OBJECTS AT THE WINDOW"""
    bird1_1.draw(window)
    bird2_2.draw(window)
    # enemy2_1.draw(window)
    enemy1_1.draw(window)
    enemy2_2.draw(window)
    object1.draw(window)
    object2.draw(window)
    first_aid.draw(window)
    flag_port.draw(window)
    flag_port2.draw(window)
    funny.draw(window)
    runner.draw(window)

    for bullet in bullets:    #DRAW BULLETS AT THE WINDOW
        bullet.draw(window)

    for obstacle in obstacles:      #DRAW OBSTACLE FROM OBSTACLE LIST AT THE WINDOW
        obstacle.draw(window)

    pygame.display.update()           #UPDATE THE DISPLAY


pygame.time.set_timer(USEREVENT + 1, 10000)     #DEFINE USEREVENT FOR TIME LOOP
pygame.time.set_timer(USEREVENT + 2, 5000)      #DEFINE USEREVENT FOR TIME LOOP
pygame.time.set_timer(USEREVENT + 3, 6000)      #DEFINE USEREVENT FOR TIME LOOP

bird1_1 = lvl1_bird(950, 250, 64, 120)      #DEFINE THE AXIS FOR BIRD ENEMY AT LEVEL 1
bird2_2 = lvl2_bird(950, 250, 64, 120)       #DEFINE THE AXIS FOR BIRD ENEMY AT LEVEL 2

runner = player(100, 275, 80, 122)      #DEFINE THE AXIS FOR MAIN CHARACTER
object1 = lvl1_rock(1000, 345, 60, 50)      #DEFINE THE AXIS FOR OBSTACLE AT LEVEL 1
object2 = lvl2_rock(1000, 343, 60, 50)      #DEFINE THE AXIS FOR OBSTACLE AT LEVEL 2
enemy1_1 = lvl1_enemy(950, 300, 64, 120)      #DEFINE THE AXIS FOR ENEMY AT LEVEL 1
enemy2_2 = lvl2_enemy(1000, 150, 64, 120)      #DEFINE THE AXIS FOR ENEMY AT LEVEL 2
first_aid = aid(7000, 200, 68, 58)      #DEFINE THE AXIS FOR FIRST-AID KIT

flag_port = flag(4450, 300, 70, 70)      #DEFINE THE AXIS FOR DESTINATION SIGN AT LEVEL 1
flag_port2 = flag2(4940, 312, 70, 70)      #DEFINE THE AXIS FORDESTINATION SIGNY AT LEVEL 2

cloudy = cloud(950, 10, 200, 70)      #DEFINE THE AXIS FOR CLOUD
funny = funny_bird(950, 10, 200, 70)      #DEFINE THE AXIS FOR BACKGROUND BIRD
keys = pygame.key.get_pressed()             #GET THE KEY EVNTS
radius = 0

x_bullet = 100              #DEFINE THE X AXIS FOR BULLET
y_bullet = 270              #DEFINE THE Y AXIS FOR BULLET

run = True

timeClock = pygame.time.Clock()         #EVENT FOR TIME COUNT
Fps = 40  # speed = 40                  #DEFINE THE FRAME PER SECOND VALUE

speed = 0

walkcount = 0

obstacles = []              #CREATE OBSTACLE LIST
bullets = []                #CREATE BULLET LIST
shootLoop = 0

score = 5                    #INITIAL SCORE IS 5
heart = 20                   #INITIAL HEART IS 20 FOR LEVEL 1
font = pygame.font.SysFont("comicsans", 30, True, True)  # ("Font_name", Font_size, Font_bool, Font_italic)
end = 0

game_over_music = load_sound("gameover.wav")    #READ MUSIC AND SOUND FROM FOLDER
lvl1_music =load_sound("dungeon_theme.ogg")
lvl2_music = load_sound("gamehard.wav")
shoot_sound = load_sound("shotgun.wav")
level_up_sound = load_sound("upgrade.wav")
winner_sound = load_sound("pleasant_creek.ogg")

"""MAIN LOOP"""
while True:

    background1_X -= 1.5  # define background loop which way
    background2_X -= 1.5  # define background loop which way

    '''COLLISION MECHANISM BETWEEN CHARACTER AND ENEMY'''
    if bird1_1.lvl1 == True:
        if runner.hitbox[1] < bird1_1.hitbox[1] + bird1_1.hitbox[3] and runner.hitbox[1] + runner.hitbox[3] > \
                bird1_1.hitbox[1]:
            if runner.hitbox[0] + runner.hitbox[2] > bird1_1.hitbox[0] and runner.hitbox[0] < bird1_1.hitbox[0] + \
                    bird1_1.hitbox[2]:
                runner.fall_1()   #FUNCTION CALL

    """BULLET HIT MECHANISM WITH ENEMY"""
    if bird1_1.visible == True:
        for bullet in bullets:
            if bullet.y - bullet.radius < bird1_1.hitbox[1] + bird1_1.hitbox[3] and bullet.y + bullet.radius > \
                    bird1_1.hitbox[1]:
                if bullet.x + bullet.radius > bird1_1.hitbox[0] and bullet.x - bullet.radius < bird1_1.hitbox[0] + \
                        bird1_1.hitbox[2]:
                    bird1_1.hit()    #FUNCTION CALL
                    score += 3         #SCORE INCREAS
                    bullets.pop(bullets.index(bullet))

                    if bullet.x < 1024 and bullet.x > 0:
                        bullet.x += bullet.vel
                    else:
                        bullets.pop(bullets.index(bullet))

    """ENEMY APPEAR AGAIN AFTER GET KILLED"""
    if bird1_1.lvl1 == True:
        if bird1_1.visible == False:
            bird1_1.x = 1000             #ENEMY APPEAR AGAIN AFTER DISAPPEARING
            bird1_1.y = 250
            bird1_1.visible = True

    '''COLLISION MECHANISM BETWEEN CHARACTER AND ENEMY'''
    if enemy1_1.lvl1 == True:
        if runner.hitbox[1] < enemy1_1.hitbox[1] + enemy1_1.hitbox[3] and runner.hitbox[1] + runner.hitbox[3] > \
                enemy1_1.hitbox[1]:
            if runner.hitbox[0] + runner.hitbox[2] > enemy1_1.hitbox[0] and runner.hitbox[0] < enemy1_1.hitbox[0] + \
                    enemy1_1.hitbox[2]:
                level_up_sound.play()       #FUNCTION CALL
                if heart == 0:
                    runner.fall_1()         #FUNCTION CALL
                if heart >=10:
                    runner.collide()        #FUNCTION CALL
                    enemy1_1.x = 950
                    for obstacle in obstacles:
                        obstacles.pop(obstacles.index(obstacle))
                    heart -= 10

    """BULLET HIT MECHANISM WITH ENEMY"""
    if enemy1_1.visible == True:
        for bullet in bullets:
            if bullet.y - bullet.radius < enemy1_1.hitbox[1] + enemy1_1.hitbox[3] and bullet.y + bullet.radius > \
                    enemy1_1.hitbox[1]:
                if bullet.x + bullet.radius > enemy1_1.hitbox[0] and bullet.x - bullet.radius < enemy1_1.hitbox[0] + \
                        enemy1_1.hitbox[2]:
                    enemy1_1.hit()           #FUNCTION CALL
                    score += 1
                    bullets.pop(bullets.index(bullet))

                    if bullet.x < 1024 and bullet.x > 0:
                        bullet.x += bullet.vel
                    else:
                        bullets.pop(bullets.index(bullet))

                    if bullet.x < 950 and bullet.x > 0:
                        bullet.x += bullet.vel
                    if bullet.x > 950 and bullet.x < 0:
                        # else:
                        bullets.pop(bullets.index(bullet))

    """ENEMY APPEAR AGAIN AFTER GET KILLED"""
    if enemy1_1.lvl1 == True:
        if enemy1_1.visible == False:       # ENEMY APPEAR AGAIN AFTER DISAPPEARING
            enemy1_1.x = 950
            enemy1_1.y = 300
            enemy1_1.visible = True

    '''COLLISION MECHANISM BETWEEN CHARACTER AND OBSTACLE'''
    if object1.lvl1 == True:
        if runner.hitbox[1] < object1.hitbox[1] + object1.hitbox[3] and runner.hitbox[1] + runner.hitbox[3] > \
                object1.hitbox[1]:
            if runner.hitbox[0] + runner.hitbox[2] > object1.hitbox[0] and runner.hitbox[0] < object1.hitbox[0] + \
                    object1.hitbox[2]:
                if score <= 0:
                    runner.fall_1()     #FUNCTION CALL
                if score >0:
                    font1 = pygame.font.SysFont("comicsans", 100)
                    text = font1.render("-5", 1, (255, 0, 0))           #"-5" FONT
                    window.blit(text, (80, 5))
                    pygame.display.update()
                    i = 0
                    while i < 50:
                        pygame.time.delay(10)
                        i += 1
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                i = 301
                                pygame.quit()
                    object1.x = 1000
                    for obstacle in obstacles:
                        obstacles.pop(obstacles.index(obstacle))
                    score -= 5

    """OBSTACLE APPEAR AGAIN AFTER DISAPPEAR"""
    if object1.lvl1 == True:
        if object1.visible == False:
            object1.x = 1000                #OBSTACLE APPEAR AGAIN AFTER DISAPPEARING
            object1.y = 350
            object1.visible = True

    '''COLLISION MECHANISM BETWEEN CHARACTER AND FIRST-AID KIT'''
    if runner.hitbox[1] < first_aid.hitbox[1] + first_aid.hitbox[3] and runner.hitbox[1] + runner.hitbox[3] > \
            first_aid.hitbox[1]:
        if runner.hitbox[0] + runner.hitbox[2] > first_aid.hitbox[0] and runner.hitbox[0] < first_aid.hitbox[0] + \
                first_aid.hitbox[2]:

            first_aid.x = 3000              #APPEAR AFTER 3000 AXIS
            for obstacle in obstacles:
                obstacles.pop(obstacles.index(obstacle))
            if heart < 29:
                font1 = pygame.font.SysFont("comicsans", 100)
                text = font1.render("+10", 1, (255, 0, 0))     #"+10" FONT FOR HEART
                window.blit(text, (500, 5))
                pygame.display.update()
                i = 0
                while i < 50:
                    pygame.time.delay(10)               #TIME DELAY TO SHOW THE FONT
                    i += 1
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            i = 301
                            pygame.quit()
                heart += 10

    '''COLLISION MECHANISM BETWEEN CHARACTER AND DESTINATION SIGN OF LEVEL 1'''
    if runner.hitbox[1] < flag_port.hitbox[1] + flag_port.hitbox[3] and runner.hitbox[1] + runner.hitbox[3] > \
            flag_port.hitbox[1]:
        if runner.hitbox[0] + runner.hitbox[2] > flag_port.hitbox[0] and runner.hitbox[0] < flag_port.hitbox[0] + \
                flag_port.hitbox[2]:
            heart = 30          #HEART INITIALISE TO 30
            flag_port.x = -300
            enemy1_1.lvl1 = False   #LEVEL 1 METARIALS BECOME FALSE
            bird1_1.lvl1 = False
            lvl1_music.stop()         #LEVEL 1 SOUNDS BECOME MUTE
            level_up_sound.play()
            object1.lvl1 = False         #LEVEL 1 METARIALS BECOME FALSE
            enemy2_2.lvl2 = True
            bird2_2.lvl2 = True
            object2.lvl2 = True
            flag_port2.lvl2 = True
            font1 = pygame.font.SysFont("comicsans", 100)
            text = font1.render("Level Up", 1, (255, 0, 0))    #"LEVEL UP" FONT
            window.blit(text, (400, 200))
            pygame.display.update()
            i = 0
            while i < 50:
                pygame.time.delay(20)           #TIME DELAY TO SHOW THW FONT
                i += 1
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        i = 301
                        pygame.quit()

    '''COLLISION MECHANISM BETWEEN CHARACTER AND DESTINATION SIGN OF LEVEL 2'''
    if flag_port2.lvl2 == True:
        if runner.hitbox[1] < flag_port2.hitbox[1] + flag_port2.hitbox[3] and runner.hitbox[1] + runner.hitbox[3] > \
                flag_port2.hitbox[1]:
            if runner.hitbox[0] + runner.hitbox[2] > flag_port2.hitbox[0] and runner.hitbox[0] < flag_port2.hitbox[0] + \
                    flag_port2.hitbox[2]:
                lvl2_music.stop()           #LEVEL 2 SOUNDS BECOME MUTE
                lvl2_music.stop()
                shoot_sound.stop()
                winner_sound.play(-1)   #SOUND PLAY INIFINITE
                runner.winn()

    '''COLLISION MECHANISM BETWEEN CHARACTER AND ENEMY'''
    if enemy2_2.lvl2 == True:
       # lvl2_music.play(-1)
        if runner.hitbox[1] < enemy2_2.hitbox[1] + enemy2_2.hitbox[3] and runner.hitbox[1] + runner.hitbox[3] > \
                enemy2_2.hitbox[1]:
            if runner.hitbox[0] + runner.hitbox[2] > enemy2_2.hitbox[0] and runner.hitbox[0] < enemy2_2.hitbox[0] + \
                    enemy2_2.hitbox[2]:
                if heart == 0:
                    runner.fall_2()         #FUNCTION CALL
                if heart >= 10:
                    runner.collide()     #FUNCTION CALL
                    enemy2_2.x = 950
                    for obstacle in obstacles:
                        obstacles.pop(obstacles.index(obstacle))
                    heart -= 10

    """BULLET HIT MECHANISM WITH ENEMY"""
    if enemy2_2.visible == True:
        for bullet in bullets:
            if bullet.y - bullet.radius < enemy2_2.hitbox[1] + enemy2_2.hitbox[3] and bullet.y + bullet.radius > \
                    enemy2_2.hitbox[1]:
                if bullet.x + bullet.radius > enemy2_2.hitbox[0] and bullet.x - bullet.radius < enemy2_2.hitbox[0] + \
                        enemy2_2.hitbox[2]:
                    enemy2_2.hit()          #FUNCTION CALL
                    score += 1
                    bullets.pop(bullets.index(bullet))

                    if bullet.x < 1024 and bullet.x > 0:
                        bullet.x += bullet.vel
                    else:
                        bullets.pop(bullets.index(bullet))

                    if bullet.x < 1024 and bullet.x > 0:
                        bullet.x += bullet.vel
                    if bullet.x > 1024 and bullet.x < 0:
                        # else:
                        bullets.pop(bullets.index(bullet))

    """ENEMY APPEAR AGAIN AFTER GET KILLED"""
    if enemy2_2.visible == False:
        enemy2_2.x = 950             #ENEMY APPEAR AGAIN AFTER DISAPPEARING
        enemy2_2.y = 280
        enemy2_2.visible = True

    '''COLLISION MECHANISM BETWEEN CHARACTER AND ENEMY'''
    if bird2_2.lvl2 == True:
        if runner.hitbox[1] < bird2_2.hitbox[1] + bird2_2.hitbox[3] and runner.hitbox[1] + runner.hitbox[3] > \
                bird2_2.hitbox[1]:
            if runner.hitbox[0] + runner.hitbox[2] > bird2_2.hitbox[0] and runner.hitbox[0] < bird2_2.hitbox[0] + \
                    bird2_2.hitbox[2]:
                runner.fall_2()          #FUNCTION CALL

    """BULLET HIT MECHANISM WITH ENEMY"""
    if bird2_2.visible == True:
        for bullet in bullets:
            if bullet.y - bullet.radius < bird2_2.hitbox[1] + bird2_2.hitbox[3] and bullet.y + bullet.radius > \
                    bird2_2.hitbox[1]:
                if bullet.x + bullet.radius > bird2_2.hitbox[0] and bullet.x - bullet.radius < bird2_2.hitbox[0] + \
                        bird2_2.hitbox[2]:
                    bird2_2.hit()                   #FUNCTION CALL
                    score += 3
                    bullets.pop(bullets.index(bullet))

                    if bullet.x < 1024 and bullet.x > 0:
                        bullet.x += bullet.vel
                    else:
                        bullets.pop(bullets.index(bullet))

    """ENEMY APPEAR AGAIN AFTER GET KILLED"""
    if bird2_2.lvl2 == True:
        if bird2_2.visible == False:
           bird2_2.x = 1000    #ENEMY APPEAR AGAIN AFTER DISAPPEARING
           bird2_2.y = 250
           bird2_2.visible = True

    '''COLLISION MECHANISM BETWEEN CHARACTER AND OBSTACLE'''
    if object2.lvl2 == True:
        if runner.hitbox[1] < object2.hitbox[1] + object2.hitbox[3] and runner.hitbox[1] + runner.hitbox[3] > \
                object2.hitbox[1]:
            if runner.hitbox[0] + runner.hitbox[2] > object2.hitbox[0] and runner.hitbox[0] < object2.hitbox[0] + \
                    object2.hitbox[2]:
                if score <= 0:
                    runner.fall_2()     #FUNCTION CALL
                if score > 0:
                    font1 = pygame.font.SysFont("comicsans", 100)
                    text = font1.render("-5", 1, (255, 0, 0))           #"-5" FONT
                    window.blit(text, (80, 5))
                    pygame.display.update()
                    i = 0
                    while i < 50:
                        pygame.time.delay(10)     #TIME DELAY TO SHOW THE FONT
                        i += 1
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                i = 301
                                pygame.quit()
                    object2.x = 1000
                    for obstacle in obstacles:
                        obstacles.pop(obstacles.index(obstacle))
                    score -= 5

    """OBSTACLE APPEAR AGAIN AFTER GET KILLED"""
    if object2.lvl2 == True:
        if object2.visible == False:
            object2.x = 1000                 #OBSTACLE APPEAR AGAIN AFTER DISAPPEARING
            object2.y = 343
            object2.visible = True

    for obstacle in obstacles:
        if obstacle.x < -64:
            obstacles.pop(obstacles.index(obstacle))    #OBSTACLES DISAPPEAR AFTER -64 AXIS
        else:
            obstacle.x -= 1.5               #OBSTACLE MOVE RIGHT TO LEFT

    if shootLoop > 0:
        shootLoop += 1              #SHOOTLOOP INCREASES
    if shootLoop > 7:
        shootLoop = 0

    keys = pygame.key.get_pressed()                 #GET KEYBOARD COMMAND

    if keys[pygame.K_SPACE] and shootLoop == 0:     #SHOOT USING "SPACE" KEY
        if runner.Left:
            runner.facing = -1
        if runner.Right:
            runner.facing = 1
        if runner.standing:
            runner.facing = 1

        if len(bullets) < 5:
            bullets.append(tile(round(runner.x + 50), round(runner.y + 85), 6, (255, 0, 0), runner.facing))
        shootLoop = 1
        shoot_sound.play()          #FUNCTION CALL
        if enemy1_1.lvl1 == True:
            lvl1_music.play(-1)     #FUNCTION CALL

        if enemy2_2.lvl2 == True:
            lvl2_music.play(-1)         #FUNCTION CALL

    for bullet in bullets:
        if bullet.x < 1024 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    if runner.falling == False:
        if keys[pygame.K_LEFT] and runner.x > runner.velocity:   # MOVE THE CHARACTER TO LEFT
            runner.x -= runner.velocity
            runner.Right = False
            runner.Left = True
            runner.standing = False

        elif keys[pygame.K_RIGHT] and runner.x < 800:       # MOVE THE CHARACTER TO RIGHT
            runner.x += runner.velocity
            runner.Right = True
            runner.Left = False
            runner.standing = False

        else:
            runner.standing = True
        if not (runner.jumping):                # MAEK THE CHARACER JUMP
            if keys[pygame.K_UP]:
                runner.jumping = True
                # runner.Right = False
                # runner.Left = False
        else:
            if runner.jumpCount >= -10:             #JUMP MECHANISM
                runner.negative = 1
                if runner.jumpCount < 0:
                    runner.negative = -1
                runner.y -= (runner.jumpCount ** 2) * 0.5 * runner.negative
                runner.jumpCount -= 1
            else:
                runner.jumping = False
                runner.jumpCount = 10

    if background1_X < background.get_width() * -1:                 # MAKE THE BACKGROUND LOOP RIGHT TO LEFT
        background1_X = background.get_width()  # make the loop infinite
    if background2_X < background.get_width() * -1:
        background2_X = background.get_width()  # make the loop infinite

    for event in pygame.event.get():
        if event.type == pygame.QUIT:               #QUIT THE GAME IF CLICK CROSS
            pygame.quit()
            run = False

        if event.type == USEREVENT + 1:             #USEREVENT 1
            speed += 1

        if event.type == USEREVENT + 2:              #USEREVENT 2
            r = random.randrange(0, 2)
            if r == 0:
                obstacles.append(cloud(cloudy.x, cloudy.y, cloudy.width, cloudy.height))   # APPEAR THE CLOUD

        """ENEMY APPEAR AGAIN AFTER GET KILLED"""
        if bird1_1.lvl1 == True:
            if bird1_1.visible == False:
               bird1_1.x = 1000          #ENEMY APPEAR AGAIN AFTER DISAPPEARING
               bird1_1.y = 250
               bird1_1.visible = True

        """FIRST-AID KIT APPEAR AGAIN AFTER USED"""
        if first_aid.visible == False:
            first_aid.x = 7000               #FIRST-AID KIT APPEAR AGAIN AFTER DISAPPEARING
            first_aid.y = 200
            first_aid.visible = True

    timeClock.tick(Fps)          # ABLE THE FPS
    redrwWindow()                # FUNCTION CALL
    pygame.display.update()      # UPDATE THE DISPLAY
