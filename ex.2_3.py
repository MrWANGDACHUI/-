#蟒蛇
from turtle import*
setup (800,500,10,10)
up()
fd(-250)
down()
pensize(20)
pencolor("grey")
seth(-40)
for i in range(4):
    pencolor("black")
    circle(40,80)
    pencolor("grey")
    circle(-40,80)
circle(40,40)
pencolor("black")
fd(40)
circle(16,180)
fd(40*2/3)
    
