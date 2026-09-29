#循环的学习
i = 1
while i <= 10:
    print(f"第{i}次实验")
    i += 1
k = 1
num = 0
while k <= 100:
    k = k + 1
    num += k
print(f"1到100数字相加的和为: {num}")

#print之后不换行使用end=传参功能
print("hello ")
print("world !")
print("对比上下语句")
print("hello ", end='')
print("world !")
#\t制表符，使数据位对齐
print("123 45678")
print("12345  6789")
print("123\t45678")
print("12345\t6789")