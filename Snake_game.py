import pygame


import time
import random as rand


pygame.init()
dis_weight = 600
dis_height = 400

dis = pygame.display.set_mode((dis_weight, dis_height))
pygame.display.set_caption('Snake game')

white = (255, 255, 255)
yellow = (255, 255, 102)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)


snake_size = 10
snake_speed = 5
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont('comicsansms', 35)
clock = pygame.time.Clock()


# Рисуем хвост
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


# Вывод сообщения на экран
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_weight / 4 - 80, dis_height / 3])


# Функция игры
def gameLoop():
    game_over = False
    game_close = False
    x1, y1 = dis_weight / 2, dis_height / 2
    x1_change = 0
    y1_change = 0

    snake_list = []
    lenght_of_snake = 1

    # Позиция для рандома
    foodx = round(rand.randint(snake_size, dis_weight - snake_size - 10) / 10) * 10
    foody = round(rand.randint(snake_size, dis_height - snake_size - 10) / 10) * 10
    # Идет игра
    while not game_over:
        # Если игра проиграна, то мы узнаем у пользователя что делать дальше
        while game_close:
            dis.fill(white)
            message('You lost! Press Q-Quit or C-Play Again', red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        quit()
                    if event.key == pygame.K_c:
                        gameLoop()

    # Здесь обрабатываем эвенты
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            # Если клавиша нажата, то смотрим какая и в какую сторону двигаться
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change != snake_size:
                    x1_change = -snake_size
                    y1_change = 0
                if event.key == pygame.K_RIGHT and x1_change != -snake_size:
                    x1_change = snake_size
                    y1_change = 0
                if event.key == pygame.K_UP and y1_change != snake_size:
                    x1_change = 0
                    y1_change = -snake_size
                if event.key == pygame.K_DOWN and y1_change != -snake_size:
                    x1_change = 0
                    y1_change = snake_size
    # Смотрим, чтобы змея не вылезла за край карты, иначе игрок проиграл
        if x1 >= dis_weight or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(white)
    # Отрисовка еды
        pygame.draw.rect(dis, red, [foodx, foody, snake_size, snake_size])
        snake_head = list()
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > lenght_of_snake:
            del snake_list[0]
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True
        our_snake(snake_size, snake_list)
        pygame.display.update()
        # Отрисовка новой еды, если её съели
        if x1 == foodx and y1 == foody:
            foodx = round(rand.randint(snake_size, dis_weight - snake_size) / 10) * 10
            foody = round(rand.randint(snake_size, dis_height - snake_size) / 10) * 10
            lenght_of_snake += 1
            print('Yummy!')
        pygame.display.update()

        clock.tick(snake_speed)

    time.sleep(2)

    pygame.quit()
    quit()


gameLoop()
