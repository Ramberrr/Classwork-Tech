# pygame template

import pygame


pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables
Day_Night_Call = 7500
Next_call = 7500
Day = False
Sky_RGB = 100
Sun_y = 50
Moon_y = 400
Smoke_timer = 100
cloud_x = 563
cloud_moveby = 4
# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
    # GAME STATE UPDATES
    #Day night Cycle
    current_time = pygame.time.get_ticks()
    if current_time >= Next_call:
        Next_call += Day_Night_Call
        print('Time Cycle')
        if Day:
            Day = False
        else:
            Day = True

    if Day:
        if Sun_y < 400:
            Sun_y += 5
            Sky_RGB -= 0.5
        if Sun_y == 400 and Moon_y > 50:
            Moon_y -= 5
            Sky_RGB -= 1
    else:
        if Moon_y < 400:
            Moon_y += 5
            Sky_RGB += 0.5
        if Moon_y == 400 and Sun_y > 50:
            Sun_y -= 5
            Sky_RGB += 1
    
    # Smoke Timer
    Smoke_timer -= 1
    if Smoke_timer == 0:
        Smoke_timer = 100

    # Cloud Animation
    if cloud_x > 670:
        cloud_moveby = -4
    elif cloud_x < -78:
        cloud_moveby = 4
    cloud_x += cloud_moveby

    # DRAW
    # Sky
    screen.fill((Sky_RGB+35, Sky_RGB+106, Sky_RGB+135))  # always the first drawing command

    # Sun & Moon
    pygame.draw.circle(screen, (249,215,29), (100, Sun_y), 30)
    pygame.draw.circle(screen, (197,194,207), (100, Moon_y), 30)

    # Background
    pygame.draw.polygon(screen,(128,128,128),((320,200),(0,480),(640,480)))
    pygame.draw.polygon(screen,(105,105,105),((480,250),(0,480),(640,480)))
    pygame.draw.polygon(screen,(105,105,105),((160,275),(0,480),(640,480)))
    pygame.draw.polygon(screen,(65,152,10),((0,400),(0,480),(640,480),(640,400)))

    # House
    pygame.draw.rect(screen, (255,0,0), (400,250,30,40))
    pygame.draw.polygon(screen, (226, 224, 110),((300,400),(300,300),(460,300),(460,400)))
    pygame.draw.polygon(screen, (255,39,13),((270,300),(270,300),(490,300),(380,250)))
    pygame.draw.polygon(screen, (92, 64, 51),((400,400),(425,400),(425,350),(400,350)))
    pygame.draw.polygon(screen,(166, 189, 214), ((380,370),(320,370),(320,325),(380,325)))

    # Smoke
    if Smoke_timer <= 100 and Smoke_timer >= 50:
        pygame.draw.circle(screen, (132, 147, 156), (419, 233), 15)
    if Smoke_timer <= 75 and Smoke_timer >= 25:
        pygame.draw.circle(screen, (132, 147, 156), (429, 211), 15)
    if Smoke_timer <= 50 and Smoke_timer >= 0:
        pygame.draw.circle(screen, (132, 147, 156), (411, 209), 15)
    if Smoke_timer <= 25 and Smoke_timer >= 0:
        pygame.draw.circle(screen, (132, 147, 156), (427, 195), 15)

    # Clouds
    pygame.draw.circle(screen, (255,255,255), (cloud_x + 48,37), 30)
    pygame.draw.circle(screen, (255,255,255), (cloud_x + 22, 35), 30)
    pygame.draw.circle(screen, (255,255,255), (cloud_x, 37), 30)

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()
