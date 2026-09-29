#获取键盘输入数据（input）
age = input("请输入你的年龄: ")  #输入的数据为字符串型，需要转换
age = int(age)
#判断是否是成年人(if/else语句)
if age >= 18:
    print("您已是成年人, 需要全票")
elif age > 10 & age  < 18:
    print("您属于未成年人可以享受半票优惠")
else:
    print("您属于儿童, 可以享受免票优惠")
print("亲, 祝您游玩愉快！")
print("______________")

#猜数游戏
import random

# 随机生成1~100的整数
secret_num = random.randint(1,100)
print("猜数字游戏!我已经生成1~100之间数字,快来猜")
n = 0
while True:
    guess = int(input("请输入你猜的数字："))
    if guess > secret_num:
        print("猜大啦！")
        n += 1
    elif guess < secret_num:
        print("猜小啦！")
        n += 1
    else:
        print(f"恭喜！猜对了，数字就是{secret_num}, 您一共猜测了{n}次")
        break  #对True无限循环的结束

#嵌套语句
if int(input("请输入你的身高:")) > 120:
    print("身高大于120cm, 无法享受免费")
    print("如果您是VIP3及以上用户也属于免票客人")
    if int(input("请告诉我您的VIP等级是: ")) > 3:
        print("恭喜您的VIP等级大于VIP3, 可以享受免票优惠")
    else:
        print("抱歉，您不满足免票条件，请缴费")
else:
    print("欢迎小朋友, 你可以免费游玩哦，祝你玩的开心")