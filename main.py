# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():
    pygame.init()
    
    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    player = Player(x, y)
    
    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for thing in updateable:
            thing.update(dt)

        screen.fill((0,0,0))

        for thing in drawable:
            thing.draw(screen)
        
        pygame.display.flip()

        # limit frame rate to 60
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
