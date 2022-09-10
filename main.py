from pygame import *
import time as t





clicked = 0
text = []
result = 0
resulted = False
g = 50



init()

icon = image.load("icon.png")
win = display.set_mode((300,450))
display.set_caption("Matrix Calculator")
display.set_icon(icon)


mainFont = font.SysFont("Sans", 40, 1,0)
mainFont2 = font.SysFont("Sans", 50, 1,0)

delete = image.load("del.png")



while True:
    m = mouse.get_pos()


    win.fill((255,255,255))
    for i in event.get():
        if i.type == QUIT:
            exit()
        if i.type == MOUSEBUTTONDOWN:
            if BUTTON_LEFT:
                clicked = 1
        if i.type == MOUSEBUTTONUP:
            clicked = 0

    draw.rect(win, (250, 250, 250), (3,   373 - 76 - 76 * 2, 72, 74))
    draw.rect(win, (250, 250, 250), (77,  373 - 76 - 76 * 2, 72, 74))
    draw.rect(win, (250, 250, 250), (151, 373 - 76 - 76 * 2, 72, 74))
    draw.rect(win, (250, 250, 250), (225, 373 - 76 - 76 * 2, 35, 74))
    draw.rect(win, (250, 250, 250), (225+37, 373 - 76 - 76 * 2, 35, 74))

    draw.rect(win, (250, 250, 250), (3,   373 - 76 - 76, 72, 74))
    draw.rect(win, (250, 250, 250), (77,  373 - 76 - 76, 72, 74))
    draw.rect(win, (250, 250, 250), (225, 373 - 76 - 76, 35, 74))
    draw.rect(win, (250, 250, 250), (225 + 37, 373 - 76 - 76, 35, 74))

    draw.rect(win, (250, 250, 250), (3,   373 - 76, 72, 74))
    draw.rect(win, (250, 250, 250), (77,  373 - 76, 72, 74))
    draw.rect(win, (250, 250, 250), (151, 373 - 76, 72, 74))
    draw.rect(win, (250, 250, 250), (225, 373 - 76, 72, 74))

    draw.rect(win, (250, 250, 250), (3,   373, 72, 74))
    draw.rect(win, (250, 250, 250), (77,  373, 72, 74))
    draw.rect(win, (250, 250, 250), (151, 373, 72, 74))
    draw.rect(win, (250, 250, 250), (225, 373, 72, 74))



    draw.rect(win, (230, 230, 230), (3, 373 - 76 - 76 * 2, 72, 74), 3)
    draw.rect(win, (230, 230, 230), (77, 373 - 76 - 76 * 2, 72, 74),  3)
    draw.rect(win, (230, 230, 230), (151, 373 - 76 - 76 * 2, 72, 74), 3)
    draw.rect(win, (230, 230, 230), (225, 373 - 76 - 76 * 2, 35, 74), 3)
    draw.rect(win, (230, 230, 230), (225 + 37, 373 - 76 - 76 * 2, 35, 74), 3)

    draw.rect(win, (230, 230, 230), (3, 373 - 76 - 76, 72, 74),   3)
    draw.rect(win, (230, 230, 230), (77, 373 - 76 - 76, 72, 74),  3)
    draw.rect(win, (230, 230, 230), (151, 373 - 76 - 76, 72, 74), 3)
    draw.rect(win, (230, 230, 230), (225, 373 - 76 - 76, 35, 74), 3)
    draw.rect(win, (230, 230, 230), (225 + 37, 373 - 76 - 76 , 35, 74), 3)

    draw.rect(win, (230, 230, 230), (3, 373 - 76, 72, 74),   3)
    draw.rect(win, (230, 230, 230), (77, 373 - 76, 72, 74),  3)
    draw.rect(win, (230, 230, 230), (151, 373 - 76, 72, 74), 3)
    draw.rect(win, (230, 230, 230), (225, 373 - 76, 72, 74), 3)

    draw.rect(win, (230, 230, 230), (3, 373, 72, 74),   3)
    draw.rect(win, (230, 230, 230), (77, 373, 72, 74),  3)
    draw.rect(win, (230, 230, 230), (151, 373, 72, 74), 3)
    draw.rect(win, (230, 230, 230), (225, 373, 72, 74), 3)



    if m[0] >=3 and m[0]<= 3+72 and m[1] >=373 - 76 - 76 * 2 and m[1] <= 373 - 76 - 76 * 2 + 74:
        draw.rect(win, (190, 190, 190), (3,   373 - 76 - 76 * 2, 72, 74), 3)
        if clicked:
            text.append('1')
            clicked = 0
    if m[0] >= 77 and m[0] <= 77 + 72 and m[1] >= 373 - 76 - 76 * 2 and m[1] <= 373 - 76 - 76 * 2 + 74:
        draw.rect(win, (190, 190, 190), (77,  373 - 76 - 76 * 2, 72, 74), 3)
        if clicked:
            text.append('2')
            clicked = 0
    if m[0] >= 151 and m[0] <= 151 + 72 and m[1] >= 373 - 76 - 76 * 2 and m[1] <= 373 - 76 - 76 * 2 + 74:
        draw.rect(win, (190, 190, 190), (151, 373 - 76 - 76 * 2, 72, 74), 3)
        if clicked:
            text.append('3')
            clicked = 0
    if m[0] >= 225 and m[0] <= 225 + 35 and m[1] >= 373 - 76 - 76 * 2 and m[1] <= 373 - 76 - 76 * 2 + 74:
        draw.rect(win, (190, 190, 190), (225, 373 - 76 - 76 * 2, 35, 74), 3)
        if clicked:
            text.append('(')
            clicked = 0
    if m[0] >= 225+37 and m[0] <= 225+37  + 35 and m[1] >= 373 - 76 - 76 * 2 and m[1] <= 373 - 76 - 76 * 2 + 74:
        draw.rect(win, (190, 190, 190), (225+37, 373 - 76 - 76 * 2, 35, 74), 3)
        if clicked:
            text.append(')')
            clicked = 0

    if m[0] >= 3 and m[0] <= 3+72 and m[1] >= 373 - 76 - 76 and m[1] <= 373 - 76 - 76 + 74:
        draw.rect(win, (190, 190, 190), (3,   373 - 76 - 76, 72, 74), 3)
        if clicked:
            text.append('4')
            clicked = 0
    if m[0] >= 77 and m[0] <= 77 + 72 and m[1] >= 373 - 76 - 76 and m[1] <= 373 - 76 - 76 + 74:
        draw.rect(win, (190, 190, 190), (77,  373 - 76 - 76, 72, 74), 3)
        if clicked:
            text.append('5')
            clicked = 0
    if m[0] >= 151 and m[0] <= 151 + 72 and m[1] >= 373 - 76 - 76 and m[1] <= 373 - 76 - 76 + 74:
        draw.rect(win, (190, 190, 190), (151, 373 - 76 - 76, 72, 74), 3)
        if clicked:
            text.append('6')
            clicked = 0
    if m[0] >= 225 and m[0] <= 225 + 35 and m[1] >= 373 - 76 - 76 and m[1] <= 373 - 76 - 76 + 74:
        draw.rect(win, (190, 190, 190), (225, 373 - 76 - 76, 35, 74), 3)
        if clicked:
            text.append('+')
            clicked = 0
    if m[0] >= 225 + 37 and m[0] <= 225 + 37 + 35 and m[1] >= 373 - 76 - 76 and m[1] <= 373 - 76 - 76 + 74:
        draw.rect(win, (190, 190, 190), (225 + 37, 373 - 76 - 76, 35, 74), 3)
        if clicked:
            text.append('-')
            clicked = 0

    if m[0] >= 3 and m[0] <= 3 + 72 and m[1] >= 373 - 76 and m[1] <= 373 - 76 + 74:
        draw.rect(win, (190, 190, 190), (3,   373 - 76, 72, 74), 3)
        if clicked:
            text.append('7')
            clicked = 0
    if m[0] >= 77 and m[0] <=77 + 72 and m[1] >= 373 - 76 and m[1] <= 373 - 76 + 74:
        draw.rect(win, (190, 190, 190), (77,  373 - 76, 72, 74), 3)
        if clicked:
            text.append('8')
            clicked = 0
    if m[0] >= 151 and m[0] <= 151 + 72 and m[1] >= 373 - 76 and m[1] <= 373 - 76 + 74:
        draw.rect(win, (190, 190, 190), (151, 373 - 76, 72, 74), 3)
        if clicked:
            text.append('9')
            clicked = 0
    if m[0] >= 225 and m[0] <= 225 + 72 and m[1] >= 373 - 76 and m[1] <= 373 - 76 + 74:
        draw.rect(win, (190, 190, 190), (225, 373 - 76, 72, 74), 3)
        if clicked:
            text.append('*')
            clicked = 0

    if m[0] >= 3 and m[0] <= 3 + 72 and m[1] >= 373 and m[1] <= 373 + 74:
        draw.rect(win, (190, 190, 190), (3,   373, 72, 74), 3)
        if clicked:
            text.append('0')
            clicked = 0
    if m[0] >= 77 and m[0] <= 77 + 72 and m[1] >= 373 and m[1] <= 373 + 74:
        draw.rect(win, (190, 190, 190), (77,  373, 72, 74), 3)
        if clicked:
            text.append('.')
            clicked = 0
    if m[0] >= 151 and m[0] <= 151 + 72 and m[1] >= 373 and m[1] <= 373 + 74:
        draw.rect(win, (190, 190, 190), (151, 373, 72, 74), 3)
        if clicked:
            text.append('/')
            clicked = 0
    if m[0] >= 225 and m[0] <= 225 + 72 and m[1] >= 373 and m[1] <= 373 + 74:
        draw.rect(win, (190, 190, 190), (225, 373, 72, 74), 3)
        if clicked:
            try:
                result = eval(''.join(text))
                resulted = True
                print(result)
                clicked = 0
            except ZeroDivisionError:
                clicked = 0
                print("Нельзя делить на 0!")


    win.blit(mainFont.render("1", True, (140, 140, 140)), (27, 157))
    win.blit(mainFont.render("2", True, (140, 140, 140)), (27+74, 157))
    win.blit(mainFont.render("3", True, (140, 140, 140)), (27+74*2, 157))

    win.blit(mainFont.render("(", True, (140, 140, 140)), (27 + 74 * 3-13, 157))
    win.blit(mainFont.render(")", True, (140, 140, 140)), (27 + 74 * 3 + 25, 157))

    win.blit(mainFont.render("+", True, (140, 140, 140)), (27 + 74 * 3 - 18, 157+76))
    win.blit(mainFont.render("-", True, (140, 140, 140)), (27 + 74 * 3 + 23, 157+74))

    win.blit(mainFont.render("4", True, (140, 140, 140)), (27, 157+75))
    win.blit(mainFont.render("5", True, (140, 140, 140)), (27 + 74, 157+75*1))
    win.blit(mainFont.render("6", True, (140, 140, 140)), (27 + 74 * 2, 157+75*1))
    win.blit(mainFont.render("7", True, (140, 140, 140)), (27, 157+76*2))
    win.blit(mainFont.render("8", True, (140, 140, 140)), (27 + 74, 157+76*2))
    win.blit(mainFont.render("9", True, (140, 140, 140)), (27 + 74 * 2, 157+76*2))

    win.blit(mainFont.render("*", True, (140, 140, 140)), (27 + 75.5 * 3, 157 + 80 * 2))

    win.blit(mainFont.render("0", True, (140, 140, 140)), (27, 157 + 74+78*2))

    win.blit(mainFont.render(".", True, (140, 140, 140)), (27+79, 157 + 74 + 80 * 2))

    win.blit(mainFont.render("/", True, (140, 140, 140)), (27 + 77*2, 157 + 74 + 80 * 2))
    win.blit(mainFont.render("=", True, (140, 140, 140)), (27 + 74 * 3, 157 + 74 + 78 * 2))

    if m[0]>=230 and m[0]<=300 and m[1] >= 79 and m[1] <= 149:
        if clicked and len(text)>0:
            text.pop()
            clicked = 0
            if g < 50:
                g += 1

    mainFont2 = font.SysFont("Sans", int(g), 1, 0)
    if resulted == True:
        text.clear()
        result = str(result)
        for inn in range(len(result)):
            text.append(result[inn])
        resulted = False
        a = mainFont2.render(str(text[0]), True, (140, 140, 140))
    else:
        a = mainFont2.render(''.join(text), True, (140, 140, 140))
    b = a.get_rect().w
    delete = transform.smoothscale(delete, (70,70))
    win.blit(delete, (230, 79))
    win.blit(a, (-b+300, 40))
    if b >= 300:
        g -= 1
    display.flip()
    print(b)
