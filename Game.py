# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((700, 327))
clock = pygame.time.Clock()
running = True

image = pygame.image.load("E:/cours/NSI/projet/Black Jack/Black-Jack-Python/Card Asset/Tables/table_green.png.png").convert_alpha()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    screen.blit(image,(700,327))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame


    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60
pygame.quit()