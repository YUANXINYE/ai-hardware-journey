#bool变量的运用和运算判断
bool_1 = True
bool_2 = False
print(f"bool_1变量的内容是: {bool_1}, 类型是{type(bool_1)}")
num1 = 1
num2 = 2
num3 = 2
print(f"num1 > num2 : {num1 > num2}")
print(f"num2 == num3 : {num2 == num3}")
print(f"num2 >= num3: {num2 >= num3}, num1数据类型为: { type(num1) }")

#if条件语句
age = 20
if age >= 18:   #注意不要忘记：
    print("我已经成年了")  #两个空格代表所属关系，属于上一个if
    print("我今年步入大学")