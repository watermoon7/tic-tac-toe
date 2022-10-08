import pygame
import sys

pygame.init()

def printgrid():
    global grid
    print(grid[0])
    print(grid[1])
    print(grid[2])

def winner(grid, playerturn):
    global gamerunning, draw
    if playerturn == 2:
        winner = 1
        winnername = 'Crosses'
    else:
        winner = 2
        winnername = 'Circles'
    winner1 = False
    if grid[0][0] == winner and grid[0][1] == winner and grid[0][2] == winner:
        print("{} WIN".format(winnername))
        winner1 = True
    if grid[1][0] == winner and grid[1][1] == winner and grid[1][2] == winner:
        print("{} WIN".format(winnername))
        winner1 = True
    if grid[2][0] == winner and grid[2][1] == winner and grid[2][2] == winner:
        print("{} WIN".format(winnername))
        winner1 = True
    if grid[0][0] == winner and grid[1][0] == winner and grid[2][0] == winner:
        print("{} WIN".format(winnername))
        winner1 = True
    if grid[0][1] == winner and grid[1][1] == winner and grid[2][1] == winner:
        print("{} WIN".format(winnername))
        winner1 = True
    if grid[0][2] == winner and grid[1][2] == winner and grid[2][2] == winner:
        print("{} WIN".format(winnername))
        winner1 = True
    if grid[0][0] == winner and grid[1][1] == winner and grid[2][2] == winner:
        print("{} WIN".format(winnername))
        winner1 = True
    if grid[2][0] == winner and grid[1][1] == winner and grid[0][2] == winner:
        print("{} WIN".format(winnername))
        winner1 = True

    check = 0
    for i in range(0, 3):
        for o in range(0, 3):
            check += int(grid[i][o])

    if winner1 == True:
        gamerunning = False
    elif check == 13 or check == 14:
        draw = True
        gamerunning = False
    
def drawgrid(playerturn, centers):
    a = 0
    for i in range(0, 3):
        for o in range(0, 3):
            if grid[i][o] == 1:
                x, y = centers[a]
                pygame.draw.line(screen,black,(x-50,y-50),(x+50,y+50),width=10)
                pygame.draw.line(screen,black,(x+50,y-50),(x-50,y+50),width=10)
            a += 1
    a = 0
    for i in range(0, 3):
        for o in range(0, 3):
            if grid[i][o] == 2:
                x, y = centers[a]
                pygame.draw.circle(screen,black,(x,y),50,width=10)
            a += 1

def user_names():
    global name1, name2
    name1 = str(input("On the X side:"))
    name2 = str(input("In the O corner:"))

#coluors
white = (255,255,255)
black = (0,0,0)
turquoise = (105,223,170)
lightpurple = (215,109,219)

#constants
width = 1
playerturn = 1
centers = [
    [100,100],
    [300,100],
    [500,100],
    [100,300],
    [300,300],
    [500,300],
    [100,500],
    [300,500],
    [500,500],
    ]

#fonts
font1 = pygame.font.Font('Mangabey.otf', 50)
font2 = pygame.font.Font('Mangabey.otf', 100)
font3 = pygame.font.Font('Mangabey.otf', 20)
font4 = pygame.font.Font('Mangabey.otf', 40)
font5 = pygame.font.Font('Mangabey.otf', 30)

#game variables
name1 = ""
name2 = ""
currentname = ""
draw = False
screen = pygame.display.set_mode((600, 700))
pygame.display.set_caption('Tic Tac Toe')
gamerunning = True
clock = pygame.time.Clock()
grid = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
    ]
start = True
playernumber = 1
user_text = ""
XorO = ["On the X side", "In the O corner"]

#start screen
while start == True:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #used for typing
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                elif event.key != pygame.K_RETURN:
                    user_text += event.unicode
                if event.key == pygame.K_RETURN and len(user_text) > 0 and playernumber == 1:
                    name1 = user_text
                    user_text = ""
                    playernumber = 2
                elif event.key == pygame.K_RETURN and len(user_text) > 0 and playernumber == 2:
                    name2 = user_text
                    start = False
                
    screen.fill(lightpurple)
    entertext = font1.render("{}: ".format(XorO[playernumber-1]),False,'Black')
    entertextrect = entertext.get_rect(center=(300,300))
    screen.blit(entertext, entertextrect)

    if len(user_text) > 30:
        user_text = user_text[:30]
    box = pygame.draw.rect(screen,black,(100, 350, 400, 50),width=5)
    boxtext = font4.render("{}".format(user_text),False,'Black')
    boxtextrect = boxtext.get_rect(center=(300,375))
    screen.blit(boxtext, boxtextrect)
    
    
    pygame.display.update()
    clock.tick(60)

currentname = name1

