import pygame, sys, random

#Gernal
pygame.init()
clock = pygame.time.Clock()


#Constants
WIDTH = 600
HEIGHT = 900
FPS = 60
BG_COLOR = (27, 72, 199)
TXT_COLOR = (228, 201, 52)

#Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Schere, Stein, Papier")
screen.fill(BG_COLOR)


#Objects
rock = pygame.image.load("c:\\temp\\Rock.png")
paper = pygame.image.load("c:\\temp\\Paper.png")
scissor = pygame.image.load("c:\\temp\\Scissor.png")
player = ""
computer = ""
rect = pygame.Rect(400, 220, 160, 100)

#Functions
def draw():
    global rock, paper, scissor
    rock = pygame.transform.scale(rock, (100, 179) ) 
    paper = pygame.transform.scale(paper, (100, 179) ) 
    scissor = pygame.transform.scale(scissor, (100, 179) ) 
    screen.blit(rock, (50, 600) )
    screen.blit(paper, (250, 600) )
    screen.blit(scissor, (450, 600) )
def computer_choice():
    global computer
    choices = ["rock", "paper", "scissor"]
    computer = "".join(random.choices(choices))


    if computer == "rock":
        rock1 = pygame.transform.flip(rock, False, True)
        screen.blit(rock1, (250, 50) )
    elif computer == "paper":
        paper1 = pygame.transform.flip(paper, False, True)
        screen.blit(paper1, (250, 50) )
    elif computer == "scissor":
        scissor1 = pygame.transform.flip(scissor, False, True)
        screen.blit(scissor1, (250, 50) )
def game(player, computer):
    font = pygame.font.SysFont(None, 50)
    player_txt = font.render("    Player:", True, TXT_COLOR)
    computer_txt = font.render("Computer:", True, TXT_COLOR)
    screen.blit(player_txt, (50, 370) )
    screen.blit(computer_txt, (50, 150) )
    pygame.draw.rect(screen, BG_COLOR, rect)
    
    if player == computer:
        txt = font.render("     Tie", True, TXT_COLOR)
        screen.blit(txt, (400, 260) )
    elif (player == "rock" and computer == "scissor") or (player == "scissor" and computer == "paper") or (player == "paper" and computer == "rock"):
        txt = font.render(" You win", True, TXT_COLOR)
        screen.blit(txt, (400, 260) )
    else: 
        txt = font.render(" You lost", True, TXT_COLOR)
        screen.blit(txt, (400, 260) )


#Main Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            inputX = event.pos[0]
            inputY = event.pos[1]

            if inputX >= 50 and inputX <= 150 and inputY >= 600 and inputY <= 800:
                player = "rock"
                screen.blit(rock, (250, 300) )
            elif inputX >= 250 and inputX <= 350 and inputY >= 600 and inputY <= 800:
                player = "paper"
                screen.blit(paper, (250, 300) )
            elif inputX >= 450 and inputX <= 550 and inputY >= 600 and inputY <= 800:
                player = "scissor"
                screen.blit(scissor, (250, 300) ) 
            else:
                player = ""

            if player != "":
                computer_choice()
                game(player, computer)

    draw()

    pygame.display.update()
    clock.tick(FPS)