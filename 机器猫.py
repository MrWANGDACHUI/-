#机器猫

#脸
from turtle import*
speed(0)
setup(600,800,0,10)
pensize(8)
color("black","blue")
begin_fill()
circle(200)
end_fill()
color("black","white")
begin_fill()
circle(157)
end_fill()

#眼睛
up()
goto(48,245)
down()
color("black","white")
begin_fill()
circle(45)
end_fill()
goto(70,245)
color("black","black")
begin_fill()
circle(10)
end_fill()
up()
goto(-48,245)
down()
color("black","white")
begin_fill()
circle(45)
end_fill()
goto(-20,245)
color("black","black")
begin_fill()
circle(10)
end_fill()

#鼻子
up()
goto(0,185)
down()
color("black","red")
begin_fill()
circle(23)
end_fill()

#嘴巴
up()
goto(0,50)
down()
circle(120,75)
up()
circle(120,210)
down()
circle(120,75)
seth(90)
fd(120)

#舌头
up()
goto(0,50)
seth(0)
circle(120,25)
down()
fillcolor("red")
begin_fill()
seth(120)
fd(20)
circle(-25,180)
fd(12)
end_fill()
