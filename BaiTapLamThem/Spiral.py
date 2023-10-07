import turtle as ttl
t = ttl.Turtle()
ch=  ttl.Screen()

ch.bgcolor("black")
t.width(3)
t.speed(15)

colors = ['red','cyan','orange','pink']
for i in range(400):
    t.pencolor(colors[i % 4])
    t.forward(i*4)
    t.right(121)