import pygame
import random
pygame.init()
#colors
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
width=600
height=400
clock=pygame.time.Clock()
fps=60
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption('Snake')
run=True
#Snake
snake_x=300
snake_y=200
snake_size=20
velocity_x=0
velocity_y=0
initial_velocity=4
head=[]
snake_list=[]
snake_length=1

#Food
food_x=random.randint(20,width-20)
food_y=random.randint(20,height-20)
food_size=20
score=0
#font
font=pygame.font.SysFont(None,50)
def render_font(text,color,x,y):
    img=font.render(text,True,color)
    screen.blit(img,(x,y))
def plot_snake(gameWindow,color,snake_list,snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow, color, [x,y,snake_size, snake_size])

while run :
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                velocity_x=initial_velocity
                velocity_y=0
            if event.key==pygame.K_LEFT:
               velocity_x = (-initial_velocity)
               velocity_y=0
            if event.key==pygame.K_UP:
                 velocity_x=0
                 velocity_y= -initial_velocity
            if event.key==pygame.K_DOWN:
               velocity_x=0
               velocity_y=initial_velocity
    snake_x=snake_x+ velocity_x
    snake_y=snake_y+velocity_y
    if abs(snake_x-food_x)<10 and abs(snake_y-food_y)<10:
        score=score +10
        food_x=random.randint(20,width-20)
        food_y=random.randint(20,height-20)

        snake_length =snake_length +5

                                                 

    screen.fill(white)
   # render_font('SCORE : ' + str(score), red, 10,10)
    head=[]
    head.append(snake_x)
    head.append(snake_y)
    snake_list.append(head)

    if len(snake_list)>snake_length:
      del snake_list[0]
    if head in snake_list[ :-1]:
        run = False

    if snake_x < 0 or snake_x > width or snake_y < 0 or snake_y > height:
        run= False

    render_font("Score:" + str(score), red, 10,10)
    #pygame.draw.rect(screen,black,[snake_x,snake_y,snake_size,snake_size])
    plot_snake(screen, black,snake_list, snake_size)
    pygame.draw.rect(screen,red,[food_x,food_y,food_size,food_size])

    pygame.display.update()
    clock.tick(fps)
pygame.quit()
quit()





