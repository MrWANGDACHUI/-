#汇率换算
M = eval('input("带有货币符号的数值:")')
if M[-1] in ['R','r']:
    D = int(eval(M[0:-1])/6)
    print("转换后的货币是:{:d}dollar".format(D))
elif M[-1] in ['D','d']:
    R = int(eval(M[0:-1])*6)
    print("转换后的货币是:{:d}RMB".format(R))
else:
    print("输入格式错误")
