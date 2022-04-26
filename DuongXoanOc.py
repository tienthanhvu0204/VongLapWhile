from ast import While
from math import dist
import turtle
screen = turtle.Screen ()
screen.setup (1000, 1000)
screen.title ("Đường xoắn ốc")
d = 1
while True:
    turtle.fd (d)
    turtle.lt (10)
    d += 0.2
    if turtle.distance (0, 0) >= 380:
        turtle.hideturtle ()
        break

turtle.done ()    

