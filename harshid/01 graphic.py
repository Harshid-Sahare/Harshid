import turtle
screen = turtle.Screen()
screen.setup(500, 600, startx=0, starty=100)
square = turtle.Turtle()
square.speed(10)

for i in range(500):
    square.forward(i)
    square.left(91)


import turtle

colors = ['yellow','green','red','white','cyan','blue']

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor('Black')
t.speed(30)

for i in range(100):
    t.color(colors[i%6])
    t.fd(i*5)
    t.left(200)
    t.width(2)