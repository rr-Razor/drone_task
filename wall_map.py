import numpy as np
import pandas as pd


# 墙壁映射工具
class Mapping:
    # 墙壁扫描点
    wall_points = [[]]
    # 墙壁映射
    wall_map = []

    def __init__(self, wall_points):
        # 将浮点数转换为整数
        self.wall_points = np.array(wall_points).astype(dtype=int)
        # 将整数个十位省略
        for i in range(0, self.wall_points.shape[0]):
            for j in range(0, self.wall_points.shape[1]):
                self.wall_points[i][j] = int(self.wall_points[i][j] / 100) * 100

    def sort_points(self, flag):
        if flag == 1:
            # 按照先行再列从小到大排序
            index = np.lexsort((self.wall_points[:, 1], self.wall_points[:, 0]))
            self.wall_points = self.wall_points[index]
        else:
            # 按照先列再行从小到大排序
            index = np.lexsort((self.wall_points[:, 0], self.wall_points[:, 1]))
            self.wall_points = self.wall_points[index]

    def wall_xy(self, axis):
        # 对墙壁扫描点进行排序处理
        self.sort_points(axis)
        # 先找竖着的墙
        x_start = self.wall_points[0][0]
        y_start = self.wall_points[0][1]

        for i in range(1, self.wall_points.shape[0]):
            # 判断是否在同一竖线上
            a = 0
            b = 0
            if axis == 1:
                a = 0
                b = x_start
            else:
                a = 1
                b = y_start
            if self.wall_points[i][a] != b:
                if x_start != self.wall_points[i - 1][0] or y_start != self.wall_points[i - 1][1]:
                    x_end = self.wall_points[i - 1][0]
                    y_end = self.wall_points[i - 1][1]

                    self.wall_map.append([x_start, y_start, x_end, y_end])

                x_start = self.wall_points[i][0]
                y_start = self.wall_points[i][1]

            else:
                # 判断是否属于同一面墙
                if self.wall_points[i][axis] - self.wall_points[i - 1][axis] > 100:
                    if x_start != self.wall_points[i - 1][0] or y_start != self.wall_points[i - 1][1]:
                        x_end = self.wall_points[i - 1][0]
                        y_end = self.wall_points[i - 1][1]

                        self.wall_map.append([x_start, y_start, x_end, y_end])

                    if axis == 1:
                        y_start = self.wall_points[i][1]
                    else:
                        x_start = self.wall_points[i][0]

        x_end = self.wall_points[self.wall_points.shape[0] - 1][0]
        y_end = self.wall_points[self.wall_points.shape[0] - 1][1]

        self.wall_map.append([x_start, y_start, x_end, y_end])

    def wall_mapping(self):
        # 找出y轴走向的墙壁
        self.wall_xy(1)

        # 找出x轴走向的墙壁
        self.wall_xy(0)

        # 输出墙壁映射结果
        pd.DataFrame(self.wall_map).to_csv("./data/output/Mapping.csv", index=None, header=None)
