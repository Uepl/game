import pygame,random,time
pygame.init()

width,height = 400,400
game_screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake Game")
x,y =200,200
delta_x, delta_y = 10,0
apple_x,apple_y = random.randrange(0,width)//10*10, random.randrange(0,height)//10*10
body_list =[(x,y)]
clock =pygame.time.Clock()
game_over = False
font = pygame.font.SysFont("Segoe UI",25)
def snake():
    global x,y,apple_x,apple_y,game_over
    x = (x+ delta_x)%width
    y = (y+ delta_y)%height
    if((x,y) in body_list):
        game_over =True
        return
    body_list.append((x,y))
    if(apple_x ==x and apple_y ==y):
        while((apple_x,apple_y) in body_list):
            apple_x,apple_y = random.randrange(0,width)//10*10, random.randrange(0,height)//10*10
    else:
        del body_list[0]
    game_screen.fill((0,0,0))
    score = font.render("Score: " + str(len(body_list)-1),True,(0,0,255))
    game_screen.blit(score,[150,0])
    pygame.draw.rect(game_screen,(255,0,0),[apple_x,apple_y,10,10])
    for(i,j) in body_list:
        pygame.draw.rect(game_screen, (255,255,255), [i,j,10,10])
    pygame.display.update()
while True:
    
    if(game_over):
        game_screen.fill((0,0,0))
        score = font.render("Score: " + str(len(body_list)), True,(0,0,255))
        game_screen.blit(score,[0,0])
        msg = font.render("Game Over",True,(255,255,255))
        game_screen.blit(msg, [width//3,height//3])
        pygame.display.update()
        time.sleep(3)
        pygame.quit()
        quit()
    events = pygame.event.get()
    for event in events:
        if(event.type ==pygame.QUIT):
            pygame.quit()
            quit()
        if(event.type ==pygame.KEYDOWN):
            if(event.key ==pygame.K_DOWN):
                if(delta_y != -10):
                    delta_y =10
                delta_x =0
            elif(event.key ==pygame.K_UP):
                if(delta_y != 10):
                    delta_y =-10
                delta_x =0 
            elif(event.key ==pygame.K_LEFT):
                if(delta_x != 10):
                    delta_x =-10
                delta_y =0
            elif(event.key ==pygame.K_RIGHT):
                if(delta_x != -10):
                    delta_x =10
                delta_y =0
            else:
                continue
            snake()
    if(not events):
        snake()        
    clock.tick(10)