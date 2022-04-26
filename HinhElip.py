import turtle
import random

screen = turtle.Screen ()
screen.setup (1000, 1000)
screen.title ("Elip")
screen.bgcolor ("black")
screen.colormode(255)
turtle.pensize (2)
turtle.speed (10)

#turtle.fd (200)

# t là khoảng tịnh tiến ban đầu
# dt là khoảng cách cộng thêm mỗi khi quay góc dx
# x biến góc vẽ elip
# dx góc quay mỗi khoảng tịnh tiến
# y biến góc quay vẽ tất cả các elip

t = 2
dt = 1
x = 0
dx = 6
y = 0

while y < 360:
    turtle.color (random.randint (0, 255), random.randint (0, 255), random.randint (0, 255))
    for i in range (2):
        while x <= 90:
            turtle.fd (t)
            turtle.lt (dx)
            t += dt
            x += dx
        while x <= 180:
            turtle.fd (t)
            turtle.lt (dx)
            t -= dt
            x += dx
        x -= 180
    y += 10
    turtle.lt (10)
turtle.hideturtle ()
turtle.done ()    
