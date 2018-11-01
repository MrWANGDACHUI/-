a=int(input("请输入您的体重："))
b=0
for i in range(10):
    b=a*0.165
    a=a+0.5
    print("{:2f}".format(b))

