import turtle as ttl

a= 0
b =0
ttl.bgcolor('black')
ttl.speed(0)
ttl.pencolor('cyan')
ttl.penup()

ttl.goto(0, 200)
ttl.pendown()
while True:
    ttl.forward(a)
    ttl.right(b)
    a += 3
    b += 1