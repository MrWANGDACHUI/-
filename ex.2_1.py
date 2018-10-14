#e1.1TempConvert.py
TempStr = eval('input("请输入带有温度符号的温度值:")')
if TempStr[-1] in ['F','f']:
    C = int((eval(TempStr[0:-1]) - 32)/1.8)
    print("温度转换后的数值{:d}C".format(C))
elif TempStr[-1] in ['C','c']:
    F = int(1.8*eval(TempStr[0:-1]) + 32)
    print("转换后的温度是{:d}F".format(F))
else:
    print("错误格式")
