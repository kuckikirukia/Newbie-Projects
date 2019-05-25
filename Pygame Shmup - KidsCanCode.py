# Shmup game
import pygame
import random
import os

WIDTH = 480
HEIGHT = 600
FPS = 60

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shmup Game")
clock = pygame.time.Clock()
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # necessary
        self.image = pygame.image.load(os.path.join(img_folder, "yian.jpg")).convert()
        self.rect = self.image.get_rect()  # necessary
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10  # sets where the player will spawn
        self.speedx = 0  # control the speed that the sprite will move
        self.speedy = 0

    def update(self):
        self.speedx = 0  # set player speed to be 0 if no movement keys are press, otherwise
        self.speedy = 0
        keystate = pygame.key.get_pressed()  # if key pressed, the player would keep moving
        if keystate[pygame.K_LEFT]:
            self.speedx = -5
        if keystate[pygame.K_RIGHT]:
            self.speedx = 5
        if keystate[pygame.K_UP]:
            self.speedy = -5
        if keystate[pygame.K_DOWN]:
            self.speedy = 5

        self.rect.x += self.speedx  # updates the speed that the sprite will move in x
        self.rect.y += self.speedy  # same as above but for y
        if self.rect.right > WIDTH:  # prevents player from moving out of screen
            self.rect.right = WIDTH  # if the rect ever moves out of width, it will be @ width
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)  # bullet will spawn at x, y of the player
        all_sprites.add(bullet)
        bullets.add(bullet)


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 8)

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, 40)
            self.speedy = random.randrange(1, 8)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):  # x, y is the coordinate where the bullet will spawn (i.e where the player is)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        # kill if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()


all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

for i in range(12):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:  # shoot the bullets
            if event.key == pygame.K_SPACE:
                player.shoot()

    # Update
    all_sprites.update()

    # check to see if a mob hit the player
    hits = pygame.sprite.spritecollide(player, mobs, False)  # check target against which group - return a list of mobs that are hit
    if hits:
        running = False  # if hit is True, then game will end

    # check to see if a bullet hit a mob
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True )  # True to remove, if mob gets hit
    for hit in hits:  # spawn more mobs when killed; otherwise it'll run out
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)

    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()