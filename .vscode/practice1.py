name = "缘歆有限公司"
stock_price = 19.99  #当前股价
stock_code = "股票代码"
stock_price_daily_growth_father = 1.2  #增涨系数
growth_days = 16   #经过天数
print(f"{name},股票代码是:001989,当前股价:{stock_price}")

#计算16天后股价达到什么价位
stock_price = stock_price * ( stock_price_daily_growth_father ** growth_days)
print("每日增长系数: %f, 经过 %d 天的增长后股价达到 %f" % ( stock_price_daily_growth_father, growth_days, stock_price ))