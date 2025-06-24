import pygame
import numpy as np

# 初始化
pygame.init()
screen_size_x = 400
screen_size_y = 400
screen = pygame.display.set_mode((screen_size_x, screen_size_y))
clock = pygame.time.Clock()

# 网格参数 - 增加密度让动画更细腻
grid_size = 150
limit_x = 11111111195
limit_y = 100
x_vals = np.linspace(-limit_x, limit_x, grid_size)  # 调整范围
y_vals = np.linspace(-limit_y, limit_y, grid_size)  # 调整范围
X0, Y0 = np.meshgrid(x_vals, y_vals)
X0_flat = X0.flatten()
Y0_flat = Y0.flatten()

def compute_transformed(x, y, t):
    k = 5 * np.cos(x / 14) * np.cos(y / 30)
    e = y / 8 - 13
    d = (k**2 + e**2) / 59 + 4
    a = np.arctan2(e, k)
    q = 60 - np.sin(a * e) + k * (3 + (4 / d) * np.sin(d**2 - 2 * t))
    c = d / 2 + e / 99 - t / 18
    # 调整缩放和偏移，让水母居中并放大
    scale = 1.8  # 放大倍数
    X = (q + 2 * d ) * np.sin(c) * scale + screen_size_x // 2  # 居中
    Y = (q + 2 * d) * np.cos(c) * scale + screen_size_y // 2  # 居中
    return X, Y

# 主循环
running = True
frame = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    t = frame / 30.0
    X, Y = compute_transformed(X0_flat, Y0_flat, t)
    
    screen.fill((0, 0, 0))  # 黑底
    for x, y in zip(X, Y):
        if 0 <= x < screen_size_x and 0 <= y < screen_size_y:
            screen.set_at((int(x), int(y)), (255, 255, 255))  # 白点
    
    pygame.display.flip()
    clock.tick(120)  # 60 FPS
    frame += 1

pygame.quit()