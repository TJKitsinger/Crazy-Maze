import pygame, sys, math
from pygame.locals import *
from spritesheet import Spritesheet
pygame.init()

FPS = 30
frames = 0
cameraheightblocks = 9
camerawidthblocks = 12
cameraheight = cameraheightblocks * 64
camerawidth = camerawidthblocks * 64
DISPLAYSURF = pygame.display.set_mode((camerawidth, cameraheight), 0, 32)
forwardstand = pygame.image.load("HarrietStandingFront.png")
rightstand = pygame.image.load("HarrietStandingRight.png")
leftstand = pygame.image.load("HarrietStandingLeft.png")
backstand = pygame.image.load("HarrietStandingBack.png")
testgrass = pygame.image.load("Grass Middle.png")
testhedge = pygame.image.load("Leaves.png")
health3 = pygame.image.load("HUD Heart 3.png")
health2 = pygame.image.load("HUD Heart 2.png")
health1 = pygame.image.load("HUD Heart 1.png")
health0 = pygame.image.load("HUD Heart 0.png")
enemygone = False
xspeed = 0
yspeed = 0
harrietxpos = 100
harrietypos = 100
harrietrightedge = harrietxpos + 64
harrietbottomedge = harrietypos + 64
cameraleftedge = 0
cameratopedge = 0
lastmoved = "down"
moving = False
health = 3
room = 1
hasWeapon = False
invincibilityframes = 60
invincible = False
enemyxpos = -1
enemyypos = -1
hasWeapon = False

enemyneutral = pygame.image.load("angry.png")
healthpotion = pygame.image.load("Potion.png")
weapon = pygame.image.load("weapon.png")

harrietfrontspritesheet = Spritesheet('harrietwalkfrontsheet.png')
harrietfront1 = harrietfrontspritesheet.get_sprite(0, 0, 64, 64)
harrietfront2 = harrietfrontspritesheet.get_sprite(0, 65, 64,64)
harrietfront3 = harrietfrontspritesheet.get_sprite(0, 129, 64,64)
harrietfront4 = harrietfrontspritesheet.get_sprite(0, 193, 64,64)
harrietfront5 = harrietfrontspritesheet.get_sprite(0, 257, 64,64)
harrietfront6 = harrietfrontspritesheet.get_sprite(0, 321, 64,64)
harrietfront7 = harrietfrontspritesheet.get_sprite(0, 385, 64,64)
harrietfront8 = harrietfrontspritesheet.get_sprite(0, 449, 64,64)
harrietfront9 = harrietfrontspritesheet.get_sprite(0, 65, 64,64)
harrietfront10 = harrietfrontspritesheet.get_sprite(0, 513, 64,64)
harrietfront11 = harrietfrontspritesheet.get_sprite(0, 577, 64,64)
harrietfront12 = harrietfrontspritesheet.get_sprite(0, 641, 64,64)
harrietfront13 = harrietfrontspritesheet.get_sprite(0, 705, 64,64)
harrietfront14 = harrietfrontspritesheet.get_sprite(0, 769, 64,64)
harrietfront15 = harrietfrontspritesheet.get_sprite(0, 833, 64,64)

harrietbackspritesheet = Spritesheet('harrietwalkbacksheet.png')
harrietback1 = harrietbackspritesheet.get_sprite(0, 0, 64, 64)
harrietback2 = harrietbackspritesheet.get_sprite(0, 65, 64,64)
harrietback3 = harrietbackspritesheet.get_sprite(0, 129, 64,64)
harrietback4 = harrietbackspritesheet.get_sprite(0, 193, 64,64)
harrietback5 = harrietbackspritesheet.get_sprite(0, 257, 64,64)
harrietback6 = harrietbackspritesheet.get_sprite(0, 321, 64,64)
harrietback7 = harrietbackspritesheet.get_sprite(0, 385, 64,64)
harrietback8 = harrietbackspritesheet.get_sprite(0, 449, 64,64)
harrietback9 = harrietbackspritesheet.get_sprite(0, 65, 64,64)
harrietback10 = harrietbackspritesheet.get_sprite(0, 513, 64,64)
harrietback11 = harrietbackspritesheet.get_sprite(0, 577, 64,64)
harrietback12 = harrietbackspritesheet.get_sprite(0, 641, 64,64)
harrietback13 = harrietbackspritesheet.get_sprite(0, 705, 64,64)
harrietback14 = harrietbackspritesheet.get_sprite(0, 769, 64,64)
harrietback15 = harrietbackspritesheet.get_sprite(0, 833, 64,64)

