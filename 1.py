import pygame
import sys

x = 1
y = 1

a = 1

stena = pygame.image.load("idle_l/барьер.png")
stena = pygame.transform.scale(stena, (50, 50))

padlock = pygame.image.load("idle_l/замок.png")
padlock = pygame.transform.scale(padlock, (50, 60))

key = pygame.image.load("idle_l/key.png")
key = pygame.transform.scale(key, (100, 100))

portal1 = pygame.image.load("idle_l/портал1.png")
portal1 = pygame.transform.scale(portal1, (60, 75))
portal2 = pygame.image.load("idle_l/портал2.png")
portal2 = pygame.transform.scale(portal2, (50, 75))

wall = pygame.image.load("idle_l/стена.png")
wall = pygame.transform.scale(wall, (600, 400))

player = pygame.image.load("idle_l/куб2.png")
player = pygame.transform.scale(player, (50, 50))
surface = pygame.Surface((600, 400))
sc = pygame.display.set_mode((600, 400))

pygame.font.init()
f1 = pygame.font.Font(None, 30)

keyBlock = False

w_press = False
s_press = False
a_press = False
d_press = False

game = True
while True:

    for i in pygame.event.get():

        # управление
            if i.type == pygame.KEYDOWN:

                if i.key == pygame.K_w:
                    w_press = True
                if i.key == pygame.K_s:
                    s_press = True
                if i.key == pygame.K_a:
                    a_press = True
                if i.key == pygame.K_d:
                    d_press = True

            if i.type == pygame.KEYUP:

                if i.key == pygame.K_w:
                    w_press = False
                if i.key == pygame.K_s:
                    s_press = False
                if i.key == pygame.K_a:
                    a_press = False
                if i.key == pygame.K_d:
                    d_press = False

            if w_press and y > 5:
                y -= 10

            if s_press and y < 345:
                y += 10

            if a_press and x > 5:
                x -= 10

            if d_press and x < 545:
                x += 10

    if i.type == pygame.QUIT:
        game = False
        sys.exit()

    sc.blit(surface, (0, 0))

    sc.blit(wall, (0, 0))
    sc.blit(player, (x, y))

    # стены
    sc.blit(stena, (75, 75))
    sc.blit(stena, (75, 125))
    sc.blit(stena, (75, 175))
    sc.blit(stena, (75, 225))
    sc.blit(stena, (75, 275))
    sc.blit(stena, (25, 275))

    sc.blit(stena, (125, 75))
    sc.blit(stena, (175, 75))
    sc.blit(stena, (225, 75))
    sc.blit(stena, (275, 75))
    sc.blit(stena, (325, 75))
    sc.blit(stena, (375, 75))
    sc.blit(stena, (425, 75))
    sc.blit(stena, (475, 75))
    sc.blit(stena, (525, 75))

    # порталы
    sc.blit(portal1, (500, 0))
    sc.blit(portal2, (0, 325))

    # замок
    sc.blit(padlock, (0, 200))

    # коллизии

    # игрок
    Coll1 = pygame.Rect((x, y,), (50, 50))

    # порталы
    Coll2 = pygame.Rect((500, 0), (50, 75))
    Coll3 = pygame.Rect((0, 325), (50, 75))

    # стены
    Coll4 = pygame.Rect((75, 75), (50, 200))
    Coll5 = pygame.Rect((0, 275), (125, 50))
    Coll6 = pygame.Rect((75, 75), (500, 50))

    if not keyBlock:
        sc.blit(key, (500, 200))
        Coll7 = pygame.Rect((525, 225), (50, 50))
        check6 = Coll1.colliderect(Coll7)
        if check6 == 1:
            keyBlock = True

    Coll8 = pygame.Rect((0, 200), (50, 60))

    # столкновение коллизий
    check = Coll1.colliderect(Coll2)
    check2 = Coll1.colliderect(Coll3)
    check3 = Coll1.colliderect(Coll4)
    check4 = Coll1.colliderect(Coll5)
    check5 = Coll1.colliderect(Coll6)
    check7 = Coll1.colliderect(Coll8)

    if check:
        x = 50
        y = 350
    if check2:
        x = 450
        y = 25

    if check3 or check4 or check5:
        print("\n\n\n\n\n\n\nYou lose!\n\n\n\n\n\n\n")
        sys.exit()

    if not keyBlock:
        if check7:
            print("\n\n\n\n\n\n\nYou need key!\n\n\n\n\n\n\n")

    if keyBlock:
        if check7:
            print("\n\n\n\n\n\n\nYou win!\n\n\n\n\n\n\n")
            sys.exit()

    pygame.display.update()
    pygame.time.delay(1)

    # поле для игры