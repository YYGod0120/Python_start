import math


class yuan:
    def __init__(self, color, r):
        self.r = r
        self.color = color

    def jisuan(self):
        area = math.pi * self.r * self.r
        c = 2 * math.pi * self.r
        print(f"这个圆的颜色是{self.color}，这个圆的面积是{area}，这个圆的周长是{c}")



yuan1 = yuan("红色",5)
yuan1.jisuan()


