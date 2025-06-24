import pygame
import numpy as np
from PIL import Image
import yaml
import os
from typing import Dict, Any

def load_config(config_file: str = "demo_configs.yaml") -> Dict[str, Any]:
    """从YAML文件加载配置"""
    with open(config_file, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def generate_demo_gif(config: Dict[str, Any], screen_size_x: int = 300, screen_size_y: int = 750):
    """根据配置生成单个演示gif"""
    name = config['name']
    filename = config['filename']
    limit_x_min = config['limit_x_min']
    limit_x_max = config['limit_x_max']
    limit_y_min = config['limit_y_min']
    limit_y_max = config['limit_y_max']
    
    print(f"开始生成 {name} - {filename}")
    print(f"  参数: x[{limit_x_min}, {limit_x_max}], y[{limit_y_min}, {limit_y_max}]")
    
    # 初始化
    pygame.init()
    screen = pygame.display.set_mode((screen_size_x, screen_size_y))
    
    # 网格参数
    grid_size = 150
    x_vals = np.linspace(limit_x_min, limit_x_max, grid_size)
    y_vals = np.linspace(limit_y_min, limit_y_max, grid_size)
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
        if frame % 20 == 0:  # 每20帧打印一次进度
            print(f"  进度: {frame+1}/{max_frames}")

    # 保存gif
    frames[0].save(
        filename,
        save_all=True,
        append_images=frames[1:],
        duration=80,
        loop=0
    )
    
    print(f"  ✅ {filename} 生成完成")
    pygame.quit()

def generate_all_demos(demos_to_generate=None):
    """生成所有或指定的演示"""
    config = load_config()
    demos = config['demos']
    
    if demos_to_generate:
        demos = [d for d in demos if d['name'] in demos_to_generate]
    
    print(f"准备生成 {len(demos)} 个演示:")
    for demo in demos:
        print(f"  - {demo['name']}: {demo['description']}")
    print()
    
    for i, demo in enumerate(demos, 1):
        print(f"[{i}/{len(demos)}] ", end="")
        generate_demo_gif(demo)
        print()

def update_readme_table():
    """更新README中的表格"""
    config = load_config()
    demos = config['demos']
    
    # 生成英文表格
    en_table = "| Configuration | Preview | Description |\n"
    en_table += "|---------------|---------|-------------|\n"
    
    # 生成中文表格  
    cn_table = "| 配置参数 | 预览效果 | 描述 |\n"
    cn_table += "|---------|---------|------|\n"
    
    for demo in demos:
        x_range = f"x[{demo['limit_x_min']}, {demo['limit_x_max']}]"
        y_range = f"y[{demo['limit_y_min']}, {demo['limit_y_max']}]"
        config_str = f"`{x_range}, {y_range}`"
        
        en_table += f"| {config_str} | ![{demo['name']}]({demo['filename']}) | {demo['description_en']} |\n"
        cn_table += f"| {config_str} | ![{demo['name']}]({demo['filename']}) | {demo['description']} |\n"
    
    print("英文表格:")
    print(en_table)
    print("\n中文表格:")
    print(cn_table)

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "table":
            update_readme_table()
        else:
            # 生成指定的演示
            demos_to_generate = sys.argv[1:]
            generate_all_demos(demos_to_generate)
    else:
        # 生成所有演示
        generate_all_demos()
    
    print("🎉 演示生成完成！") 