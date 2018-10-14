#无角正方形
from turtle import*
setup(800,500,10,10)
pensize(3)
for i in range(4):
    left(90)
    up()
    fd(50)
    down()
    fd(100)
    up()
    fd(50)
