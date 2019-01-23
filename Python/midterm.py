# Engineering_4_Midterm
import pygame
import time
from random import randint

(WIDTH, HEIGHT) = (640, 640)
background_color = (255,255,255)
black = (0,0,0)
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Midterm")
screen.fill(background_color)

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = None
        if event.type == pygame.KEYDOWN:
            startTime = time.time()
            for i in range (0,640):
                for j in range (0,640):
                    color = (randint(0,255),randint(0,255),randint(0,255))
                    screen.set_at((i,j),color)
            print("This generation took %f seconds to run." %(time.time()-startTime))
            pygame.display.flip()
            
pygame.quit()
