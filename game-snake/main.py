#Necesario para las teclas presionadas
from pygame.locals import *
import pygame
import sys

pygame.init()
#Establecemos el tamaño de la ventana.
ventana = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()
#podemos ponerle titulo a nuestra ventana, entre otras cosas,
pygame.display.set_caption("🐍 Juego Snake 🐍")

class Snake():

    def __init__(self):
        self.size=pygame.Rect((300,300),(10,30))
        

    def draw_snake(self):
        pygame.draw.rect(ventana,(255,255,255),self.size)
        
    def move(self,x,y):
        self.size.move_ip(x,y)
        pygame.draw.rect(ventana,(255,255,255),self.size)

snake=Snake()

#Bucle de "Juego"
while True:
    dt = clock.tick(30) / 1000

    for event in pygame.event.get():    #Cuando ocurre un evento...

            
        if event.type == pygame.KEYDOWN:
            #Obtenemos el mapping de teclas presionadas
            keys = pygame.key.get_pressed()
            if keys[K_w] or keys[K_UP]:
                #Rellenamos la ventana con un color de Pygame
                snake.move(0,-10)
            if keys[K_a] or keys[K_LEFT]:
                snake.move(10,0)
            if keys[K_d] or keys[K_RIGHT]:
                snake.move(-10,0)
            if keys[K_s] or keys[K_DOWN]:
                snake.move(0,10)

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ventana.fill((0, 0, 0)) 
    snake.draw_snake()
    pygame.display.update() 