harrietrightspritesheet = Spritesheet('harrietwalkrightsheet.png')
harrietright1 = harrietrightspritesheet.get_sprite(0, 0, 64, 64)
harrietright2 = harrietrightspritesheet.get_sprite(0, 65, 64,64)
harrietright3 = harrietrightspritesheet.get_sprite(0, 129, 64,64)
harrietright4 = harrietrightspritesheet.get_sprite(0, 193, 64,64)
harrietright5 = harrietrightspritesheet.get_sprite(0, 257, 64,64)
harrietright6 = harrietrightspritesheet.get_sprite(0, 321, 64,64)
harrietright7 = harrietrightspritesheet.get_sprite(0, 385, 64,64)
harrietright8 = harrietrightspritesheet.get_sprite(0, 449, 64,64)
harrietright9 = harrietrightspritesheet.get_sprite(0, 65, 64,64)
harrietright10 = harrietrightspritesheet.get_sprite(0, 513, 64,64)
harrietright11 = harrietrightspritesheet.get_sprite(0, 577, 64,64)
harrietright12 = harrietrightspritesheet.get_sprite(0, 641, 64,64)
harrietright13 = harrietrightspritesheet.get_sprite(0, 705, 64,64)
harrietright14 = harrietrightspritesheet.get_sprite(0, 769, 64,64)
harrietright15 = harrietrightspritesheet.get_sprite(0, 833, 64,64)

harrietleftspritesheet = Spritesheet('harrietwalkleftsheet.png')
harrietleft1 = harrietleftspritesheet.get_sprite(0, 0, 64, 64)
harrietleft2 = harrietleftspritesheet.get_sprite(0, 65, 64,64)
harrietleft3 = harrietleftspritesheet.get_sprite(0, 129, 64,64)
harrietleft4 = harrietleftspritesheet.get_sprite(0, 193, 64,64)
harrietleft5 = harrietleftspritesheet.get_sprite(0, 257, 64,64)
harrietleft6 = harrietleftspritesheet.get_sprite(0, 321, 64,64)
harrietleft7 = harrietleftspritesheet.get_sprite(0, 385, 64,64)
harrietleft8 = harrietleftspritesheet.get_sprite(0, 449, 64,64)
harrietleft9 = harrietleftspritesheet.get_sprite(0, 65, 64,64)
harrietleft10 = harrietleftspritesheet.get_sprite(0, 513, 64,64)
harrietleft11 = harrietleftspritesheet.get_sprite(0, 577, 64,64)
harrietleft12 = harrietleftspritesheet.get_sprite(0, 641, 64,64)
harrietleft13 = harrietleftspritesheet.get_sprite(0, 705, 64,64)
harrietleft14 = harrietleftspritesheet.get_sprite(0, 769, 64,64)
harrietleft15 = harrietleftspritesheet.get_sprite(0, 833, 64,64)

with open("test.txt") as words:
    strings = [line.split() for line in words]

print(strings)

levelheight = len(strings[0])
levelwidth = len(strings)
print(levelheight, levelwidth)

print(strings)



class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = "W"

board = list(([[Tile(x, y) for y in range(levelheight)] for x in range (levelwidth)]))

for y in range(levelheight):
    for x in range(levelwidth):
        #print(x, y)
        board[x][y].image = strings[x][y]

