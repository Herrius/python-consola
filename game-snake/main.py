import random
import pygame


pygame.init()
tomato=(255,99,71)
white=(255,255,255)
screen_width=800
screen_height=800
screen=pygame.display.set_mode((screen_width,screen_height))
icon = pygame.image.load('favicon.ico')
pygame.display.set_icon(icon)
pygame.display.set_caption('🐍 Juego Snake 🐍')
game_over=False
#controla el tiempo de actualizacion
clock = pygame.time.Clock()
snake_speed=30

font_style = pygame.font.SysFont(None, 50)
font = pygame.font.SysFont("comicsansms", 35)

def score(points):
    value = font.render("Your Score: " + str(points), True, (160,120,90))
    screen.blit(value, [10, 10])

def message(msg,color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [90, 110])
class Snake():
    def __init__(self):
        self.color= white
        self.width=10
        self.height=10
        self.length=1
        self.x_ini=screen_width/2
        self.y_ini=screen_height/2
        self.body=[[self.x_ini,self.y_ini]]

    def draw(self,canva):
        for x in self.body:
            pygame.draw.rect(canva,self.color,[x[0],x[1],self.width,self.height])

class Food(Snake):
    def __init__(self):
        super().__init__()
        self.color=tomato
    

def game_loop():
    snake_move=10

    x_update=0
    y_update=0

    game_over = False
    game_close = False

    snake=Snake()
    foodx = random.randint(1, 79)*10
    foody = random.randint(1, 79)*10 
    while not game_over:
        while game_close == True:
            screen.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", (120,160,120))
            score(snake.length-1)
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
        if snake.x_ini >= screen_width or snake.x_ini < 0 or snake.y_ini >= screen_height or snake.y_ini < 0:
            game_close = True
        #limpiar venta
        screen.fill((0,0,0))
        pygame.draw.rect(screen,tomato,[foodx,foody,10,10])
        snake_head=[]
        snake.x_ini+=x_update
        snake.y_ini+=y_update
        snake_head.append(snake.x_ini)
        snake_head.append(snake.y_ini)
        snake.body.append(snake_head)
        if len(snake.body) > snake.length:
            del snake.body[0]

        for x in snake.body[:-1]:
            if x == snake_head:
                game_close = True
        snake.draw(screen)
        score(snake.length-1)
        pygame.display.update()

        clock.tick(30)
        if snake.x_ini == foodx and snake.y_ini == foody:
            foodx = random.randint(1, 79)*10
            foody = random.randint(1, 79)*10 
            snake.length += 1
    pygame.quit()
    quit()

game_loop()