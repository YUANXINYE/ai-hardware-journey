#将实例化两个标量，并执行算术运算，即加法、乘法、除法和指数。
import torch

x = torch.tensor(3.0)
y = torch.tensor(2.0)
x + y, x * y, x / y, x ** y
print(f"{x + y}, {x * y}, {x / y}, {x ** y}")

#一维张量表示向量,可以具有任意长度
x = torch.arange(4)
print(f"一维张量x等于:{x}")
print(f"{x[1]}")  #通过张量的索引来访问任一元素本身

#访问张量的长度
x = torch.tensor([1, 2, 3, 4, 5])
print(f"向量元素个数: {len(x)}, 向量类别: {type(x)}, 形状:{x.shape}")

#指定两个分量和来创建一个形状为m x n的矩阵
A = torch.arange(20).reshape(5, 4)
print(A)

B = torch.arange(6).reshape(2, 3)
print(B)
print(B.T)  #转置，行变列，列变行
#特殊矩阵，转置等于其本身
C = torch.tensor([[1, 2, 3], [2, 0, 4], [3, 4, 5]])
print(C)
print(C == C.T)

#张量
X = torch.arange(24).reshape(2, 3, 4) #两层，每层3 x 4
B = A.clone()  # 通过分配新内存，克隆A给B
print(X)