from turtle import*
import turtle

colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(150):
    t.pencolor(colors[x%6])
    t.width(x/100 + 1)
    t.forward(x)
    t.left(59)

color('purple','red')
begin_fill()
left(50)
forward(100)
circle(40,180)
left(260)
circle(40,180)
forward(100)
end_fill()

color('red')
begin_fill()
left(2)
forward(20)
circle(-5,90)
forward(200)
circle(5,90)
forward(100)
circle(-5,90)
forward(50)
circle(-5,90)
forward(200)
circle(-5,90)
forward(200)
end_fill()
done()
