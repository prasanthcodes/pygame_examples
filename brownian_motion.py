import pygame
import random
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

#---input params---
fps_rate=100
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
max_time=1e3


N_particles=100
radius=3
particle_color=(0, 0, 255)

#---create initial positions of particles-----
xpos=[]
ypos=[]
if N_particles<2:
    x=int(SCREEN_WIDTH/2.0)
    y=int(SCREEN_HEIGHT/2.0)
    xpos.append(x)
    ypos.append(y)
else:
    for i in range(N_particles):
        x=int(SCREEN_WIDTH*random.random())
        y=int(SCREEN_HEIGHT*random.random())
        xpos.append(x)
        ypos.append(y)


#---initializations-------
pygame.init()
# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
time_count=1
running = True
clock = pygame.time.Clock()

while running:

    #----window closing conditions-------
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False
        if time_count > max_time:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    for i in range(N_particles):
        #---x,y points----
        xpos[i] = xpos[i] + int(3*random.random())-1
        ypos[i] = ypos[i] + int(3*random.random())-1
        # Draw a solid blue circle
        c1=pygame.draw.circle(screen, particle_color, (xpos[i],ypos[i]),radius)
    pygame.display.flip()
    time_count+=1

    clock.tick(fps_rate)
    fps=clock.get_fps()
    # # ---save screenshot---
    # pygame.image.save(screen, "screenshot.png")

pygame.quit()



