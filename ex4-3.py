n1, n2 = eval(input('请输入两个整数，中间用逗号隔开：'))
x, y = n1, n2
r = x % y
while r > 0:
    x,y = y,r
    r = x % y

print('{}和{}最大公约数是：{}， 最小公倍数是：{}'.format(n1, n2, y, n1 * n2 / y))
