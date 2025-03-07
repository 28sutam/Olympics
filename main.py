import turtle

screen = turtle.Screen()
screen.screensize(500,500)
screen.bgcolor("tan")

t = turtle.Turtle()

t.penup()
t.pencolor('blue')
t.goto(-80,15)
t.pendown()
t.circle(35)
t.penup()

t.penup()
t.pencolor('black')
t.goto(0,15)
t.pendown()
t.circle(35)
t.penup()

t.penup()
t.pencolor('red')
t.goto(80,15)
t.pendown()
t.circle(35)
t.penup()

t.penup()
t.pencolor("green")
t.goto(40,-15)
t.pendown()
t.circle(35)
t.penup()

t.penup()
t.pencolor('yellow')
t.goto(-40,-15)
t.pendown()
t.circle(35)
t.penup()


t.goto(0,200)
t.pencolor('purple')
t.pendown()
t.write("Winter Olympics", font=("bold",30,"bold italic"),align="center")
t.penup()

t.goto(0,-200)
t.pencolor('purple')
t.pendown()
t.write("2026", font=("bold",30,"bold italic"),align="center")
t.penup()


turtle.done()