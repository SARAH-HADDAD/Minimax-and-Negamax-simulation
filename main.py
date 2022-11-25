import pygame
import button

pygame.init()

#create game window
SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 760

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

#game variables
game_paused = False
menu_state = "main"

#define fonts
font = pygame.font.SysFont("arialblack", 40)

#define colours
TEXT_COL = (255, 255, 255)

#load button images

MiniMax_img=pygame.image.load("images/MiniMax.png")
NegaMax_img=pygame.image.load("images/NegaMax.png")
NegaMaxWithAlphaBeta_img=pygame.image.load("images/NegaMax with Alpha-Beta Pruning.png")
#create button instances
MiniMax_button=button.Button((1300/2)-(MiniMax_img.get_width()/2),760/4,MiniMax_img,1)
NegaMax_button=button.Button((1300/2)-(NegaMax_img.get_width()/2),760/2,NegaMax_img,1)
NegaMaxWithAlphaBeta_button=button.Button((1300/2)-(NegaMaxWithAlphaBeta_img.get_width()/2),(760*3)/4,NegaMaxWithAlphaBeta_img,1)
def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

#game loop
run = True
while run:

  screen.fill((52, 78, 91))
  if MiniMax_button.draw(screen):  print("minmax")
  if NegaMax_button.draw(screen):   print("nigamax")
  if NegaMaxWithAlphaBeta_button.draw(screen):   print("alpha beta")


  #event handler
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        game_paused = True
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()

pygame.quit()