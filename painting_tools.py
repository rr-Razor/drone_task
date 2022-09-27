import matplotlib.pyplot as plt
import math
import numpy as np


# 绘图工具
class Draw:
    # 创建figure
    figure = plt.figure()
    # 创建axes
    axes = figure.add_subplot(1, 1, 1)

    # 保存FlightPath.csv数据
    paths = [[]]
    # 保存LIDARPoints.csv数据
    points = [[]]

    # 保存扫描点坐标
    x = []
    y = []

    # 路径点个数和扫描点的个数
    num_of_paths = 0
    num_of_points = 0

    def __init__(self, paths_origin, points_origin):
        # 坐标点预处理
        paths = paths_origin[1::2]
        # 将坐标点的单位由米转换为毫米
        for i in range(0, paths.shape[0]):
            for j in range(0, paths.shape[1]):
                paths[i][j] = paths[i][j] * 1000

        self.num_of_paths = paths.shape[0]
        self.num_of_points = points_origin.shape[0]

        # 属性赋值
        self.paths = paths
        self.points = points_origin

    # 绘制飞行轨迹
    def draw_paths(self):
        self.axes.plot(self.paths[:, 0], self.paths[:, 1], c="blue")
        self.axes.scatter(self.paths[:, 0], self.paths[:, 1], c="blue", s=30)

    # 绘制扫描点
    def draw_points(self):
        self.transfer()
        self.axes.scatter(self.x, self.y, c="red", s=2)
        # self.axes.plot(self.x, self.y, c="red")

    # 扫描点坐标转换
    def transfer(self):
        # 遍历扫描点
        p_id = 0
        count = 0

        for i in range(0, self.num_of_points):
            # 判断是否是id行
            if i == count:
                count = count + self.points[i][1] + 1
                p_id = int(self.points[i][0])
            else:
                # 获取扫描点扫描墙壁的坐标
                x = self.paths[p_id][0] + self.points[i][1] * math.cos(self.points[i][0] / 180 * math.pi)
                y = self.paths[p_id][1] - self.points[i][1] * math.sin(self.points[i][0] / 180 * math.pi)
                self.x.append(x)
                self.y.append(y)
        return list(zip(self.x, self.y))

    # 显示绘制结果
    def show(self):
        plt.show()
