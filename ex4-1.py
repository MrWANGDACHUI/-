#猜数字
a=5
i=0
while True:
    b=int(input(""))
    i=i+1
    if a>b:
        print("遗憾，太小了!")
    elif a<b:
        print("遗憾，太大了!")
        break
    else:
        print("预测{:d}次，你猜中了".format(i))
        
