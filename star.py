import turtle

win=turtle.Screen()
nav=turtle.Turtle()

nav.hideturtle()

nav.shape("turtle")
nav.stamp()
move=30
nav.fillcolor("teal")
nav.begin_fill()

for _ in range(12):
    
    
    nav.penup()
    nav.forward(50)
    nav.pendown()
    nav.forward(25)
    nav.penup()
    nav.forward(15)
    nav.stamp()
    nav.home()
    nav.right(move)
    move=move+30
nav.end_fill()
win.mainloop()
