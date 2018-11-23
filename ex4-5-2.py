from random import *
seed(0)
a = randint(0,100)
i = 0;
while True:
    try:
        b = int(input('请输入一个0-100之间的整数：'))
    except:
        print("输入错误！")
        continue
        
    i=i+1
    if a > b:
        print('遗憾，太小了')
    elif a == b:
        print('预测{}次，你猜中了！'.format(i))
        break
    else:
        print('遗憾，太大了')
