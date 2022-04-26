import turtle
x = float (input ("Nhập chiều dài cạnh hình vuông: "))
i = 0
screen = turtle.Screen ()
screen.setup (800,800)
screen.title ("Vẽ hình vuông")
t = turtle.Turtle ()
while i < 4:
    t.fd (x)
    t.lt (90)
    i += 1
t.hideturtle ()
turtle.done ()