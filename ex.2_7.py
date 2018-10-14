#六芒星
import turtle as t
def drawTriangle(e,direct=120):
    for i in range(3):
        t.fd(e)
        t.left(direct)

t.seth(-90)
drawTriangle(200,120)
t.up()
t.seth(0)
t.fd(115.5)
t.seth(-90)
t.fd(200)
t.down()
t.seth(90)
drawTriangle(200,120)

    
