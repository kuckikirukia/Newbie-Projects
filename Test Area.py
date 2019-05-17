# code.Pylet - Scrolling Background With Player
# watch the video here - https://youtu.be/AX8YU2hLBUg
# Any questions? Just ask!

import math, random, sys
import pygame
from pygame.locals import *


# exit the program
def events():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()


# define display surface
W, H = 1000, 800
HW, HH = W / 2, H / 2
AREA = W * H

# initialize display
pygame.init()
CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((W, H))
pygame.display.set_caption("code.Pylet - Scrolling Background with Player")
FPS = 500

# define some colors
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)

# loads the background image
bg = pygame.image.load("PalletTown.png").convert()
bgWidth, bgHeight = bg.get_rect().size

stageWidth = bgWidth * 6
stageHeight = bgHeight * 6
stagePosX = 0
stagePosY = 0

startScrollingPosX = HW
startScrollingPosY = HH

circleRadius = 15
circlePosX = circleRadius
circlePosY = circleRadius

playerPosX = 0  # circleRadius originally but doesn't seem to matter?
playerPosY = 0  # determines which position @ y-axis the player is locate at
playerVelocityX = 0  # initial velocity at x
playerVelocityY = 0  # initial velocity at y

# main loop of the game
while True:
    events()

    k = pygame.key.get_pressed()

    if k[K_RIGHT]:
        playerVelocityX = 2
        playerVelocityY = 0

    elif k[K_LEFT]:
        playerVelocityX = -2
        playerVelocityY = 0

    elif k[K_UP]:
        playerVelocityX = 0
        playerVelocityY = -2

    elif k[K_DOWN]:
        playerVelocityX = 0
        playerVelocityY = 2

    else:
        playerVelocityX = 0
        playerVelocityY = 0  # if we don't include this part, the movement becomes "crazy" - moves by itself

    # scrolling for left & right movements
    playerPosX += playerVelocityX
    playerPosY += playerVelocityY  # this has to be + for up/down movements to work

    if playerPosX > stageWidth - circleRadius: playerPosX = stageWidth - circleRadius
    if playerPosX < circleRadius: playerPosX = circleRadius
    if playerPosX < startScrollingPosX:
        circlePosX = playerPosX
    elif playerPosX > stageWidth - startScrollingPosX:
        circlePosX = playerPosX - stageWidth + W
    else:
        circlePosX = startScrollingPosX
        stagePosX += -playerVelocityX

    #

    if playerPosY > stageHeight - circleRadius: playerPosY = stageHeight - circleRadius
    if playerPosY < circleRadius: playerPosY = circleRadius
    if playerPosY < startScrollingPosY:
        circlePosY = playerPosY
    elif playerPosY > stageHeight - startScrollingPosY:
        circlePosY = playerPosY - stageHeight + H
    else:
        circlePosY = startScrollingPosY
        stagePosY += -playerVelocityY

    #

    rel_x = stagePosX % bgWidth
    rel_y = stagePosY % bgHeight
    DS.blit(bg, (rel_x - bgWidth, 0))

    if rel_x < W:
        DS.blit(bg, (rel_x, 0))
    if rel_y > H:
        DS.blit(bg, (rel_x, 0))

    # creates player object (i.e the white circle)
    pygame.draw.circle(DS, WHITE, (int(circlePosX), playerPosY - circleRadius), circleRadius, 0)

    pygame.display.update()
    CLOCK.tick(FPS)
    DS.fill(BLACK)
