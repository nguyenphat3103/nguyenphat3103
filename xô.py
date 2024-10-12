import pygame
import sys

# Khởi tạo Pygame
pygame.init()

# Các thiết lập màn hình
width, height = 300, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Xo (Tic Tac Toe)")

# Các màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LINE_COLOR = (23, 145, 135)

# Kích thước ô
cell_size = 100

# Lưới trò chơi
grid = [["" for _ in range(3)] for _ in range(3)]
current_player = "X"

def draw_grid():
    for i in range(1, 3):
        pygame.draw.line(screen, LINE_COLOR, (0, i * cell_size), (width, i * cell_size), 2)
        pygame.draw.line(screen, LINE_COLOR, (i * cell_size, 0), (i * cell_size, height), 2)

def draw_marks():
    for i in range(3):
        for j in range(3):
            if grid[i][j] == "X":
                pygame.draw.line(screen, BLACK, (j * cell_size + 20, i * cell_size + 20), 
                                 (j * cell_size + cell_size - 20, i * cell_size + cell_size - 20), 2)
                pygame.draw.line(screen, BLACK, (j * cell_size + cell_size - 20, i * cell_size + 20), 
                                 (j * cell_size + 20, i * cell_size + cell_size - 20), 2)
            elif grid[i][j] == "O":
                pygame.draw.circle(screen, BLACK, (j * cell_size + cell_size // 2, 
                                                     i * cell_size + cell_size // 2), cell_size // 2 - 20, 2)

def check_winner():
    for row in grid:
        if row[0] == row[1] == row[2] and row[0] != "":
            return row[0]
    
    for col in range(3):
        if grid[0][col] == grid[1][col] == grid[2][col] and grid[0][col] != "":
            return grid[0][col]
    
    if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != "":
        return grid[0][0]
    
    if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != "":
        return grid[0][2]
    
    return None

# Vòng lặp chính
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = event.pos
            clicked_row = mouseY // cell_size
            clicked_col = mouseX // cell_size
            
            if grid[clicked_row][clicked_col] == "":
                grid[clicked_row][clicked_col] = current_player
                winner = check_winner()
                current_player = "O" if current_player == "X" else "X"
                
                if winner:
                    print(f"Người chơi {winner} thắng!")
                    pygame.quit()
                    sys.exit()
    
    screen.fill(WHITE)
    draw_grid()
    draw_marks()
    pygame.display.update()
