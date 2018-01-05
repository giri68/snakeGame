# Snake Game!!!
# imports
import pygame, sys, random, time

# initilizing errors
check_errors = pygame.init()
if check_errors[1] > 0:
  print("Had {0} errors, exiting...".format(check_errors[1]))
  sys.exit(-1)
else:
  print("The game successfully initialized")

  # play surface
pygame.display.set_caption('Snake Game')
playSurface = pygame.display.set_mode((720, 460))
  
# pygame.display.set_caption('Snake Game')
Dwidth = 720
Dheight = 460

time.sleep(1)

#colors
red = pygame.Color(255, 0, 0) # game over
green = pygame.Color(0, 255, 0) # snake
blue = pygame.Color(0, 0, 255)
black = pygame.Color(0, 0, 0 ) # score
white = pygame.Color(255, 255, 255) # background
brown = pygame.Color(165, 42, 42) # food

# FPS controller

fpsController = pygame.time.Clock()

# snak variables
snakePos = [100, 50]
snakeBody = [[100, 50], [90, 50], [80, 50]]
foodPos = [random.randrange(1, 72)*10, random.randrange(1, 46)*10]

foodSpawn = True


direction = 'RIGHT'
changeto = direction

score = 0
icon = pygame.image.load('apple.png')
pygame.display.set_icon(icon)

Logo = pygame.image.load('snakelogo.png')

appleimg = pygame.image.load('apple.png')

img = pygame.image.load('snake.png')
tail = pygame.image.load('snake.png')

blocks = 20
AppleThickness = 30

background_image = pygame.image.load('test.png').convert()
background_image = pygame.transform.scale(background_image, (720, 460))
background_position = (0,0)
click_sound = pygame.mixer.Sound('Saito_Koji_-_08_-_One_Minute_For_The_Sun.ogg')
click_sound.play()

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)
# pygame.mixer.music.load('laser5.ogg')
# pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
# pygame.mixer.music.play()

def pause():
  paused = True
  message("Paused", black, -100, size="large")
  message("Press SPACE again to continue or Q to quit.", black, 25)
  pygame.display.update()
  while paused:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()

      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
          paused = False

        elif event.key == pygame.K_q:
          pygame.quit()
          quit()

    fpsController.tick(5)
foodPos = [random.randrange(1, 72)*10, random.randrange(1, 46)*10]

# def randAppleGen():
#     randAppleX = round(random.randrange(0,Dwidth-AppleThickness))#/10.0)*10.0
#     randAppleY = round(random.randrange(0,Dheight-AppleThickness))#/10.0)*10.0

#     return randAppleX,randAppleY
def randAppleGen():
    randAppleX = random.randrange(1, 72)*10
    randAppleY = random.randrange(1, 46)*10

    return randAppleX,randAppleY
randAppleX,randAppleY = randAppleGen()

def game_intro():
    intro = True

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        playSurface.fill(green)
        playSurface.blit(Logo,[0,100,800,170])

        message("The objective of the game is to eat red apples,",
                black,
                -30)
        message("the more apples you eat the longer you get and",
                black,
                10)
        message("if you run into yourself or the edges you die.",
                black,
                50)
        message("Press C to play, SPACE to pause, or Q to quit.",
                black,
                180)
        pygame.display.update()
        fpsController.tick(15)

def text_objects(text,color,size):
    if size == "small":
        textSurface = smallfont.render(text,True,color)
    elif size == "medium":
        textSurface = medfont.render(text,True,color)
    elif size == "large":
        textSurface = largefont.render(text,True,color)

    return textSurface, textSurface.get_rect()


def message(msg,color,y_displace=0, size = "small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = (Dwidth/2),(Dheight/2) +y_displace
    playSurface.blit(textSurf,textRect)

# Game over function
def gameOver():
  myFont = pygame.font.SysFont('monaco', 72)
  GOsurf = myFont.render('Game Over!', True, red)
  GOrect = GOsurf.get_rect()
  GOrect.midtop = (360, 15)
  playSurface.blit(GOsurf, GOrect)
  showScore(0)
  pygame.display.flip()
  time.sleep(2)
  pygame.quit() # pygame exit
  sys.exit() # console exit



def showScore(choice=1):
  sFont = pygame.font.SysFont('monaco', 40)
  Ssurf = sFont.render('Score : {0}'.format(score), True, white)
  Srect = Ssurf.get_rect()
  if choice == 1:
    Srect.midtop = (80, 10)
  else:
    Srect.midtop = (360, 120)
  playSurface.blit(Ssurf, Srect)
  

    


game_intro()
# Main logic of the game
randAppleX,randAppleY = randAppleGen()
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT or  event.key == ord('d'):
        changeto = 'RIGHT'
      if event.key == pygame.K_LEFT or  event.key == ord('a'):
        changeto = 'LEFT'
      if event.key == pygame.K_UP or  event.key == ord('w'):
        changeto = 'UP'
      if event.key == pygame.K_DOWN or  event.key == ord('s'):
        changeto = 'DOWN'
      if event.key == pygame.K_ESCAPE: 
        pygame.event.post(pygame.event.Event(pygame.QUIT))

  
  
  # validation of direction
  if changeto == 'RIGHT' and not direction == 'LEFT':
    direction = 'RIGHT'
  if changeto == 'LEFT' and not direction == 'RIGHT':
    direction = 'LEFT'
  if changeto == 'UP' and not direction == 'DOWN':
   direction = 'UP'
  if changeto == 'DOWN' and not direction == 'UP':
    direction = 'DOWN'
  

  if direction == 'RIGHT':
    snakePos[0] += 10
  if direction == 'LEFT':
    snakePos[0] -= 10
  if direction == 'UP':
   snakePos[1] -= 10
  if direction == 'DOWN':
   snakePos[1] += 10
  

       
  # Snake body mechanism
  snakeBody.insert(0, list(snakePos))
  if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
    score += 1
    foodSpawn = False
  else:
   snakeBody.pop()

  if foodSpawn == False:
    foodPos = [random.randrange(5, 70)*10, random.randrange(5, 45)*10]
    foodSpawn = True

  
  # if snakePos[0] == randAppleX and snakePos[1] == randAppleY:
  #   score += 1
  #   foodSpawn = False
  # else:
  #  snakeBody.pop()

  # if foodSpawn == False:
  #   foodPos = 
  #   foodSpawn = True

  

  # Background
  playSurface.fill(blue)

  
  playSurface.blit(background_image, background_position)
  showScore()
  #Draw Snake
  for pos in snakeBody:
    pygame.draw.rect(playSurface, green, pygame.Rect(pos[0],pos[1],10,10))

  
  
  #pygame.draw.rect(playSurface, brown, pygame.Rect(foodPos[0],foodPos[1],10,10))

  playSurface.blit(appleimg,(foodPos[0], foodPos[1]))
  

  

  if snakePos[0] > 710 or snakePos[0] < 0:
   gameOver()
  if snakePos[1] > 450 or snakePos[1] < 0:
    gameOver()

  for block in snakeBody[1:]:
    if snakePos[0] == block[0] and snakePos[1] == block[1]:
      gameOver()
      
  
  
  pygame.display.flip()
  fpsController.tick(15)
  


    
    