def enemy():
    global harrietypos, harrietxpos, enemyypos, enemyxpos, health, invincible, lastmoved, firedweapon, enemygone
    if(harrietypos <= enemyypos - 128):
        enemyypos = enemyypos-4
    if (harrietypos >= enemyypos + 128):
        enemyypos = enemyypos + 4
    if (harrietxpos <= enemyxpos - 128):
        enemyxpos = enemyxpos - 4
    if (harrietxpos >= enemyxpos + 128):
        enemyxpos = enemyxpos + 4

    if(harrietypos >= enemyypos - 32 and harrietypos < enemyypos + 32 and harrietxpos >= enemyxpos - 32 and harrietxpos < enemyxpos + 32 and invincible == False and firedweapon == False and (room != 2) and enemygone == False):
        health = health - 1
        invincible = True
        if(lastmoved == "left"):
            harrietxpos = harrietxpos + 60
        if (lastmoved == "right"):
            harrietxpos = harrietxpos - 60
        if (lastmoved == "up"):
            harrietypos = harrietypos + 60
        if (lastmoved == "down"):
            harrietypos = harrietypos - 60

    if (harrietypos >= enemyypos - 32 and harrietypos < enemyypos + 32 and harrietxpos >= enemyxpos - 32 and harrietxpos < enemyxpos + 32 and invincible == False and firedweapon == True):
        enemygone = True

def Weapon():
    global hasWeapon
    if(room == 2 and harrietypos >= 268 and harrietypos < 332 and harrietxpos >= 268 and harrietxpos < 332):
        hasWeapon = True

def absoluteLeftTopCoordsOfBox(x, y):
    left = x * (64)
    top = y * (64)
    return (left, top)

def cameraLeftTopCoordsOfBox(x, y):
    left = (x * 64) - cameraleftedge
    top = (y * 64) - cameratopedge
    return (left, top)

