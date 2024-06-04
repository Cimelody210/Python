import turtle

t = turtle.Turtle()
t.speed(5)
t.pensize(3)
t.penup()
t.goto(0, -200)
t.pendown()

# vẽ đầu Pikachu
t.fillcolor('#FED836')
t.begin_fill()
t.circle(120)
t.end_fill()

# vẽ tai trái
t.penup()
t.goto(-70, 120)
t.pendown()
t.setheading(215)
t.fillcolor('#FED836')
t.begin_fill()
t.circle(50, 90)
t.setheading(90)
t.circle(50, 90)
t.end_fill()

# vẽ tai phải
t.penup()
t.goto(70, 120)
t.pendown()
t.setheading(325)
t.fillcolor('#FED836')
t.begin_fill()
t.circle(50, -90)
t.setheading(90)
t.circle(50, -90)
t.end_fill()

# vẽ mắt trái
t.penup()
t.goto(-40, 50)
t.pendown()
t.setheading(0)
t.fillcolor('#FFFFFF')
t.begin_fill()
t.circle(30)
t.end_fill()

t.penup()
t.goto(-30, 60)
t.pendown()
t.fillcolor('#000000')
t.begin_fill()
t.circle(15)
t.end_fill()

# vẽ mắt phải
t.penup()
t.goto(40, 50)
t.pendown()
t.setheading(0)
t.fillcolor('#FFFFFF')
t.begin_fill()
t.circle(30)
t.end_fill()

t.penup()
t.goto(30, 60)
t.pendown()
t.fillcolor('#000000')
t.begin_fill()
t.circle(15)
t.end_fill()

# vẽ miệng
t.penup()
t.goto(-40, 0)
t.pendown()
t.setheading(-90)
t.pensize(5)
t.circle(40, 180)

# vẽ đuôi
t.penup()
t.goto(-120, -30)
t.pendown()
t.setheading(-45)
t.fillcolor('#FED836')
t.begin_fill()
t.circle(150, 90)
t.circle(150, -90)
t.end_fill()

t.hideturtle()
turtle.done()
