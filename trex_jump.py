import pygame
import random

# Khởi tạo Pygame
pygame.init()

# Kích thước cửa sổ
WIDTH, HEIGHT = 800, 400
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("T-Rex Jump Game(by Nguyễn Phát)")

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Tốc độ và FPS
FPS = 60
SPEED = 5

# Khởi tạo font chữ
font = pygame.font.Font(None, 36)

# Hình chữ nhật đại diện cho T-Rex
trex = pygame.Rect(50, 300, 50, 50)

# Danh sách chướng ngại vật
obstacles = []
obstacle_timer = 0

# Các biến liên quan đến nhảy
base_jump_speed = 15  # Vận tốc nhảy ban đầu
jump_factor = 1.2     # Tăng 20%
jump_speed = base_jump_speed * jump_factor  # Vận tốc sau khi tăng
gravity = 1
trex_velocity = 0
is_jumping = False

# Hàm sinh chướng ngại vật
def spawn_obstacle():
    obstacle = pygame.Rect(WIDTH, 300, 50, 50)
    obstacles.append(obstacle)

# Hàm vẽ mọi thứ lên màn hình
def draw_window():
    window.fill(WHITE)

    # Vẽ T-Rex
    pygame.draw.rect(window, BLACK, trex)

    # Vẽ các chướng ngại vật
    for obstacle in obstacles:
        pygame.draw.rect(window, BLACK, obstacle)

    # Cập nhật màn hình
    pygame.display.update()

# Vòng lặp chính của game
def main():
    global is_jumping, trex_velocity, obstacle_timer

    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

        # Xử lý sự kiện
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if not is_jumping:  # Chỉ cho phép nhảy khi đang đứng yên
                    is_jumping = True
                    trex_velocity = -jump_speed

        # Cập nhật vị trí của T-Rex
        if is_jumping:
            trex.y += trex_velocity
            trex_velocity += gravity

            # Khi T-Rex chạm đất, dừng nhảy
            if trex.y >= 300:
                trex.y = 300
                is_jumping = False

        # Sinh chướng ngại vật ngẫu nhiên
        if obstacle_timer > 90:  # Mỗi 1.5 giây tạo chướng ngại vật
            spawn_obstacle()
            obstacle_timer = 0

        # Di chuyển và loại bỏ chướng ngại vật ra khỏi màn hình
        for obstacle in obstacles[:]:
            obstacle.x -= SPEED
            if obstacle.x < -50:
                obstacles.remove(obstacle)

        # Kiểm tra va chạm
        for obstacle in obstacles:
            if trex.colliderect(obstacle):
                print("Game Over!")
                run = False

        # Vẽ mọi thứ lên màn hình
        draw_window()

        # Tăng thời gian đếm chướng ngại vật
        obstacle_timer += 1

    pygame.quit()

if __name__ == "__main__":
    main()
