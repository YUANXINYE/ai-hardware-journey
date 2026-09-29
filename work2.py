"""随机数统计实验
   用 numpy 生成 1000 个正态分布随机数：
      打印这组数据的均值和标准差（应接近 0 和 1）
      统计落在 [均值−标准差， 均值+标准差] 之间的数的比例（应接近 68%） 
      用 matplotlib 画直方图：plt.hist(data, bins=30)，最后 plt.show()  
"""

import numpy as np

data = np.random.normal(0, 1, 1000)   # 均值0，标准差1，1000个

print("平均值 mean:", np.mean(data))      # 应接近 0
print("标准差 std:", np.std(data))        # 应接近 1

mask = (data > np.mean(data) - np.std(data)) & (data < np.mean(data) + np.std(data))
count_true = mask.sum()        # True按1计数，这就是布尔索引的妙处
ratio = count_true / 1000
print("满足条件的元素个数:", count_true)
print("落在±1σ内的比例:", ratio)          # 应接近 0.68

import matplotlib.pyplot as plt
plt.hist(data, bins=30)
plt.show()