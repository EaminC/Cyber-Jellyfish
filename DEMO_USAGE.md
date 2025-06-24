# Demo Generator Usage / 演示生成器使用说明

## Overview / 概述

This project now supports generating multiple demo GIFs from YAML configuration files, allowing for asymmetric parameter ranges and easier batch generation.

本项目现在支持从 YAML 配置文件生成多个演示 GIF，允许不对称参数范围和更简便的批量生成。

## Configuration File / 配置文件

Edit `demo_configs.yaml` to define different parameter combinations:

编辑 `demo_configs.yaml` 来定义不同的参数组合：

```yaml
demos:
  - name: "custom_demo"
    description: "自定义演示"
    description_en: "Custom demo"
    filename: "demo_custom.gif"
    limit_x_min: -100
    limit_x_max: 200
    limit_y_min: -50
    limit_y_max: 300
```

## Usage / 使用方法

### Generate All Demos / 生成所有演示

```bash
python generate_demos_from_yaml.py
```

### Generate Specific Demos / 生成指定演示

```bash
python generate_demos_from_yaml.py small moderate asymmetric_y
```

### Generate README Table / 生成 README 表格

```bash
python generate_demos_from_yaml.py table
```

## Parameter Explanation / 参数说明

- `limit_x_min/max`: X-axis coordinate range / X 轴坐标范围
- `limit_y_min/max`: Y-axis coordinate range / Y 轴坐标范围
- `name`: Internal identifier / 内部标识符
- `filename`: Output GIF filename / 输出 GIF 文件名
- `description`: Chinese description / 中文描述
- `description_en`: English description / 英文描述

## Asymmetric Patterns / 不对称图案

The mathematical transformation supports asymmetric ranges, allowing for creative patterns:

数学变换支持不对称范围，可以创造富有创意的图案：

- **Y-axis asymmetric**: `y[-500, 100]` creates downward-biased patterns
- **X-axis asymmetric**: `x[0, 1000]` creates rightward-shifted patterns
- **Quadrant patterns**: `x[0, 500], y[0, 500]` focuses on first quadrant

- **Y 轴不对称**: `y[-500, 100]` 创造向下偏移的图案
- **X 轴不对称**: `x[0, 1000]` 创造向右偏移的图案
- **象限图案**: `x[0, 500], y[0, 500]` 专注于第一象限

## Dependencies / 依赖

Make sure to install PyYAML:

确保安装 PyYAML：

```bash
pip install PyYAML
```
