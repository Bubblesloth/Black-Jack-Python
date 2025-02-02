# Example file showing a basic pygame "game loop"
import os
import pygame


uri = os.path.join(os.path.dirname(__file__),  "table_green.png")

# pygame setup
pygame.init()
screen = pygame.display.set_mode((700, 327))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    fond = pygame.image.load(uri).convert()

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60