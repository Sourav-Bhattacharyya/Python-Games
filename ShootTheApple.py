import pgzrun
import pygame
import time
from random import randint
apple = Actor("apple.png") 
font = pygame.font.SysFont(None, 50)
text1 = font.render("Good Shot", True, (0, 0, 0))
text2 = font.render("You Missed", True, (0, 0, 0))
def draw():
    screen.clear()
    apple.draw()

def place_apple():
    apple.x = randint(10,500)
    apple.y = randint(10,600)

def on_mouse_down(pos):
    if apple.collidepoint(pos):
        screen.blit(text1, (20,140))
        place_apple()
    else:
        screen.clear()
        screen.blit(text2, (30,40))
        screen.blit(font.render("Do You want to quit?", True, (0, 0, 0)),(40,40))
        pygame.display.flip()
        time.sleep(2)
        quit()

place_apple()
pgzrun.go()