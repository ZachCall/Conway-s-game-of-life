import pygame
import numpy as np

# colours
dark_grey = (32,32,32)
black = (0, 0, 0)
white = (255, 255, 255)
green = (0,128,0)
red = (255,0,0)
dark_green = (0,100,0)
dark_red = (139, 0, 0)
grey = (128,128,128)

def blankBoard(height, width):
    board = np.zeros((width +100, height+100))
    return board

def drawBoard(screen, currentMatrix, grid, width, height, y_offset, cellsize):
    pygame.draw.rect(screen, dark_grey, (0, y_offset*cellsize, width*cellsize, height*cellsize))

    for x in range(currentMatrix.shape[0]-100):
        for y in range(currentMatrix.shape[1]-100):
            if (y < height):
                if (x == 0 or x == 1 or x == width - 1 or x == width - 2):
                    if (x == 1 and grid):
                        pygame.draw.rect(screen, black, (x  * cellsize, (y + y_offset)* cellsize, cellsize-1, cellsize))
                    else:
                        pygame.draw.rect(screen, black, (x  * cellsize, (y + y_offset)* cellsize, cellsize, cellsize))
                
                else:
                    colour = black

                    if (currentMatrix[x][y] == 1):
                        colour = white
                    
                    if (grid):
                        pygame.draw.rect(screen, colour, (x * cellsize, (y+ y_offset)* cellsize, cellsize-1, cellsize-1))
                    else:
                        pygame.draw.rect(screen, colour, (x  * cellsize, (y + y_offset)* cellsize, cellsize, cellsize))

def drawUI(screen, height, width, button_size, space_size, cellsize, generation):
    # title
    title = pygame.image.load ("images/title.png")
    title = pygame.transform.scale(title ,(int(width*0.5*cellsize),int(height*0.1*cellsize)))
    screen.blit(title, (int(width*0.25*cellsize),int(height*cellsize*0.02)))

    # generations
    smallfont = pygame.font.SysFont('arial.ttf',35)
    text = smallfont.render("Generation: "+ str(generation), True , white)
    position  = text.get_width()
    screen.blit(text, (width*cellsize*0.99-position, height*cellsize*0.02))

    # start button
    start = pygame.image.load("images/start.png")
    start =  pygame.transform.scale(start ,(button_size, int(height*0.06*cellsize)))
    screen.blit(start, (space_size,int(height*cellsize*0.94)))

    # pause
    pause = pygame.image.load ("images/stop.png")
    pause =  pygame.transform.scale(pause ,(button_size, int(height*0.06*cellsize)))
    screen.blit(pause, (2*space_size + button_size,int(height*cellsize*0.94)))

    # quit
    quit = pygame.image.load ("images/quit.png")
    quit =  pygame.transform.scale(quit ,(button_size, int(height*0.06*cellsize)))
    screen.blit(quit, (3*space_size + 2*button_size,int(height*cellsize*0.94)))

    # clear
    clear = pygame.image.load ("images/clear.png")
    clear =  pygame.transform.scale(clear ,(button_size, int(height*0.06*cellsize)))
    screen.blit(clear, (4*space_size + 3*button_size,int(height*cellsize*0.94)))

    # quit
    grid = pygame.image.load ("images/grid.png")
    grid =  pygame.transform.scale(grid ,(button_size, int(height*0.06*cellsize)))
    screen.blit(grid, (5*space_size + 4*button_size,int(height*cellsize*0.94)))

def updateboard(currentMatrix, height, width):
    newMatrix = np.zeros((width + 100, height + 100))

    for x in range(-5, currentMatrix.shape[0]-1):
        for y in range(-5, currentMatrix.shape[1]-1):
            alive_neighbors = 0
            
            for i in range(-1, 2):
                for j in range(-1, 2):
                    alive_neighbors += currentMatrix[x+i][y+j]

            alive_neighbors =  alive_neighbors - currentMatrix[x][y]

            if (currentMatrix[x][y] == 1 and alive_neighbors < 2):
                newMatrix[x][y] = 0
            
            elif (currentMatrix[x][y] == 1 and 2 <= alive_neighbors <= 3):
                newMatrix[x][y] = 1

            elif (currentMatrix[x][y] == 1 and alive_neighbors > 3):
                newMatrix[x][y] = 0

            elif (currentMatrix[x][y] == 0 and alive_neighbors == 3):
                newMatrix[x][y] = 1 

    return newMatrix

