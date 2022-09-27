import copy

import pandas as pd
from painting_tools import Draw
from wall_map import Mapping


# 任务一：数据可视化
def task1_display(paths, points):
    draw = Draw(paths, points)
    # 绘制飞行路径
    draw.draw_paths()
    # 绘制墙壁
    draw.draw_points()
    # 绘制结果展示
    draw.show()


# 任务五：获取墙壁映射
def task5_mapping(paths, points):
    # 获取墙壁扫描点
    draw2 = Draw(paths, points)
    wall_points = draw2.transfer()
    # 根据扫描点计算墙壁映射
    mapping = Mapping(wall_points)
    mapping.wall_mapping()


if __name__ == '__main__':
    # 读数据
    paths_origin = pd.read_csv("./data/input/FlightPath.csv", header=None).values
    points_origin = pd.read_csv("./data/input/LIDARPoints.csv", header=None).values

    # 拷贝数据
    paths1 = copy.deepcopy(paths_origin)
    points1 = copy.deepcopy(points_origin)
    paths2 = copy.deepcopy(paths_origin)
    points2 = copy.deepcopy(points_origin)

    # 调用任务一方法
    task1_display(paths1, points1)
    # 调用任务五方法
    task5_mapping(paths2, points2)

    # 写数据
    # print(points)
    # pd.DataFrame(points).to_csv("./data/output/test.csv", index=None, header=None)
    # points.to_csv("./data/output/test.csv", index=None)
