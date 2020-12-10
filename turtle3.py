import turtle

window =turtle.Screen()

nav=turtle.Turtle()
nav.shape("turtle")
nav.color("green")

nav.fillcolor("teal")
nav.begin_fill()

nav.penup()

size=10

for _ in range(30):
    nav.stamp()
    size=size+3
   # print(size)
    nav.forward(size)
    nav.right(24)

nav.end_fill()


window.mainloop()