def startgame():
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    
    # game specs
    cellsize = round(screen.get_width()*0.0075)
    height = round(screen.get_height() / cellsize) 
    width = round(screen.get_width() / cellsize)

    # grid specs
    game_height = round(height*0.80)
    y_offset = round(height * 0.12)

    #gamestate
    grid = True
    status = False
    generations = 0

    # button specs
    button_size = round(width * cellsize * 0.14)
    space_size = round(width * cellsize * 0.05)

    # button location
    b1 = space_size
    b2 = space_size*2 + button_size
    b3 = space_size*3 + button_size*2
    b4 = space_size*4 + button_size*3
    b5 = space_size*5 + button_size*4
    button_start = int(height*cellsize*0.94)
    button_end = int(height*cellsize)

    matrix = blankBoard(height, width)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            if (status == False): #game paused 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # game is paused
                    if (0 <=pygame.mouse.get_pos()[0] and y_offset*cellsize <= pygame.mouse.get_pos()[1]):
                        if (width * cellsize >=pygame.mouse.get_pos()[0] and height*cellsize >= pygame.mouse.get_pos()[1]):
                            generations = 0
                            x_coord = round(pygame.mouse.get_pos()[0]/cellsize)
                            y_coord = round(pygame.mouse.get_pos()[1]/cellsize) - y_offset
                            
                            if (matrix[x_coord, y_coord] == 1):
                                matrix[x_coord, y_coord] = 0
                            else:
                                matrix[x_coord, y_coord] = 1
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                # START BUTTON
                if (b1 <=pygame.mouse.get_pos()[0] and button_start <= pygame.mouse.get_pos()[1]):
                    if (b1+button_size >=pygame.mouse.get_pos()[0]and button_end >=pygame.mouse.get_pos()[1]):
                        status = True

                # STOP BUTTON
                if (b2 <=pygame.mouse.get_pos()[0] and button_start <= pygame.mouse.get_pos()[1]):
                    if (b2+button_size >=pygame.mouse.get_pos()[0]and button_end >=pygame.mouse.get_pos()[1]):
                        status = False
                
                # Quit BUTTON
                if (b3 <=pygame.mouse.get_pos()[0] and button_start <= pygame.mouse.get_pos()[1]):
                    if (b3+button_size >=pygame.mouse.get_pos()[0]and button_end >=pygame.mouse.get_pos()[1]):
                        pygame.quit()
                        return

                # CLear BUTTON
                if (b4 <=pygame.mouse.get_pos()[0] and button_start <= pygame.mouse.get_pos()[1]):
                    if (b4+button_size >=pygame.mouse.get_pos()[0]and button_end >=pygame.mouse.get_pos()[1]):
                        matrix = blankBoard(height, width)
                        generations = 0

                # Grid BUTTON
                if (b5 <=pygame.mouse.get_pos()[0] and button_start <= pygame.mouse.get_pos()[1]):
                    if (b5+button_size >=pygame.mouse.get_pos()[0]and button_end >=pygame.mouse.get_pos()[1]):
                        if (grid):
                            grid = False
                        else:
                            grid = True
                             
        if (status == True):
            generations += 1
            matrix = updateboard(matrix, height, width)

        screen.fill(black)
        drawBoard(screen, matrix, grid, width, game_height, y_offset, cellsize)
        drawUI(screen, height, width, button_size, space_size, cellsize, generations)
        pygame.display.update()

if __name__ == '__main__':
    startgame()