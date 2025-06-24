# 赛博水母 (Cyber Jellyfish)

中文 | [English](./README.md)

一个基于 Python 和 Pygame 的动态赛博电子水母动画项目。

![Demo](demo.gif)

## 特性

- 🌊 流畅的实时动画效果
- 🎨 极简的黑白视觉风格
- 💫 数学函数驱动的有机形态
- 🖥️ 高分辨率渲染
- ⚡ 120fps 流畅体验

## 运行要求

- Python 3.6+
- pygame
- numpy

## 安装依赖

```bash
pip install pygame numpy
```

## 运行

```bash
python draw.py
```

## 技术原理

这个动画使用复杂的数学变换来模拟水母的游动：

- 通过三角函数和指数函数创建有机的形态变化
- 使用网格点变换来生成流畅的动画效果
- 实时计算每一帧的粒子位置

### 核心数学公式

水母动画通过以下数学变换生成：

```
k = 5 × cos(x/14) × cos(y/30)
e = y/8 - 13
d = (k² + e²)/59 + 4
a = arctan2(e, k)
q = 60 - sin(a × e) + k × (3 + (4/d) × sin(d² - 2t))
c = d/2 + e/99 - t/18

X = q × sin(c) × scale + center_x
Y = (q + 9d) × cos(c) × scale + center_y
```

其中：

- `(x, y)` 是初始网格坐标
- `t` 是时间参数 (frame/30.0)
- `scale` 控制大小 (默认: 1.8)
- `center_x, center_y` 是屏幕中心坐标

## 参数说明

- `grid_size`: 控制渲染精度，数值越大越细腻
- `scale`: 控制水母大小
- `screen_size_x/y`: 窗口尺寸
- `clock.tick()`: 控制帧率

## 贡献

欢迎提交 Issues 和 Pull Requests 来改进这个项目！

## 许可证

MIT License
