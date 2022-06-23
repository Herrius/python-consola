from audioop import tomono
import time,random
import pygame
pygame.init()
screen_width=800
screen_height=800
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.update()
icon = pygame.image.load('../favicon.ico')
pygame.display.set_icon(icon)
pygame.display.set_caption('🐍 Juego Snake 🐍')
game_over=False
white=(255,255,255)
tomato=(255,99,71)
snake_move=10


#controla el tiempo de actualizacion
clock = pygame.time.Clock()
snake_speed=30

font_style = pygame.font.SysFont(None, 50)

def message(msg,color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [screen_width/4, screen_height/4])
class Snake():
    def __init__(self):
        self.color= white
        self.x_ini=screen_width/2
        self.y_ini=screen_height/2
        self.width=10
        self.height=10

    def draw(self,canva,x=0,y=0):
        self.x_ini+=x
        self.y_ini+=y
        pygame.draw.rect(canva,self.color,[self.x_ini,self.y_ini,self.width,self.height])

class Food(Snake):
    def __init__(self):
        super().__init__()
        self.color=tomato
    

def game_loop():
    x_update=0
    y_update=0

    game_over = False
    game_close = False

    snake=Snake()
    foodx = random.randint(10, 790)
    foody = random.randint(10, 790) 
    while not game_over:
        while game_close == True:
            screen.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", (120,160,120))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    x_update = -snake_move
                    y_update = 0
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    x_update = snake_move
                    y_update = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    y_update = -snake_move
                    x_update = 0
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    y_update = snake_move
                    x_update = 0
                elif event.key == pygame.K_r:
                    game_close = True

        #limpiar venta
        screen.fill((0,0,0))
        pygame.draw.rect(screen,tomato,[foodx,foody,10,10])
        snake.draw(screen,x_update,y_update)
        message("You lost",(124,124,124))
        pygame.display.update()
        if snake.x_ini == foodx and snake.y_ini == foody:
            print("Yummy!!")
        clock.tick(30)
    pygame.quit()
    quit()

game_loop()