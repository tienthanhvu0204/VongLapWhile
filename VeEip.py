import turtle
import random

screen = turtle.Screen ()
screen.setup (1000, 1000)
screen.title ("Elip")
screen.bgcolor ("black")
screen.colormode(255)
turtle.pensize (2)
turtle.speed (10)

r = 200

y = 0

while y < 360:
    turtle.color (random.randint (0, 255), random.randint (0, 255), random.randint (0, 255))
    for i in range (2):
        turtle.circle (r, 90)
        turtle.circle (r / 2, 90)
    y += 20
    turtle.lt (20)

turtle.hideturtle ()
turtle.done ()    
