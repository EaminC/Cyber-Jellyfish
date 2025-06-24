import pygame
import numpy as np
from PIL import Image
import os

def generate_demo_gif(limit_x, limit_y, filename, description):
    """生成指定参数的演示gif"""
    print(f"开始生成 {description} - {filename}")
    
    # 初始化
    pygame.init()
    screen_size_x = 300
    screen_size_y = 750
    screen = pygame.display.set_mode((screen_size_x, screen_size_y))
    
    # 网格参数
    grid_size = 150
    x_vals = np.linspace(-limit_x, limit_x, grid_size)
    y_vals = np.linspace(-limit_y, limit_y, grid_size)
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
        scale = 1.8
        X = q * np.sin(c) * scale + screen_size_x // 2
        Y = (q + 9 * d) * np.cos(c) * scale + screen_size_y // 2
        return X, Y

    # 录制参数
    frames = []
    max_frames = 120  # 4秒动画

    # 录制循环
    for frame in range(max_frames):
        t = frame / 30.0
        X, Y = compute_transformed(X0_flat, Y0_flat, t)
        
        screen.fill((0, 0, 0))
        for x, y in zip(X, Y):
            if 0 <= x < screen_size_x and 0 <= y < screen_size_y:
                screen.set_at((int(x), int(y)), (255, 255, 255))
        
        # 保存当前帧
        pygame_image = pygame.surfarray.array3d(screen)
        pygame_image = pygame_image.swapaxes(0, 1)
        pil_image = Image.fromarray(pygame_image)
        frames.append(pil_image)
        
        pygame.display.flip()
        print(f"  进度: {frame+1}/{max_frames}")

    # 保存gif
    frames[0].save(
        filename,
        save_all=True,
        append_images=frames[1:],
        duration=80,  # 每帧持续时间
        loop=0
    )
    
    print(f"  ✅ {filename} 生成完成")
    pygame.quit()

# 生成三个不同参数的演示
demos = [
    (15, 15, "demo_small.gif", "小范围参数 (limit_x=15, limit_y=15)"),
    (11111111195, 15, "demo_wide.gif", "宽范围参数 (limit_x=11111111195, limit_y=15)"),
    (11111111195, 95, "demo_current.gif", "当前参数 (limit_x=11111111195, limit_y=95)")
]

for limit_x, limit_y, filename, description in demos:
    generate_demo_gif(limit_x, limit_y, filename, description)
    print()

print("🎉 所有演示gif生成完成！") 