import pygame
import time
import random

# Khởi tạo Pygame
pygame.init()

# Thiết lập màu sắc
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Kích thước màn hình
width, height = 600, 400
dis = pygame.display.set_mode((width, height))
pygame.display.set_caption('Game Rắn Săn Mồi (by NguyenPhat)')

# Kích thước và tốc độ khối rắn
snake_block = 10
clock = pygame.time.Clock()

# Font chữ
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Hàm hiển thị điểm số
def Your_score(score):
    value = score_font.render("Điểm của bạn: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

# Vẽ con rắn
def our_snake(snake_block, snake_List):
    for segment in snake_List:
        pygame.draw.rect(dis, green, [segment[0], segment[1], snake_block, snake_block])

# Hiển thị thông báo kết thúc game
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [width / 6, height / 3])

# Hàm chọn cấp độ
def choose_level():
    level = None
    while level is None:
        dis.fill(blue)
        message("Nhấn 1 - Dễ, 2 - Vừa, 3 - Khó", yellow)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    level = 10  # Dễ
                elif event.key == pygame.K_2:
                    level = 15  # Vừa
                elif event.key == pygame.K_3:
                    level = 20  # Khó

    return level

# Hàm chính của game
def gameLoop(snake_speed):
    game_over = False
    game_close = False

    # Vị trí ban đầu của rắn
    x1 = width / 2
    y1 = height / 2

    # Hướng di chuyển ban đầu
    x1_change = 0
    y1_change = 0

    # Danh sách chứa thân rắn
    snake_List = []
    Length_of_snake = 1

    # Vị trí của thức ăn
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    # Vòng lặp trò chơi
    while not game_over:

        # Xử lý khi game kết thúc
        while game_close:
            dis.fill(blue)
            message("Bạn thua! Nhấn C để chơi lại, Q để thoát", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop(snake_speed)

        # Xử lý sự kiện di chuyển của rắn
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0

        # Kiểm tra va chạm với tường
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        # Cập nhật vị trí rắn
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)

        # Vẽ thức ăn
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])

        # Cập nhật thân rắn
        snake_Head = [x1, y1]
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Kiểm tra va chạm với thân rắn
        for segment in snake_List[:-1]:
            if segment == snake_Head:
                game_close = True

        # Vẽ rắn và điểm số
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        # Kiểm tra va chạm với thức ăn
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        # Điều chỉnh tốc độ game
        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Chạy game
snake_speed = choose_level()
gameLoop(snake_speed)
