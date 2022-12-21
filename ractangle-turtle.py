import turtle
tao=turtle.Pen()
tao.shape('turtle')
def rectangle():
    for i in range(4):
        tao.fd(100)
        tao.lt(90)
        
def go(x,y):
    tao.penup()
    tao.goto(x,y)
    tao.pendown()

go(100,100)
rectangle()
