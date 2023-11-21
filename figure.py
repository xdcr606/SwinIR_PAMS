import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import math
# score = [random.randint(0,10) for i in range(100)] # 此处随机生成一个数值列表
# score = pd.Series(score)
# se1 = pd.cut(score, [0,1,2,5,8,10]) # 统计0-1,1-2依次类推各个区间的数值数量
# print(se1.value_counts())

def draw():
    data = np.loadtxt("./res1.txt")
    data_series = data.flatten()
    min_v, max_v = min(data_series), max(data_series)
    cnt = 20
    pad = math.ceil((max_v - min_v) / cnt)
    sections = []
    v = min_v
    while v < max_v:
        sections.append(v)
        v += pad
    sections.append(max_v)
    data_pd = pd.cut(data_series, sections)
    res = data_pd.value_counts()
    plt.bar(sections[:-1], res, width=8, align='edge')
    plt.xticks(sections)
    plt.xlabel("Max Value")
    plt.ylabel("Numbers")
    plt.show()

if __name__ == "__main__":
    draw()