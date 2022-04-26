import turtle
import random as r
s = turtle.Screen ()
s.bgcolor ("orange")
s.setup (1050, 500)
s.title ("Rùa tập thể dục")
t = turtle.Turtle ()
t.hideturtle ()
t.penup ()
t.goto (-500, 0)
t.pensize (5)
t.color ("red")
t.showturtle ()
# a = r.randint (5, 10)
# b = r.randint (5, 10)
i = 0
while i < 1000:
    a = r.randint (0, 3)
    t.pendown () if a < 2 else t.penup ()
    x = r.randint (5, 10)
    t.fd (x)
    i += x
    
"""   t.pendown ()
    t.fd (a)
    t.penup ()
    t.fd (b)
    i += (a + b)
"""
turtle.done ()

"""
a = r.randint (0, 2)
x = r.randint (5, 10)
print (a)
print (x)
"""