#main loop    
while True:
    draw = False
    while gamerunning == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #every if statememt removes and inserts 1s and 2s representing the player whose turn it is and where they picked
            if event.type == pygame.MOUSEBUTTONDOWN:
                posx, posy = pygame.mouse.get_pos()
                if posx > 1 and posy > 1 and posx < 199 and posy < 199 and grid[0][0] == 0:
                    grid[0].pop(0)
                    grid[0].insert(0, playerturn)
                    if currentname == name1:
                        currentname = name2
                    else:
                        currentname = name1
                    if playerturn == 1:
                        playerturn = 2
                    else:
                        playerturn = 1
                if posx > 201 and posy > 1 and posx < 399 and posy < 199 and grid[0][1] == 0:
                    grid[0].pop(1)
                    grid[0].insert(1, playerturn)
                    if currentname == name1:
                        currentname = name2
                    else:
                        currentname = name1
                    if playerturn == 1:
                        playerturn = 2
                    else:
                        playerturn = 1
                if posx > 401 and posy > 1 and posx < 599 and posy < 199 and grid[0][2] == 0:
                    grid[0].pop(2)
                    grid[0].insert(2, playerturn)
                    if currentname == name1:
                        currentname = name2
                    else:
                        currentname = name1
                    if playerturn == 1:
                        playerturn = 2
                    else:
                        playerturn = 1
                if posx > 1 and posy > 201 and posx < 199 and posy < 399 and grid[1][0] == 0:
                    grid[1].pop(0)
                    grid[1].insert(0, playerturn)
                    if currentname == name1:
                        currentname = name2
                    else:
                        currentname = name1
                    if playerturn == 1:
                        playerturn = 2
                    else:
                        playerturn = 1
                if posx > 201 and posy > 201 and posx < 399 and posy < 399 and grid[1][1] == 0:
                    grid[1].pop(1)
                    grid[1].insert(1, playerturn)
                    if currentname == name1:
                        currentname = name2
                    else:
                        currentname = name1
                    if playerturn == 1:
                        playerturn = 2
                    else:
                        playerturn = 1
                if posx > 401 and posy > 201 and posx < 599 and posy < 399 and grid[1][2] == 0:
                    grid[1].pop(2)
                    grid[1].insert(2, playerturn)
                    if currentname == name1:
                        currentname = name2
                    else:
                        currentname = name1
                    if playerturn == 1:
                        playerturn = 2
                    else:
                        playerturn = 1
                if posx > 1 and posy > 401 and posx < 199 and posy < 599 and grid[2][0] == 0:
                    grid[2].pop(0)
                    grid[2].insert(0, playerturn)
                    if playerturn == 1:
                        playerturn = 2
                    else:
                        playerturn = 1
                    if currentname == name1:
                        currentname = name2
                    else:
                        currentname = name1
                if posx > 201 and posy > 401 and posx < 399 and posy < 599 and grid[2][1] == 0:
                    grid[2].pop(1)
                    grid[2].insert(1, playerturn)
                    if playerturn == 1:
                        playerturn = 2
                    else:
                        playerturn = 1
                    if currentname == name1:
                        currentname = name2
                    else:
                        currentname = name1
                if posx > 401 and posy > 401 and posx < 599 and posy < 599 and grid[2][2] == 0:
                    grid[2].pop(2)
                    grid[2].insert(2, playerturn)
                    if playerturn == 1:
                        playerturn = 2
                    else:
                        playerturn = 1
                    if currentname == name1:
                        currentname = name2
                    else:
                        currentname = name1
                if restartbox.collidepoint(pygame.mouse.get_pos()):
                    grid = [
                        [0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0]
                        ]
                if exitbox.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()
                    
        #drawing the grid
        screen.fill(white)
        line1 = pygame.draw.line(screen,black,(200,0),(200,600),width=3)
        line2 = pygame.draw.line(screen,black,(400,0),(400,600),width=3)
        line3 = pygame.draw.line(screen,black,(0,200),(600,200),width=3)
        line4 = pygame.draw.line(screen,black,(0,400),(600,400),width=3)
        line5 = pygame.draw.line(screen,black,(0,600),(600,600),width=3)
        restartbox = pygame.draw.rect(screen, black, (450, 625, 100, 50), width=5)
        restarttext = font3.render("Restart Board",False,'Black')
        restarttextrect = restarttext.get_rect(center=(500,650))
        screen.blit(restarttext, restarttextrect)
        exitbox = pygame.draw.rect(screen, black, (50, 625, 100, 50), width=5)
        exittext = font5.render("Exit",False,'Black')
        exittextrect = exittext.get_rect(center=(100,650))
        screen.blit(exittext, exittextrect)
        #drawing the grid every move
        drawgrid(playerturn, centers)
        #drawing the info text
        infotext = font1.render("{}'s turn".format(currentname),False,'Black')
        infotextrect = infotext.get_rect(center=(300,650))
        screen.blit(infotext, infotextrect)
        
        #checking for a winner
        winner(grid, playerturn)
        
        pygame.display.update()
        clock.tick(60)

    #swapping the players around for correct winner
    if currentname == name1:
        currentname = name2
    elif currentname == name2:
        currentname = name1
            
    while gamerunning == False:
        grid = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
            ]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    gamerunning = True
        #drawing things
        screen.fill(turquoise)
        if draw == False:
            newgametext = font2.render("{} WINS!".format(currentname),False,'Black')
            newgametextrect = newgametext.get_rect(center=(300,250))
            screen.blit(newgametext, newgametextrect)
        else:
            newgametext = font2.render(("DRAW!"),False,'Black')
            newgametextrect = newgametext.get_rect(center=(300,250))
            screen.blit(newgametext, newgametextrect)
        extratext = font1.render("Press N to play again".format(playerturn),False,'Black')
        extratextrect = extratext.get_rect(center=(300,375))
        screen.blit(extratext, extratextrect)
        
        pygame.display.update()
        clock.tick(60)
