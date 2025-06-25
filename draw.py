import pygame
import numpy as np

# 初始化
pygame.init()
screen_size_x = 400
screen_size_y = 400
screen = pygame.display.set_mode((screen_size_x, screen_size_y))
clock = pygame.time.Clock()

# 网格参数 - 支持不对称范围
grid_size = 140
limit_x_min = -10000
limit_x_max = 10000
limit_y_min = -46
limit_y_max = 200
generate_demo = True  # 是否生成演示gif

# GIF生成参数
gif_fps = 30  # GIF帧率 (frames per second) - 建议范围: 10-30
gif_duration_seconds = 4  # GIF总时长 (秒) - 建议范围: 2-8秒
# 注意: 高帧率 + 长时长 = 大文件 + 慢生成

x_vals = np.linspace(limit_x_min, limit_x_max, grid_size)  # 不对称X范围
y_vals = np.linspace(limit_y_min, limit_y_max, grid_size)  # 不对称Y范围
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
    X = (q + 2 * d) * np.sin(c) * scale + screen_size_x // 2  # 居中
    Y = (q + 2 * d) * np.cos(c) * scale + screen_size_y // 2  # 居中
    return X, Y

# Demo生成功能
if generate_demo:
    from PIL import Image
    print("🎬 开始生成演示gif...")
    
    # 计算帧数和时间参数
    max_frames = int(gif_fps * gif_duration_seconds)
    frame_duration_ms = int(1000 / gif_fps)  # 每帧持续时间(毫秒)
    time_step = gif_duration_seconds / max_frames  # 时间步长
    
    print(f"📊 GIF参数: {gif_fps} FPS, {gif_duration_seconds}秒, 总帧数: {max_frames}")
    
    frames = []
    
    for frame in range(max_frames):
        t = frame * time_step
        X, Y = compute_transformed(X0_flat, Y0_flat, t)
        
        screen.fill((0, 0, 0))
        for x, y in zip(X, Y):
            if 0 <= x < screen_size_x and 0 <= y < screen_size_y:
                screen.set_at((int(x), int(y)), (255, 255, 255))
        
        # 保存帧
        pygame_image = pygame.surfarray.array3d(screen)
        pygame_image = pygame_image.swapaxes(0, 1)
        pil_image = Image.fromarray(pygame_image)
        frames.append(pil_image)
        
        pygame.display.flip()
        if frame % max(1, max_frames // 5) == 0:  # 显示5次进度
            print(f"  进度: {frame+1}/{max_frames}")
    
    # 保存gif
    frames[0].save('demo.gif', save_all=True, append_images=frames[1:], duration=frame_duration_ms, loop=0)
    print(f"✅ demo.gif 生成完成 ({gif_fps} FPS, {gif_duration_seconds}秒)")
    print("🎮 继续在pygame窗口中观看动画...")

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
    clock.tick(120)  # 120 FPS
    frame += 1

pygame.quit()