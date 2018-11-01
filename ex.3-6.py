#e4.3TextProgress.py
import time
scale = 50
print("执行开始".center(scale//2,'-'))
t = time.clock()
for i in range(scale+1):
    a = '*' * i
    b = '.' * (scale - i)
    print("\rStarting[{}->{}]Done!".format(a,b),end='')
    time.sleep(0.05)
print("\n"+"执行结束".center(scale//2,'-'))
