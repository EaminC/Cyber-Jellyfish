# Cyber Jellyfish

English | [中文](./README_CN.md)

A dynamic cyber jellyfish animation project based on Python and Pygame.

![Demo](demo.gif)

## Features

- 🌊 Smooth real-time animation effects
- 🎨 Minimalist black and white visual style
- 💫 Organic forms driven by mathematical functions
- 🖥️ High-resolution rendering
- ⚡ Smooth 120fps experience

## Requirements

- Python 3.6+
- pygame
- numpy

## Installation

```bash
pip install pygame numpy
```

## Usage

```bash
python draw.py
```

## Technical Principles

This animation uses complex mathematical transformations to simulate jellyfish swimming:

- Creates organic morphological changes through trigonometric and exponential functions
- Uses grid point transformations to generate smooth animation effects
- Real-time calculation of particle positions for each frame

### Core Mathematical Formulas

The jellyfish animation is generated through the following mathematical transformations:

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

Where:

- `(x, y)` are the initial grid coordinates
- `t` is the time parameter (frame/30.0)
- `scale` controls the size (default: 1.8)
- `center_x, center_y` are the screen center coordinates

## Parameter Description

- `grid_size`: Controls rendering precision, higher values for more detail
- `scale`: Controls jellyfish size
- `screen_size_x/y`: Window dimensions
- `clock.tick()`: Controls frame rate

## Contributing

Welcome to submit Issues and Pull Requests to improve this project!

## License

MIT License

idea 来源互联网 实现由 claude agent 完成
