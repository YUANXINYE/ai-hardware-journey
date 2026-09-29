import torch  #引入pytorch工具包

# 1.创建张量
x = torch.arange(12)
print(x, x.shape)  #打印张量内容和形状
y = torch.tensor([2, 3, 2, 5, 8, 9, 5, 7])
Y = y.reshape(2, 4)
print(y, y.shape)
print(Y)

# 2.改变形状
X = x.reshape(3, 4)  #3行4列
print(X)

# 3.创建特殊张量
print(torch.zeros(2, 3, 4)) #全0，生成两个3*4的零向量矩阵
print(torch.ones(2, 3))
print(torch.randn(3, 4))  #标准正态分布，数据97%概率在[-3——3之间]，也有极小概率在其他
print(torch.rand(2,3)) # [0,1) 均匀分布，数值一定大于等于0，小于1

# 4.运算
x = torch.tensor([1.0, 2, 4, 8])
y = torch.tensor([2, 2, 2, 2])
print(x + y, x * y, x /y, x ** y)
print(torch.exp(x))    #指数

# 5.矩阵乘法
A = torch.arange(12).reshape(3, 4)
B = torch.arange(8).reshape(4, 2)
print("矩阵乘法 A@B:")
print(A @ B)  # 矩阵乘法：(3x4)·(4x2)=(3x2)
print("逐元素相乘 A*A:")
print(A * A)  # 相同位置元素相乘：形状不变

# 6.合并、广播
print(torch.cat((A, A), dim = 0)) #沿行拼接
print(torch.cat((A, A), dim = 1)) #沿列拼接
a = torch.arange(3).reshape(3, 1)
b = torch.arange(2).reshape(1, 2)
print(a + b) #广播:3 x 1 + 1 x 2 = 3 x 2

# 7.与numpy互转（数据预处理常用）
import numpy
A = numpy.array([1.0, 2.0, 3.0, 4.0])
t = torch.tensor(A) #numpy -> torch
print(t, t.numpy()) #torch -> numpy