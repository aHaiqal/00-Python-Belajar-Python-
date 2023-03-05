import turtle

turtle.pensize(1)
turtle.speed(1)
turtle.color("black")
turtle.begin_fill()
turtle.fillcolor("red")
turtle.left(150)
turtle.forward(180)
turtle.circle(-90,180)
turtle.setheading(60)
turtle.circle(-90,180)
turtle.forward(180)
turtle.end_fill()
turtle.mainloop()


# Kue ulang tahun
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('lightyellow')
#s.tracer(0)

t.penup()
t.goto(-150, -100)
t.pendown()
t.pensize(2)
t.color('black', 'pink')
t.begin_fill()
for i in range(3):
    t.forward(300)
    t.left(90)
    t.forward(125)
    t.left(90)


t.end_fill()
t.forward(300)
t.left(90)

# Lingkaran
t.color('black', 'yellow')
t.begin_fill()
t.circle(50, 180)
for i in range(2):
    t.left(180)
    t.circle(50, 180)
t.end_fill()

turtle.done()
