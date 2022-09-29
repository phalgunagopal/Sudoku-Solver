import sys
import pygame
import time
pygame.font.init()
font1 = pygame.font.SysFont("comicsans", 40)
font2 = pygame.font.SysFont("comicsans", 20)

grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]
def find_blanks(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==0 or board==" ":
                board[i][j]=0
                return i,j
    return False
def check_existence(board,n,pos):
    pygame.init()
    for i in range(len(board)):
        if n==board[pos[0]][i] and pos[1]!=i:
            return False
    for i in range(len(board)):
        if n==board[i][pos[1]] and pos[0]!=i:
            return False
    for i in range((pos[0]//3)*3,((pos[0]//3)*3)+3):
        for j in range((pos[1]//3)*3,((pos[1]//3)*3)+3):
            if n==board[i][j] and (i,j)!=pos:
                return False
    return True
def solve_sudoku(board):
    pygame.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 35)
    t0 = time.perf_counter()
    blanks=find_blanks(board)
    if not blanks:
        t1=time.perf_counter()
        print(t1-t0)
        pygame.draw.rect(screen, pygame.Color("white"), (20, 770, 750, 750 ))
        text1 = font1.render("SOLVED!!", 1, (0, 0, 0))
        screen.blit(text1, (20, 770))
        pygame.display.update()

        return True
    else:
        row,column=blanks
        for i in range(1,10):
            if check_existence(board,i,(row,column)):
                pygame.init()
                board[row][column]=i
                value = myfont.render(str( chr(i+96)), True, pygame.Color("black"))
                try:
                   screen.blit(value, (column * 80 + 15 + 30, (row * 80) + 25))
                   pygame.display.update()
                except:
                    print("")



                if solve_sudoku(board):
                    return True
                board[row][column]=0

                pygame.draw.rect(screen, pygame.Color("white"),(column * 80 + 20, row * 80 + 20, 80 - 30, 80 - 10))
                time.sleep(0.02)

        return False


pygame.init()

running=True
running2=True
size=800,800
pygame.display.set_caption( "WORDOKU Solver(A TO I)" )


screen=pygame.display.set_mode(size)
def draw_bg():
    screen.fill(pygame.Color("white"))
    pygame.draw.rect(screen,pygame.Color("black"),pygame.Rect(15,15,720,720),10)
    i=1
    while (i*80)<720:
        lwidth=5 if i%3!=0 else 10
        pygame.draw.line(screen,pygame.Color("black"),pygame.Vector2((i*80)+15,15),pygame.Vector2((i*80)+15,735),lwidth)
        pygame.draw.line(screen, pygame.Color("black"), pygame.Vector2(15,(i * 80) + 15),pygame.Vector2(735,(i * 80)+15),lwidth)
        i+=1
    pygame.display.flip()

def drawnum(screen,position):
    running2=True
    i=position[0]
    j=position[1]

    myfont = pygame.font.SysFont('Comic Sans MS', 35)
    while running2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                pygame.draw.rect(screen, pygame.Color("white"),
                                 (position[1] * 80 + 20, position[0] * 80 + 20, 80 - 30, 80 - 10))
                pygame.display.update()

                if not (0<event.key-96<10  ):  # checking with 0
                    grid[i ][j ] = 0

                    pygame.draw.rect(screen, pygame.Color("white"), ( position[1] * 80 +20, position[0] * 80+20, 80-30 , 80-10 ))
                    pygame.display.update()
                    return



                if (0 < event.key - 96< 10):  # We are checking for valid input
                    pygame.draw.rect(screen, pygame.Color("white"), (position[1] * 80+20, position[0] * 80+20, 80-30 , 80-10 ))
                    value = myfont.render(str(chr(event.key )), True, pygame.Color("black"))
                    screen.blit(value, (position[1] * 80+15+30, (position[0] * 80)+25))

                    pygame.display.update()
                    b=True
                    for k in range(len(grid)):
                        if event.key-96== grid[position[0]][k] and position[1] != k:
                            b=False
                    for k in range(len(grid)):
                        if event.key-96 == grid[k][position[1]] and position[0] != k:
                            b=False
                    for k in range((position[0] // 3) * 3, ((position[0] // 3) * 3) + 3):
                        for m in range((position[1] // 3) * 3, ((position[1] // 3) * 3) + 3):
                            if event.key-96 == grid[k][m] and (k, m) != position:
                               b=False
                    if  not b:
                        pygame.draw.rect(screen, pygame.Color("white"),(position[1] * 80 + 20, position[0] * 80 + 20, 80 - 30, 80 - 10))
                        grid[i][j]=0
                        pygame.display.update()
                        #break
                    pygame.display.update()
                    if b:
                        grid[i][j] = event.key-96


                    pygame.event.pump()
                    running2=False

draw_bg()
text1 = font1.render("PRESS ENTER TO  SOLVE",1,(0,0,0))

screen.blit(text1, (20, 770))

while running:
    for event in pygame.event.get():

        if event.type==pygame.MOUSEBUTTONUP and event.button==1:
            pos=list(pygame.mouse.get_pos())
            if pos[1] <740:
                pos[0]=(pos[0]-15)//80
                pos[1]=(pos[1]-15)//80
                temp=pos[0]
                pos[0]=pos[1]
                pos[1]=temp
                if pos[0]<=9 and pos[1]<9:

                    drawnum(screen,pos)
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RETURN:
                solve_sudoku(grid)


        if event.type == pygame.QUIT:
            running=False
            pygame.quit()
        #drawnum()
        #pygame.display.flip()



#solve_sudoku(grid)



