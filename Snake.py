import pygame
from os import path
import time
import random
pygame.init()

WIDTH=800
HEIGHT= 800

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
#создаем дисплей
screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption('Змейка на PyGame')
#путь к сторонним файлам 
img_dir = path.join(path.dirname(__file__), 'img')
music_dir = path.join(path.dirname(__file__), 'music')
#загрузка фона
bg = pygame.image.load(path.join(img_dir,'Fon_grass4_1.jpg')).convert()
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
bg_rect = bg.get_rect()
#загрузка музыки
pygame.mixer.music.load(path.join(music_dir, 'Intense.mp3'))
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)
am = pygame.mixer.Sound(path.join(music_dir,'apple_bite.ogg'))
am.set_volume(0.5)
#задаем скорость
snake_speed = 15
#внутриигровое время
clock = pygame.time.Clock()

#шрифты для надписей
font_style = pygame.font.SysFont(None, 32)
score_font = pygame.font.SysFont("comicsansms", 25)
#функция для вывода финальной записи
def message(msg, color):
    mes = font_style.render(msg, True, color)
    screen.blit(mes, [WIDTH/16, HEIGHT/2])
#функция подсчета очков
def score_for_snake(score):
    value = score_font.render("Ваш счет: " + str(score), True, RED)
    screen.blit(value, [0, 0])
#создание блоков для змеи
def new_block(snake_body):
    for x in snake_body:
        pygame.draw.rect(screen,BLACK, [x[0], x[1], 10, 10])
#игровая функция, в ней находиться игровой цикл
def game():
    #создание еды
    foodx = round(random.randrange(0, WIDTH - 10) / 10) * 10
    foody = round(random.randrange(0, HEIGHT - 10) / 10) * 10
    #загрузка и размещение картинки еды
    food_img =  [pygame.image.load(path.join(img_dir, 'f_1.png')).convert(), pygame.image.load(path.join(img_dir, 'f_2.png')).convert(),pygame.image.load(path.join(img_dir, 'f_3.png')).convert(),pygame.image.load(path.join(img_dir, 'f_4.png')).convert(),pygame.image.load(path.join(img_dir, 'f_5.png')).convert() ]
    food = pygame.transform.scale(random.choice(food_img), (10,10))
    food.set_colorkey(WHITE)
    food_rect = food.get_rect(x = foodx, y = foody)
    #координаты для змеи
    xcor = WIDTH/2
    ycor = HEIGHT/2
    x = 0
    y = 0
    #список элементов змеи
    snake_body = []
    #длина змеи
    length = 1
    #переменные для циклов
    run = True
    end = False
    #основной игровой цикл
    while run:
        #цикл для перезагрузки игры или выхода из игры
        while end == True:
            screen.fill(BLUE)
            message("Ты проиграл! Нажми 'C' для продолжения  или 'Q'-для выхода", RED)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:                    
                    if event.key == pygame.K_q:
                        run = False
                        end = False
                    if event.key == pygame.K_c:
                        game()
        #обработка событий (закрытие окна, нажатие на клавиши)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x = -10
                        y = 0
                    elif event.key == pygame.K_RIGHT:
                        x = 10
                        y = 0
                    elif event.key == pygame.K_UP:
                        y = -10
                        x = 0
                    elif event.key == pygame.K_DOWN:
                        y = 10
                        x = 0
        #проверка на касание границ
        if xcor >= WIDTH or xcor < 0 or ycor >= HEIGHT or ycor < 0:
            end = True
        #изменение координат змеи
        xcor += x
        ycor += y
        #заливка экрана и отображение всех элементов на дисплее
        screen.fill(BLUE)
        screen.blit(bg, bg_rect)
        screen.blit(food, food_rect)
        #pygame.draw.rect(screen, BLUE, (xcor, ycor, 10,10))
        #pygame.draw.rect(screen, GREEN, (foodx, foody, 10,10))

        #заполнение списка змеи
        snake_head = []
        snake_head.append(xcor)
        snake_head.append(ycor)
        snake_body.append(snake_head)
        if len(snake_body) > length:
            del snake_body[0]
            
        for z in snake_body [:-1]:
            if z == snake_head:
                end = True
        new_block(snake_body)
        score_for_snake(length -1)
        pygame.display.update()
        #съедание еды 
        if xcor == foodx and ycor == foody:
            foodx = round(random.randrange(0, WIDTH - 30) / 10) * 10
            foody = round(random.randrange(0, HEIGHT - 30) / 10) * 10
            food_img =  [pygame.image.load(path.join(img_dir, 'f_1.png')).convert(), pygame.image.load(path.join(img_dir, 'f_2.png')).convert(),pygame.image.load(path.join(img_dir, 'f_3.png')).convert(),pygame.image.load(path.join(img_dir, 'f_4.png')).convert(),pygame.image.load(path.join(img_dir, 'f_5.png')).convert() ]
            food = pygame.transform.scale(random.choice(food_img), (10,10))
            food.set_colorkey(WHITE)    
            food_rect = food.get_rect(x = foodx, y = foody)
            #меняем длину змеи (заодно и счет на дисплее измениться)
            length += 1
            #звуковой эффект
            am.play()
        #переворот дисплея
        pygame.display.flip()
        #скорость отображения кадров (зависит от скорости змеи)
        clock.tick(snake_speed)

    #message('Ты проиграл!', RED)
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    quit()
#перезапуск игровой функции
game()
