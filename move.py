import pygame
#importing the gaming library
pygame.init()
#calling the initialisation function of pygame library - constructor function

width = 600
height = 600
#width and height of the output window

screen = pygame.display.set_mode((width, height))
#setup the screen as per window width and height

pygame.display.update()
colour = ("white")
x = 60
y = 60
squarewdth = 70
squareheight = 70
while True:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            exit()
    keypress = pygame.key.get_pressed()
    #when a key is pressed it takes note of which key was pressed
    if keypress[pygame.K_LEFT]:
        x = x-0.3
    if keypress[pygame.K_RIGHT]:
        x=x+0.3    
    if keypress[pygame.K_UP]:
            y=y-0.3 
    if keypress[pygame.K_DOWN]:
                y=y+0.3 
    if x<0:
          x = 10
          colour = ("red")
    if x>530:
          x = 520
          colour = ("orange")
    if y<0:
          y = 10
          colour = ("yellow")
    if y>530:
          y = 520
          colour = ("green")
    screen.fill("black")  
    pygame.draw.rect(screen, (colour), pygame.Rect(x,y,squarewdth , squareheight))
    pygame.display.update()