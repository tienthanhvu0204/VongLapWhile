import turtle
import random
s = turtle.Screen ()
s.screensize (800, 800)
s.title ("Rùa bị quản")
t = turtle.Turtle ()
t.shapesize (3, 5, 1)
t.hideturtle ()
t.penup ()
t.goto (0, -300)
t.pendown ()
t.circle (300)
t.penup ()
t.home ()
t.showturtle ()

i = 0
while i < 10:
    a = random.randint (0, 360)
    t.lt (a)
    t.fd (300)
    t.home ()
    i += 1
turtle.done ()