def drawlevel():
    global lastmoved, moving, enemygone
    for x in range (levelwidth):
        for y in range (levelheight):
            if(board[x][y].image=="W"):
                DISPLAYSURF.blit(testhedge, (cameraLeftTopCoordsOfBox(x, y)))
            if (board[x][y].image == "G"):
                DISPLAYSURF.blit(testgrass, (cameraLeftTopCoordsOfBox(x, y)))
            if (board[x][y].image == "P"):
                DISPLAYSURF.blit(testgrass, (cameraLeftTopCoordsOfBox(x, y)))

    if(enemygone == False and (room == 1 or room == 3 or room == 4 or room == 5)):
        DISPLAYSURF.blit(enemyneutral, (enemyxpos, enemyypos))
    if(room == 2 and hasWeapon == False):
        DISPLAYSURF.blit(weapon, (300, 300))
    #if (room == 4):
        #DISPLAYSURF.blit(healthpotion, (300, 300))
    #pygame.draw.rect(DISPLAYSURF, (0, 0, 0), (enemyxpos, enemyypos, 64, 64))

    if(moving == False):
        if(lastmoved == "down"):
            DISPLAYSURF.blit(forwardstand, (harrietxpos, harrietypos))
        if (lastmoved == "right"):
            DISPLAYSURF.blit(rightstand, (harrietxpos, harrietypos))
        if (lastmoved == "left"):
            DISPLAYSURF.blit(leftstand, (harrietxpos, harrietypos))
        if (lastmoved == "up"):
            DISPLAYSURF.blit(backstand, (harrietxpos, harrietypos))
    else:
        if(lastmoved == "down"):
            if(frames % 15 == 1):
                DISPLAYSURF.blit(harrietfront1, (harrietxpos, harrietypos))
            if(frames % 15 == 2):
                DISPLAYSURF.blit(harrietfront2, (harrietxpos, harrietypos))
            if (frames % 15 == 3):
                DISPLAYSURF.blit(harrietfront3, (harrietxpos, harrietypos))
            if (frames % 15 == 4):
                DISPLAYSURF.blit(harrietfront4, (harrietxpos, harrietypos))
            if (frames % 15 == 5):
                DISPLAYSURF.blit(harrietfront5, (harrietxpos, harrietypos))
            if (frames % 15 == 6):
                DISPLAYSURF.blit(harrietfront6, (harrietxpos, harrietypos))
            if (frames % 15 == 7):
                DISPLAYSURF.blit(harrietfront7, (harrietxpos, harrietypos))
            if (frames % 15 == 8):
                DISPLAYSURF.blit(harrietfront8, (harrietxpos, harrietypos))
            if (frames % 15 == 9):
                DISPLAYSURF.blit(harrietfront1, (harrietxpos, harrietypos))
            if (frames % 15 == 10):
                DISPLAYSURF.blit(harrietfront2, (harrietxpos, harrietypos))
            if (frames % 15 == 11):
                DISPLAYSURF.blit(harrietfront3, (harrietxpos, harrietypos))
            if (frames % 15 == 12):
                DISPLAYSURF.blit(harrietfront4, (harrietxpos, harrietypos))
            if (frames % 15 == 13):
                DISPLAYSURF.blit(harrietfront5, (harrietxpos, harrietypos))
            if (frames % 15 == 14):
                DISPLAYSURF.blit(harrietfront6, (harrietxpos, harrietypos))
            if (frames % 15 == 0):
                DISPLAYSURF.blit(harrietfront7, (harrietxpos, harrietypos))
        if (lastmoved == "up"):
            if (frames % 15 == 1):
                DISPLAYSURF.blit(harrietback1, (harrietxpos, harrietypos))
            if (frames % 15 == 2):
                DISPLAYSURF.blit(harrietback2, (harrietxpos, harrietypos))
            if (frames % 15 == 3):
                DISPLAYSURF.blit(harrietback3, (harrietxpos, harrietypos))
            if (frames % 15 == 4):
                DISPLAYSURF.blit(harrietback4, (harrietxpos, harrietypos))
            if (frames % 15 == 5):
                DISPLAYSURF.blit(harrietback5, (harrietxpos, harrietypos))
            if (frames % 15 == 6):
                DISPLAYSURF.blit(harrietback6, (harrietxpos, harrietypos))
            if (frames % 15 == 7):
                DISPLAYSURF.blit(harrietback7, (harrietxpos, harrietypos))
            if (frames % 15 == 8):
                DISPLAYSURF.blit(harrietback8, (harrietxpos, harrietypos))
            if (frames % 15 == 9):
                DISPLAYSURF.blit(harrietback1, (harrietxpos, harrietypos))
            if (frames % 15 == 10):
                DISPLAYSURF.blit(harrietback2, (harrietxpos, harrietypos))
            if (frames % 15 == 11):
                DISPLAYSURF.blit(harrietback3, (harrietxpos, harrietypos))
            if (frames % 15 == 12):
                DISPLAYSURF.blit(harrietback4, (harrietxpos, harrietypos))
            if (frames % 15 == 13):
                DISPLAYSURF.blit(harrietback5, (harrietxpos, harrietypos))
            if (frames % 15 == 14):
                DISPLAYSURF.blit(harrietback6, (harrietxpos, harrietypos))
            if (frames % 15 == 0):
                DISPLAYSURF.blit(harrietback7, (harrietxpos, harrietypos))
        if (lastmoved == "right"):
            if (frames % 15 == 1):
                DISPLAYSURF.blit(harrietright1, (harrietxpos, harrietypos))
            if (frames % 15 == 2):
                DISPLAYSURF.blit(harrietright2, (harrietxpos, harrietypos))
            if (frames % 15 == 3):
                DISPLAYSURF.blit(harrietright3, (harrietxpos, harrietypos))
            if (frames % 15 == 4):
                DISPLAYSURF.blit(harrietright4, (harrietxpos, harrietypos))
            if (frames % 15 == 5):
                DISPLAYSURF.blit(harrietright5, (harrietxpos, harrietypos))
            if (frames % 15 == 6):
                DISPLAYSURF.blit(harrietright6, (harrietxpos, harrietypos))
            if (frames % 15 == 7):
                DISPLAYSURF.blit(harrietright7, (harrietxpos, harrietypos))
            if (frames % 15 == 8):
                DISPLAYSURF.blit(harrietright8, (harrietxpos, harrietypos))
            if (frames % 15 == 9):
                DISPLAYSURF.blit(harrietright1, (harrietxpos, harrietypos))
            if (frames % 15 == 10):
                DISPLAYSURF.blit(harrietright2, (harrietxpos, harrietypos))
            if (frames % 15 == 11):
                DISPLAYSURF.blit(harrietright3, (harrietxpos, harrietypos))
            if (frames % 15 == 12):
                DISPLAYSURF.blit(harrietright4, (harrietxpos, harrietypos))
            if (frames % 15 == 13):
                DISPLAYSURF.blit(harrietright5, (harrietxpos, harrietypos))
            if (frames % 15 == 14):
                DISPLAYSURF.blit(harrietright6, (harrietxpos, harrietypos))
            if (frames % 15 == 0):
                DISPLAYSURF.blit(harrietright7, (harrietxpos, harrietypos))
        if (lastmoved == "left"):
            if (frames % 15 == 1):
                DISPLAYSURF.blit(harrietleft1, (harrietxpos, harrietypos))
            if (frames % 15 == 2):
                DISPLAYSURF.blit(harrietleft2, (harrietxpos, harrietypos))
            if (frames % 15 == 3):
                DISPLAYSURF.blit(harrietleft3, (harrietxpos, harrietypos))
            if (frames % 15 == 4):
                DISPLAYSURF.blit(harrietleft4, (harrietxpos, harrietypos))
            if (frames % 15 == 5):
                DISPLAYSURF.blit(harrietleft5, (harrietxpos, harrietypos))
            if (frames % 15 == 6):
                DISPLAYSURF.blit(harrietleft6, (harrietxpos, harrietypos))
            if (frames % 15 == 7):
                DISPLAYSURF.blit(harrietleft7, (harrietxpos, harrietypos))
            if (frames % 15 == 8):
                DISPLAYSURF.blit(harrietleft8, (harrietxpos, harrietypos))
            if (frames % 15 == 9):
                DISPLAYSURF.blit(harrietleft1, (harrietxpos, harrietypos))
            if (frames % 15 == 10):
                DISPLAYSURF.blit(harrietleft2, (harrietxpos, harrietypos))
            if (frames % 15 == 11):
                DISPLAYSURF.blit(harrietleft3, (harrietxpos, harrietypos))
            if (frames % 15 == 12):
                DISPLAYSURF.blit(harrietleft4, (harrietxpos, harrietypos))
            if (frames % 15 == 13):
                DISPLAYSURF.blit(harrietleft5, (harrietxpos, harrietypos))
            if (frames % 15 == 14):
                DISPLAYSURF.blit(harrietleft6, (harrietxpos, harrietypos))
            if (frames % 15 == 0):
                DISPLAYSURF.blit(harrietleft7, (harrietxpos, harrietypos))
    if(health == 3):
        DISPLAYSURF.blit(health3, (0, 0))
    if(health == 2):
        DISPLAYSURF.blit(health2, (0, 0))
    if(health == 1):
        DISPLAYSURF.blit(health1, (0, 0))
    if(health == 0):
        pygame.quit()
    #pygame.draw.rect(DISPLAYSURF, (0, 0, 0), (harrietxpos, harrietypos, 64, 64))
    #pygame.display.update()

