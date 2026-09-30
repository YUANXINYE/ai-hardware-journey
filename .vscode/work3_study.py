import torch
x = torch.arange(4.0, requires_grad = True) #开启求导（梯度追踪）
y = 2 * torch.dot(x, x)  #点积分
y.backward() #自动求导,保存到x.grad
print(x.grad)    

#study1
k = torch.arange(5.0, requires_grad = True)
y = k.sum()
y.backward()  #反向求导
print(f"y = {y.item()}") #.item转换位为数字（浮点型）
print(f"自动求导 k.grand = {k.grad.tolist()}")

#study2
k2 = torch.arange(5.0, requires_grad = True)
y2 = ( k2 * k2 ).sum()
y2.backward()
print(f"y2 = {y2}")
print(f"自动求导 k2.grand = {k2.grad}")

#study3
k3 = torch.tensor([2.0, 4.0, 3.0, 1.0, 7.0], requires_grad= True)
y3 = 3 * torch.dot(k3, k3)
y3.backward()
print(f"y3 = {y3}")
print(f"自动求导结果是: {k3.grad}")

#study4三角函数
print("=" * 58)
print("例4:y = sum(sin(x))")
# 数学推导：(sin x)' = cos x，所以梯度 = cos(x) = [1, cos1, cos2, cos3]
x = torch.arange(4.0, requires_grad=True)
y = torch.sin(x).sum()
y.backward()
print(f"y   = {y.item():.4f}")
print(f"自动求导 x.grad = {x.grad.tolist()}")
print(f"手动公式 cos(x) = {torch.cos(x).tolist()}  -> 一致\n")