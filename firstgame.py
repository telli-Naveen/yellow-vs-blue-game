import pygame
pygame.init()
#Size of screen
screen=pygame.display.set_mode((800,600))


#loading image yellow and position of yellow
yellowimage=pygame.image.load('yellow.png')
yellowX=0
yellowY=300

#creting function for yellow img calling the fun while running
def yellow():
    screen.blit(yellowimage,(yellowX,yellowY))

running=True
while running:
    screen.fill((0,0,255))
    for e in pygame.event.get():
      if e.type == pygame.KEYDOWN:
       if e.key==pygame.K_KP_4 or e.key==pygame.K_KP_5:
          yellowY=yellowY-10
       if yellowY<=0:
           print('YELLOW IS WIN')
           running=False
       if e.key==pygame.K_a or e.key==pygame.K_s:
           yellowY=yellowY+10
       if yellowY>=600:
           print('BLUE IS WIN.')
           running=False
      elif e.type==pygame.QUIT:
        running=False

    yellow()

    pygame.display.update()