def main():
    global xspeed, yspeed, harrietxpos, harrietypos, harrietbottomedge, harrietrightedge, lastmoved, moving, cameraleftedge, camerarightedge, frames, enemyxpos, enemyypos, invincible, invincibilityframes, room, weapon, firedweapon, enemygone
    lastmoved = "down"
    health = 3
    FPSCLOCK = pygame.time.Clock()
    drawlevel()
    enemyxpos = 200
    enemyypos = 400
    movementspeed = 8
    while True:


        FPSCLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        if (pygame.key.get_pressed()[K_SPACE] == True and hasWeapon == True):
            firedweapon = True
            print("weapon fired")

        if (pygame.key.get_pressed()[K_UP] == True):
            xspeed = 0
            yspeed = -1
            #print(xspeed, yspeed)

        elif (pygame.key.get_pressed()[K_DOWN] == True):
            xspeed = 0
            yspeed = 1
            #print(xspeed, yspeed)

        elif (pygame.key.get_pressed()[K_RIGHT] == True):
            xspeed = 1
            yspeed = 0
            #print(xspeed, yspeed)

        elif (pygame.key.get_pressed()[K_LEFT] == True):
            xspeed = -1
            yspeed = 0
            #print(xspeed, yspeed)

        else:
            xspeed = 0
            yspeed = 0
            #print(xspeed, yspeed)
            moving = False

        if (xspeed == 1):
            if(board[math.trunc((harrietrightedge+movementspeed)/64)][math.trunc((harrietypos)/64)].image != "W" and board[math.trunc((harrietrightedge+movementspeed)/64)][math.trunc((harrietbottomedge)/64)].image != "W"):
                harrietxpos = harrietxpos + movementspeed
                #print("right")
                lastmoved = "right"
                moving = True
                enemy()
                Weapon()

        elif (xspeed == -1):
            if (board[math.trunc((harrietxpos - movementspeed) / 64)][math.trunc((harrietypos) / 64)].image != "W" and board[math.trunc((harrietxpos - movementspeed)/64)][math.trunc((harrietbottomedge)/64)].image != "W"):
                harrietxpos = harrietxpos - movementspeed
                #print("left")
                lastmoved = "left"
                moving = True
                enemy()
                Weapon()

        if (yspeed == 1):
            if (board[math.trunc(harrietxpos / 64)][math.trunc((harrietbottomedge+movementspeed)/ 64)].image != "W" and board[math.trunc(harrietrightedge / 64)][math.trunc((harrietbottomedge+movementspeed) / 64)].image != "W"):
                harrietypos = harrietypos + movementspeed
                #print("down")
                lastmoved = "down"
                moving = True
                enemy()
                Weapon()
        elif (yspeed == -1):
            if (harrietypos <= 0):
                harrietxpos = 400
                harrietypos = 400
                room = room + 1

                if(room == 2):
                    enemygone = False
                    with open("test2.txt") as words:
                        strings = [line.split() for line in words]

                    #print(strings)

                    levelheight = len(strings[0])
                    levelwidth = len(strings)
                    #print(levelheight, levelwidth)

                    #print(strings)

                    for y in range(levelheight):
                        for x in range(levelwidth):
                            # print(x, y)
                            board[x][y].image = strings[x][y]
                    drawlevel()

                if (room == 3):
                    enemygone = False
                    with open("test3.txt") as words:
                        strings = [line.split() for line in words]

                    #print(strings)

                    levelheight = len(strings[0])
                    levelwidth = len(strings)
                    #print(levelheight, levelwidth)

                    #print(strings)

                    for y in range(levelheight):
                        for x in range(levelwidth):
                            # print(x, y)
                            board[x][y].image = strings[x][y]

                    drawlevel()

                if (room == 4):
                    enemygone = False
                    with open("test4.txt") as words:
                        strings = [line.split() for line in words]

                    #print(strings)

                    levelheight = len(strings[0])
                    levelwidth = len(strings)
                    #print(levelheight, levelwidth)

                    #print(strings)

                    for y in range(levelheight):
                        for x in range(levelwidth):
                            # print(x, y)
                            board[x][y].image = strings[x][y]

                    drawlevel()

                if (room == 5):
                    enemygone = False
                    with open("test5.txt") as words:
                        strings = [line.split() for line in words]

                    #print(strings)

                    levelheight = len(strings[0])
                    levelwidth = len(strings)
                    #print(levelheight, levelwidth)

                    #print(strings)

                    for y in range(levelheight):
                        for x in range(levelwidth):
                            # print(x, y)
                            board[x][y].image = strings[x][y]

                    drawlevel()

                if(room == 6):
                    pygame.quit()

            if (board[math.trunc(harrietxpos / 64)][math.trunc((harrietypos-movementspeed) / 64)].image != "W" and board[math.trunc(harrietrightedge / 64)][math.trunc((harrietypos-movementspeed) / 64)].image != "W"):
                harrietypos = harrietypos - movementspeed
                #print("up")
                lastmoved = "up"
                moving = True
                enemy()
                Weapon()

        if(room == 5 and enemygone == True):
              quit()
        #elif (xspeed == 0 and yspeed == 0):

        harrietrightedge = harrietxpos + 64
        harrietbottomedge = harrietypos + 64
        #print(harrietrightedge, harrietbottomedge)
        #cameraleftedge = harrietxpos - 1000
        #cameratopedge = harrietypos - 1000
        if(invincible == True):
            invincibilityframes = invincibilityframes - 1
            if(invincibilityframes == 0):
                invincible = False
                invincibilityframes = 60

        firedweapon = False
        frames = frames + 1
        drawlevel()
        pygame.display.update()

main()